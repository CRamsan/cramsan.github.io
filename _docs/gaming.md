---
title: Gaming
layout: page
---

Gaming is always a fun hobby of mine. I do not consider myself a hard-core gamer, but I have a lot of appretiation for games as a way of art. 

---

# Currently looking for

{% assign category_list = site.data.game_lookout %}
{% for category in category_list %}
### {{ category.type }}
{% assign item_list = category.items %}
{% for item in item_list %}
  * {{ item }}
{% endfor %}
{% endfor %}

---

# Game collection

This is a list of games and consoles that me and my girlfriend own together. This collection is always changing but I will try to keep it as up to date as I can.

{% assign console_list = site.data.game_collection %}
{% for console in console_list %}
### {{ console.name }}
{% assign game_list = console.games %}
{% for game in game_list %}
  * {{ game }}
{% endfor %}
{% endfor %}

