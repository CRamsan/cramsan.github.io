---
layout: page
title: Projects
index: 1
---

{% assign projects_list = site.data.projects %}
{% for node in projects_list %}
  * [{{ node.name }}]({{ node.url }}): {{ node.description }}
{% endfor %}

