---
title: Gaming
layout: page
index: 4
---

{% assign console_list = site.data.gamecollection %}
{% for console in console_list %}
# {{ console.name }}
{% assign game_list = console.games %}
{% for game in game_list %}
  * {{ game }}
{% endfor %}
{% endfor %}

