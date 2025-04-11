---
layout: home
title: O'Neil Relative Strength Market Reports
---

{% assign reports = site.static_files | where_exp: "file", "file.path contains 'oneil_relative_strength_report_'" | sort: 'path' | reverse %}
{% assign latest_report = reports[0].path | split: '/' | last | split: '.' | first %}

<div class="home-content">
  <h1>Daily Market Strength Reports</h1>
  <p>Welcome to the Market Strength Reports dashboard. These reports provide automated market analysis using William O'Neil's relative strength methodology.</p>
  
  <div class="latest-report">
    <h2>Latest Report</h2>
    <a href="{{ site.baseurl }}/{{ latest_report }}" class="report-button">View Latest Report ({{ latest_report | split: '_' | last }})</a>
  </div>
  
  <div class="archive-link">
    <p>Looking for older reports? <a href="{{ site.baseurl }}/archive">Browse the Archive</a></p>
  </div>
</div>

<style>
.home-content {
  text-align: center;
  margin: 50px auto;
  max-width: 800px;
}
.latest-report {
  margin: 40px 0;
}
.report-button {
  display: inline-block;
  padding: 12px 24px;
  background-color: #0366d6;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  font-weight: bold;
  margin-top: 10px;
}
.report-button:hover {
  background-color: #0056b3;
}
</style>