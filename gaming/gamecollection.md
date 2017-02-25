---
title: Game Collection
layout: default
---

This is a list of games and consoles that me and my girlfriend own together. This collection is always changing but I will try to keep it as up to date as I can.

{% assign console_list = site.data.gamecollection %}
{% for console in console_list %}
# {{ console.name }}
{% assign game_list = console.games %}
{% for game in game_list %}
  * {{ game }}
{% endfor %}
{% endfor %}

