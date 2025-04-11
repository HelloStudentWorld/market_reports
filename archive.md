---
layout: page
title: Report Archive
permalink: /archive/
---

# Report Archive

Browse all past market reports organized by date.

<!-- Regular reports from _reports collection if exists -->
<div class="archive-list">
  {% assign reports_by_year = site.reports | group_by_exp: "report", "report.date | date: '%Y'" %}
  {% for year in reports_by_year %}
    <h2>{{ year.name }}</h2>
    {% assign reports_by_month = year.items | group_by_exp: "report", "report.date | date: '%B'" %}
    {% for month in reports_by_month %}
      <h3>{{ month.name }}</h3>
      <ul class="report-list">
      {% for report in month.items %}
        <li>
          <a href="{{ report.url | relative_url }}">
            <span class="report-date">{{ report.date | date: "%Y-%m-%d" }}</span> - 
            <span class="report-title">{{ report.title }}</span>
          </a>
        </li>
      {% endfor %}
      </ul>
    {% endfor %}
  {% endfor %}
</div>

<!-- Archived reports from archived_reports directory -->
<div class="archive-list">
  <h2>Archived Reports</h2>
  
  {% assign archived_files = site.static_files | where_exp: "file", "file.path contains '/archived_reports/'" | where_exp: "file", "file.path contains '.md'" %}
  
  {% if archived_files.size > 0 %}
    {% assign reports = "" | split: "" %}
    {% for file in archived_files %}
      {% assign filename = file.path | split: '/' | last %}
      {% if filename contains "oneil_relative_strength_report" %}
        {% assign reports = reports | push: file %}
      {% endif %}
    {% endfor %}
    
    {% assign sorted_reports = reports | sort: "path" | reverse %}
    
    <ul class="report-list">
      {% for file in sorted_reports %}
        {% assign filename = file.path | split: '/' | last %}
        {% assign date_parts = filename | split: '_' %}
        {% assign date_string = date_parts | last | split: '.' | first %}
        <li>
          <a href="{{ file.path | relative_url }}">
            <span class="report-date">{{ date_string }}</span> - 
            <span class="report-title">O'Neil Relative Strength Report</span>
          </a>
        </li>
      {% endfor %}
    </ul>
  {% else %}
    <p>No archived reports found.</p>
  {% endif %}
</div>