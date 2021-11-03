---
title: Planetside 2 Killboard for Overwolf
date: 2014-04-17 00:00:00 Z
categories:
- gaming
- programming
tags:
- planetside
- javascript
- overwolf
layout: post
---

After being playing with Javascript, HTML and CSS for couple weeks, I decided it was time for me to give this technologies a chance. So I came up with this overlay for [Overwolf](https://www.overwolf.com/) that will give you live data as well as record you most epic moments.

As some of you know I am a very involved [Planetside 2](https://www.planetside2.com/home) player. I am working on the [Auraxis Control Center](https://play.google.com/store/apps/details?id=com.cesarandres.ps2link) and I always trying to see what can do to help the community. With my outfit([Derp Company](https://derpcompany.com/home/)) me and some members have tried to come up with some ideas of projects we can work on. 

One member, Beljoda, started working on a squad-lead assistant application for the [Overwolf](https://www.overwolf.com/) Overlay. He also developed a Javascript script that wrapped over the [Census API](https://census.soe.com/) and retrieved the information and populated the web page dynamically. At that point I had never worked with CSS or JS but I decided to keep digging, and by using his code I manage to come up with a nice page that gives real time data for a given user([Link](https://ndacm.org/~ramirezs/sla/Player_Dashboard.html)). But that page was mostly a prototype to see what data I could use as well as learning how to use the new c:join function.

But having a page that displays data straight from them API was nothing really new or special. So I decided to do something a bit more interesting and came to the idea of checking kills or deaths to trigger a screen shot. And this is the result:

{% include post_image.html image_id=site.data.flickr.photos.33105304383 %}

I have a key bind that I use to show or hide this panel, and I also added a link to go to a 'lite' mode of the panel. This will minimize the window but it will keep taking screen shots based on the settings.

{% include post_image.html image_id=site.data.flickr.photos.33788443741 %}

It is not Recursion Stat Tracker but it is a neat project, and I like keeping some records of my kills.

{% include post_album.html photoset=site.data.flickr.photosets.72157678987835494 %}

I have already submitted the application to the Overwolf team and it will be hopefully accepted in couple weeks.
