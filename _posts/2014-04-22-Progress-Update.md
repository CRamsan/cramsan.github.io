---
title: Progress Update
tags: gaming programming API
categories: gaming programming
date: 2014-04-22 00:00:00 Z
layout: post
---

Auraxis Control Center
----------------------

Version 2.8.X was released! After several months of work, finally I was able to ship the tablet support as well as some general improvements under the hood. After the first day I noticed some minor bugs that were fixed on a ninja-fix with version 2.8.1. After the features were out I started and(after several nights of work) finished adding comments to most of the classes in the game. Now they are  easier to understand for newcomers. But I have also noticed a new set of crashes that are affecting a small number of users. With me moving and finishing college I have not have time to go back and fix the errors but is it top priority in the bug tracker. Currently I only have my laptop, which even though capable, it is still not a very good environment to work on. Hopefully I will have some time soon to fix this problems, no ETA though, I will also take it easy as I feel I need some vacations too :).


PS2 Killboard
-------------

The app was submitted and approved by the OW team but at the same time I noticed a critical bug that could completely crash the computer. Apparently when multiple kills happen at the exact same time, the Census API may return them in different order every time. If the events come in different order, the killboard will count that as a new events and it will trigger a screen capture. So in theory the API could return a different result on every call, and with that a new screenshot would be taken. Given that the killboards can make requests multiple times a second, that could fill up several gigabytes of data very quickly, eventually making the system to slow down due to all the IO requests. 

As I said earlier, I will not have time to work on this and due to the severity of the bug, I decided to ask the OW team to simply remove the app for now. Hopefully I will bring it back at some point.

PS2 Event Streaming
-------------------

And I saved the best for last. Now the Census API supports the use of websockets to push some data based on in-game events, more info [here]("https://census.soe.com/#ps2-websocket1"). Currently the events you can recieve are kills, vehicle kills, player login/logout, territory change and alerts. This opens the windows of possibilities to a completely new set of applications, seen as now we can receive data on demand instead of having to pull every single time. I have some great ideas, but I will talk about them in other time.
