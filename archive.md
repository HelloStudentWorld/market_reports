---
layout: page
title: Report Archive
permalink: /archive/
---
<!--
<div class="site-nav" style="margin-bottom: 20px;">
  <a href="{{ site.baseurl }}/oneil_relative_strength_report_2025-04-10" class="nav-link">Latest Report</a>
</div>
-->

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
    
    {% assign reports_by_year = reports | group_by_exp: "file", "file.name | slice: -14, 4" %}
    
    {% for year in reports_by_year %}
      <h3>{{ year.name }}</h3>
      <ul class="report-list">
        {% for file in year.items %}
          {% assign date_string = file.name | slice: -14, 10 %}
          <li>
            <a href="{{ file.path | relative_url }}">
              <span class="report-date">{{ date_string }}</span> - 
              <span class="report-title">O'Neil Relative Strength Report</span>
            </a>
          </li>
        {% endfor %}
      </ul>
    {% endfor %}
  {% else %}
    <p>No archived reports found.</p>
  {% endif %}
</div>