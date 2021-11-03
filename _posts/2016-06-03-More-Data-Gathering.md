---
title: More Data Gathering
date: 2016-06-03 00:00:00 Z
categories:
- programming
tags:
- programming
- iot
- wemo
layout: post
---

This is the project that has been sucking my time lately, a lightweight hub for data that is collected in my home. The project started as a service to keep track of the energy consumption from two WeMos in my apartment. But When I was done I noticed that there is no reason why this wouldn't work for other kinds of data.

The application is divided on three parts, the server, the API and the modules. Let me explain what each part does.


The server
---------

This is a python script that uses the scheduler to trigger events to poll devices. The server will import all the modules in the 'modules' folder and then it will instantiate an object for each module enabled in the senson_station.cfg file. Each module imported has the logic to check if a device is online and 

The Modules(Tentative title)
----------------------------

I say tentative title because it is a bad idea to call something 'module' since it is such a common word.

To handle multiple types of sensors, each module is a self contained python class that provides information to the server about how often should the polling happen as well as the logic to do the polling itself. Other pieces of information in each module also include a database version and also the format of the data to be retrieved. 

The API
-------

And in order to get the information out of the database there are two endpoints, a JSON endpoint and a simple HTML page. The JSON endpoint allows other application to get the summarized data in JSON format. While the HTML page is just a front-end that formats the JSON data into some ugly HTML tables.

For some more information you can look into the README file from the repo at [sensor_station](https://github.com/CRamsan/sensor_station). 
