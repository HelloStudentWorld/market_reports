---
layout: home
title: O'Neil Relative Strength Market Reports
---

# Daily Market Reports

Welcome to the O'Neil Relative Strength Market Reports page. These reports are automatically generated daily at 1:10pm Los Angeles time and provide comprehensive market analysis using William O'Neil's relative strength methodology.

## Latest Report

{% assign latest_report = site.reports | sort: 'date' | last %}
{% assign root_report_files = site.static_files | where_exp: "file", "file.path contains 'oneil_relative_strength_report_'" | where_exp: "file", "file.path contains '.md'" %}

{% if latest_report or root_report_files.size > 0 %}
  {% if root_report_files.size > 0 %}
    {% assign latest_file = root_report_files | sort: 'modified_time' | last %}
    {% assign report_date = latest_file.name | remove: "oneil_relative_strength_report_" | remove: ".md" %}
    <a href="{{ latest_file.path | relative_url }}" class="latest-report-link">
      <div class="latest-report">
        <h3>O'Neil Relative Strength Report</h3>
        <p class="report-date">{{ report_date }}</p>
        <div class="report-preview">
          <div class="highlights">
            <h4>Market Insights</h4>
            <p>Daily market analysis using William O'Neil's relative strength methodology.</p>
            <p class="read-more">Read full analysis →</p>
          </div>
        </div>
      </div>
    </a>
  {% else %}
    <a href="{{ latest_report.url | relative_url }}" class="latest-report-link">
      <div class="latest-report">
        <h3>{{ latest_report.title }}</h3>
        <p class="report-date">{{ latest_report.date | date: "%Y-%m-%d" }}</p>
        <div class="report-preview">
          <div class="highlights">
            <h4>Market Insights</h4>
            {{ latest_report.ai_summary | truncatewords: 100 }}
            <p class="read-more">Read full analysis →</p>
          </div>
        </div>
      </div>
    </a>
  {% endif %}
{% else %}
  <div class="latest-report">
    <h3>No reports available yet</h3>
    <p>The first report will be generated soon. Please check back later.</p>
  </div>
{% endif %}

## Previous Reports

{% assign reports = site.reports | sort: 'date' | reverse %}
{% assign root_report_files = site.static_files | where_exp: "file", "file.path contains 'oneil_relative_strength_report_'" | where_exp: "file", "file.path contains '.md'" %}
{% assign all_reports = root_report_files | sort: 'modified_time' | reverse %}

{% if reports.size > 1 or all_reports.size > 1 %}
  {% assign displayed_reports = 0 %}
  {% assign latest_file = all_reports | first %}
  
  {% for file in all_reports limit:10 %}
    {% if file.path != latest_file.path or displayed_reports > 0 %}
      {% assign report_date = file.name | remove: "oneil_relative_strength_report_" | remove: ".md" %}
      <div class="report-item">
        <a href="{{ file.path | relative_url }}">
          <span class="report-date">{{ report_date }}</span> - 
          <span class="report-title">O'Neil Relative Strength Report</span>
        </a>
      </div>
      {% assign displayed_reports = displayed_reports | plus: 1 %}
    {% endif %}
  {% endfor %}
  
  {% for report in reports limit:10 %}
    {% if forloop.first == false %}
    <div class="report-item">
      <a href="{{ report.url | relative_url }}">
        <span class="report-date">{{ report.date | date: "%Y-%m-%d" }}</span> - 
        <span class="report-title">{{ report.title }}</span>
      </a>
    </div>
    {% endif %}
  {% endfor %}
{% else %}
  <p>Previous reports will appear here as they are generated.</p>
{% endif %}

{% if reports.size > 1 or all_reports.size > 1 %}
[View All Reports]({{ '/archive' | relative_url }})
{% endif %}