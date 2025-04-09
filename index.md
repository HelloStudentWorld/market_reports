---
layout: home
title: O'Neil Relative Strength Market Reports
---

# Daily Market Reports

Welcome to the O'Neil Relative Strength Market Reports page. These reports are automatically generated daily at 1:10pm Los Angeles time and provide comprehensive market analysis using William O'Neil's relative strength methodology.

## Latest Report

{% assign latest_report = site.reports | sort: 'date' | last %}

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

## Previous Reports

{% assign reports = site.reports | sort: 'date' | reverse %}
{% for report in reports limit:10 %}
  {% unless forloop.first %}
  <div class="report-item">
    <a href="{{ report.url | relative_url }}">
      <span class="report-date">{{ report.date | date: "%Y-%m-%d" }}</span> - 
      <span class="report-title">{{ report.title }}</span>
    </a>
  </div>
  {% endunless %}
{% endfor %}

[View All Reports]({{ '/archive' | relative_url }})