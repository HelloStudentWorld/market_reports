---
layout: page
title: Report Archive
permalink: /archive/
---

# Report Archive

Browse all past market reports organized by date.

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