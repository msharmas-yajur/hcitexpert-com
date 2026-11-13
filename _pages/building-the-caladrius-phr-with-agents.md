---
title: "Building the Caladrius PHR with agents"
permalink: /series/building-the-caladrius-phr-with-agents/
---

A day-by-day technical diary by Manish Sharma on building the Caladrius Health personal health record (PHR) with AI coding agents.

<ul>
{% assign series_posts = site.tags['building-the-caladrius-phr-with-agents'] | sort: 'day' %}
{% for p in series_posts %}
  <li><a href="{{ p.url | relative_url }}">{{ p.title | escape }}</a> <small>({{ p.date | date: "%B %-d, %Y" }})</small></li>
{% endfor %}
</ul>
