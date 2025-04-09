# Market Reports GitHub Pages Site

This repository automatically generates a GitHub Pages site for the daily O'Neil Relative Strength market reports. Reports are published daily at 1:10 PM Los Angeles time.

## Features

- Automatically processes market reports with consistent naming
- Uses ChatGPT-4o-mini API to generate detailed explanations of market conditions
- Creates an aesthetically pleasing static website with Jekyll
- Archives past reports for easy access

## Setup

1. Create a GitHub repository and enable GitHub Pages
2. Set up an OPENAI_API_KEY secret in your repository settings
3. Push this code to your repository
4. GitHub Actions will automatically build and deploy the site daily

## Local Development

```bash
# Install dependencies
bundle install

# Serve locally
bundle exec jekyll serve
```

## How It Works

1. GitHub Actions runs daily at 1:10 PM Los Angeles time
2. The script finds the latest market report
3. It processes the report through ChatGPT-4o-mini to generate detailed analysis
4. Jekyll builds the site with the processed reports
5. The site is deployed to GitHub Pages

## Customization

- Edit `_config.yml` to change site settings
- Modify styles in `assets/css/style.scss`
- Adjust layouts in the `_layouts` directory