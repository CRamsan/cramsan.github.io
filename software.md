---
title: Software List
layout: page
index: 5
---

Gaming is always a fun hobby of mine. I do not consider myself a hard-core gamer, but I have a lot of appretiation for games as a way of art. 

---

# Game collection

This is a list of games and consoles that me and my girlfriend own together. This collection is always changing but I will try to keep it as up to date as I can.

{% assign category_list = site.data.software %}
{% for category in category_list %}
<h2>{{ category.name }}</h2>
{% assign software_list = category.list %}
{% for program in software_list %}
<li><span class="socialIconLabel">{{ program.name }}</span><span class="iconListGroup">{% for platform in program.plats %}{% case platform %}{% when 'W' %}<img src="/public/svg/icon/windows.svg" class="svgIcon"/>{% when 'L' %}<img src="/public/svg/icon/linux.svg" class="svgIcon">{% when 'M' %}<img src="/public/svg/icon/macos.svg" class="svgIcon">{% when 'A' %}<img src="/public/svg/icon/android.svg" class="svgIcon">{% endcase %}{% endfor %}</span></li>
<p class="programDescriptionP">{{ program.description | strip_html }}<p>
{% endfor %}
{% endfor %}

