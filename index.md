---
layout: default
title: O'Neil Relative Strength Market Reports
---

{% assign reports = site.static_files | where_exp: "file", "file.path contains 'oneil_relative_strength_report_'" | sort: 'path' | reverse %}
{% assign latest_report = reports[0].path | split: '/' | last | split: '.' | first %}

<script>
window.onload = function() {
  // Redirect to the latest report
  window.location.href = "{{ site.baseurl }}/{{ latest_report }}";
}
</script>

<div class="loading-message">
  <h1>Redirecting to the latest market report...</h1>
  <p>If you are not redirected automatically, <a href="{{ site.baseurl }}/{{ latest_report }}">click here</a>.</p>
</div>

<style>
.loading-message {
  text-align: center;
  margin-top: 50px;
}
</style>