---
title: This has been a slow year
date: 2016-05-19 00:00:00 Z
categories:
- programming
tags:
- iot
- wemo
- raspberrypi
layout: post
---

This is a reminder for myself that I should stop 'investing' into increasing my productivity. I am at a point in which if I were to actually work on something I would get it done much sooner than if I were to work on achieving 120% productivity.

----

A few weeks I uploaded a new repo which I am calling [Sensor Station](https://github.com/CRamsan/sensor_station). Basically the idea is to have a low powered device gathering data from other low powered devices and providing a way to access that data. The current implementation is two python daemons running on a raspberry pi, although it can run on anything really. One of the daemons is constantly listening and checking the status of WeMos in the network and saving the information locally to a SQLite databse. The second daemon is exposing the information in the database via a JSON endpoint or a HTML page. The data is gathered every minute and then you can see a breakdown of usage per WeMo.

There are still a few bugs to fix before I can post it somewhere, specially dealing with network errors but the project was short and fun. 
