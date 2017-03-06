---
title: Auraxis Control Center version 3 is out!
date: 2015-06-03 00:00:00 Z
tags: programming planetside 
categories: programming
layout: post
---

This post is two weeks too late but Auraxis Control Center just hit version 3 this last month. I decided to bump up the version number since this release included some major work such as namespaces, localization, new panels and better crash reporting. 

The upgrade was very smooth despite of the radical changes. I decided to spend two weeks for testing and it seemed that I caught all major cases(except for one crash that affected few people). The number of users went up again even without me advertising the new features, which means that there is still a healthy amount of people looking for PS2 apps. 

After the initial release I got couple crash reports, but the information I got from the Play Store was very limited and so I decided to reintroduce ACRA into the app. This time I took a different approach, instead of doing the lazy way of using email intents, I deployed a simple Google AppEngine app that stores logs. I used the ACRA functionality to POST crash logs in JSON format so I can simply post it to my own url. This ended up been much easier and better for the user since they do not need to do anything. The only thing that I lost is the ability for them to send messages, but I think that the fact that I can get crash logs in almost real-time makes up for that fact.

Apart from that I added Spanish as a language and now I am also adding German. Those will have to be the two languages I support unless I can get better translations for the strings I have. 

Overall I think this was a very successful update, and at a good time too since the PS4 launch of Planetside is getting near.
