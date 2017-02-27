---
title: Gaming
layout: page
index: 4
---

Gaming is always a fun hobby of mine. I do not consider myself a hard-core gamer, but I have a lot of appretiation for games as a way of art. 

---

## Currently looking for

{% assign category_list = site.data.gamelookout %}
{% for category in category_list %}
### {{ category.type }}
{% assign item_list = category.items %}
{% for item in item_list %}
  * {{ item }}
{% endfor %}
{% endfor %}

---

In order to focus and complete the games I start, this page will keep will be my reminder to focus on one game at a time. There is not a real start date for this date, it is just a list that starts roughtly when I started collecting games.

## Current game queue

{% for game in site.data.gamequeue %}
{% if forloop.first == true %}
 * {{ game }}
{% else %}
 * ~~{{ game }}~~       
{% endif %}
{% endfor %}

---

## Game collection

This is a list of games and consoles that me and my girlfriend own together. This collection is always changing but I will try to keep it as up to date as I can.

{% assign console_list = site.data.gamecollection %}
{% for console in console_list %}
### {{ console.name }}
{% assign game_list = console.games %}
{% for game in game_list %}
  * {{ game }}
{% endfor %}
{% endfor %}

