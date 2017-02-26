---
title: Gaming
layout: page
index: 4
---

Gaming is always a fun hobby of mine. I do not consider myself a hard-core gamer, but I have a lot of appretiation for games as a way of art. 

## [Game Collection](gamecollection/)

In order to focus and complete the games I start, this page will keep will be my reminder to focus on one game at a time. There is not a real start date for this date, it is just a list that starts roughtly when I started collecting games.

## Current game queue

{% for game in site.data.gamequeue %}
{% if forloop.first == true %}
 * {{ game }}
{% else %}
 * ~~{{ game }}~~       
{% endif %}
{% endfor %}
