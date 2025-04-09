#!/usr/bin/env python

import os
import re
import glob
import yaml
import frontmatter
import datetime
from pathlib import Path
import requests
import openai
import shutil
import sys

# Set up OpenAI API
openai.api_key = os.environ.get("OPENAI_API_KEY")
if not openai.api_key:
    print("WARNING: OPENAI_API_KEY not found in environment variables")

def get_latest_report():
    """Find the latest report in the market_reports directory."""
    # List all directories and files to debug
    print("Current directory:", os.getcwd())
    print("Files in current directory:", os.listdir("."))
    
    # Try multiple patterns
    patterns = [
        "oneil_relative_strength_report_*.md",
        "**/oneil_relative_strength_report_*.md",
        "market_reports/oneil_relative_strength_report_*.md",
        "**/market_reports/oneil_relative_strength_report_*.md"
    ]
    
    for pattern in patterns:
        reports = glob.glob(pattern, recursive=True)
        if reports:
            print(f"Found reports using pattern '{pattern}':", reports)
            return sorted(reports)[-1]
        else:
            print(f"No reports found using pattern '{pattern}'")
    
    print("ERROR: No reports found with any pattern!")
    return None

def process_with_openai(report_content):
    """Process the report content with OpenAI to generate a detailed explanation."""
    if not openai.api_key:
        return "**API Key Error:** OpenAI API key not found. Please add your API key to use the AI summary feature."
        
    prompt = f"""
    As a financial market expert, analyze the following market report and provide a detailed explanation 
    focusing on these aspects:
    
    1. Overall market conditions and the key insights from the Buffett Indicator
    2. Which sectors are showing strength and weakness, and what that means for investors
    3. Notable stocks mentioned in buy and sell recommendations and why they're significant
    4. Strategic recommendations for investors based on the current market conditions
    
    Format your response in markdown with clear headings, bullet points where appropriate, and focus
    on providing meaningful analysis that adds value beyond what's directly stated in the report.
    
    Here's the report to analyze:
    
    {report_content}
    """
    
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # Using GPT-4o mini as specified
            messages=[
                {"role": "system", "content": "You are a market analysis expert who explains financial reports in detail."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1500
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error processing with OpenAI: {e}")
        return f"**API Error:** Unable to generate AI summary. Please see the main report for details."

def convert_markdown_to_jekyll(input_path, output_dir):
    """Convert a standard markdown report to Jekyll format with front matter."""
    print(f"Converting file: {input_path}")
    
    # Check if file exists
    if not os.path.exists(input_path):
        print(f"ERROR: Input file does not exist: {input_path}")
        return None
    
    # Read the report content
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"Successfully read {len(content)} characters from {input_path}")
    
    # Extract date from filename
    date_match = re.search(r'(\d{4}-\d{2}-\d{2})', os.path.basename(input_path))
    if not date_match:
        print(f"Could not extract date from filename: {input_path}")
        return None
    
    report_date = date_match.group(1)
    print(f"Extracted date: {report_date}")
    
    # Process with OpenAI
    print("Processing content with OpenAI...")
    ai_summary = process_with_openai(content)
    print(f"Generated AI summary of {len(ai_summary)} characters")
    
    # Create front matter
    post = frontmatter.Post(
        content,
        title="Daily Relative Strength Report",
        date=report_date,
        layout="report",
        ai_summary=ai_summary
    )
    
    # Create the _reports directory if it doesn't exist
    reports_dir = os.path.join(output_dir, "_reports")
    os.makedirs(reports_dir, exist_ok=True)
    print(f"Created reports directory: {reports_dir}")
    
    # Write the Jekyll post
    output_path = os.path.join(reports_dir, f"{report_date}-market-report.md")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post))
    
    print(f"Successfully wrote Jekyll post to {output_path}")
    return output_path

def copy_images(report_date, output_dir):
    """Copy image files to the Jekyll assets directory."""
    image_files = [
        f"buffett_indicator_{report_date.replace('-', '')}.png",
        f"oneil_relative_strength_{report_date}.png",
        f"sector_strength_{report_date.replace('-', '')}.png"
    ]
    
    print(f"Looking for image files: {image_files}")
    
    assets_dir = os.path.join(output_dir, "assets", "images")
    os.makedirs(assets_dir, exist_ok=True)
    print(f"Created assets directory: {assets_dir}")
    
    for image_file in image_files:
        print(f"Checking for image file: {image_file}")
        if os.path.exists(image_file):
            try:
                shutil.copy2(image_file, os.path.join(assets_dir, image_file))
                print(f"Copied {image_file} to assets directory")
                
                # Update image paths in the report
                update_image_paths(report_date, image_file, output_dir)
            except Exception as e:
                print(f"Error copying {image_file}: {e}")
        else:
            # Try to find the image in other directories
            for root, dirs, files in os.walk('.'):
                for file in files:
                    if file == image_file:
                        full_path = os.path.join(root, file)
                        try:
                            shutil.copy2(full_path, os.path.join(assets_dir, image_file))
                            print(f"Found and copied {full_path} to assets directory")
                            
                            # Update image paths in the report
                            update_image_paths(report_date, image_file, output_dir)
                            break
                        except Exception as e:
                            print(f"Error copying {full_path}: {e}")

def update_image_paths(report_date, image_file, output_dir):
    """Update image paths in the report to point to the assets directory."""
    report_path = os.path.join(output_dir, "_reports", f"{report_date}-market-report.md")
    
    if not os.path.exists(report_path):
        print(f"Report not found for updating image paths: {report_path}")
        return
    
    with open(report_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update image paths - try both formats
    updated_content = content
    
    replacements = [
        (f"![{image_file.split('_')[0].title()}]({image_file})", 
         f"![{image_file.split('_')[0].title()}](/assets/images/{image_file})"),
        (f"![{image_file.split('_')[0].title()} {image_file}]({image_file})", 
         f"![{image_file.split('_')[0].title()}](/assets/images/{image_file})"),
        (f"![{image_file.split('_')[0].title()}](/{image_file})", 
         f"![{image_file.split('_')[0].title()}](/assets/images/{image_file})"),
        (f"![{image_file.split('_')[0].title()}](./{image_file})", 
         f"![{image_file.split('_')[0].title()}](/assets/images/{image_file})"),
    ]
    
    for old, new in replacements:
        if old in updated_content:
            updated_content = updated_content.replace(old, new)
            print(f"Replaced image path: {old} -> {new}")
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"Updated image paths in {report_path}")

def main():
    try:
        # Find the latest report
        latest_report = get_latest_report()
        if not latest_report:
            print("ERROR: No report found. Exiting.")
            sys.exit(1)
        
        print(f"Processing latest report: {latest_report}")
        
        # Extract date from filename
        date_match = re.search(r'(\d{4}-\d{2}-\d{2})', latest_report)
        if not date_match:
            print(f"Could not extract date from filename: {latest_report}")
            sys.exit(1)
        
        report_date = date_match.group(1)
        
        # Set output directory to current directory (repo root)
        output_dir = "."
        
        # Convert markdown to Jekyll format
        converted_path = convert_markdown_to_jekyll(latest_report, output_dir)
        if not converted_path:
            print("ERROR: Failed to convert report to Jekyll format")
            sys.exit(1)
        
        # Copy and update image paths
        copy_images(report_date, output_dir)
        
        print("Report processing completed successfully.")
    except Exception as e:
        print(f"ERROR: An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()