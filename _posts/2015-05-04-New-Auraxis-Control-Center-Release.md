---
layout: post
title: New Auraxis Control Center Release
---

The last few months have been really slow for Auraxis Control Center. Most of the features that I wanted were there and I have not getting any bug reports, and with the jobs and Youtube projects I had to push coding down the priority list. But lots of changes were coming and I decided it was time to get back into action.

What is coming
--------------
With the change from Sony Online Entertainment to Day Break Game, their backend had to migrate from http://census.soe.com to http://census.daybreakgames.com and all the API calls had to be moved to new API endpoint. The API also added new namespaces for PS4 data, both EU and US data. Some other changes that were in the pipeline involve general improvements in some rough edges here and there(more on this can be found here: https://github.com/cesarramirez/auraxiscontrolcenter/issues)

Another aspect that was important for me to support was multiple languages. English is the dominant language in the Planetside 2 community but there is still a big number of other languages. The statistics showed that the most used languages are English, German, French, Spanish, Italian and Russian. The DBG census supports English, Spanish, German, Italian, French and Turkish so I am planning on at least supporting the first five for Auraxis Control Center. 

The problem
-----------

For adding this new features I needed to implement some changes to the code that would break some assumptions to how things were done before. Previously, the URL requests were made using my own API to generate URLS, but this could get complicated and sometimes I ended up just hard-coding the URL. Now with the new set of namespace I had to add some UI elements to let the user select the namespace to use. Some other changes had to go to the database schema so that the namespace would be saved for all profiles and outfits so they could be retrieved later too.

For adding support for multiple languages I had to clean some URLs that had the language hard-coded, as well as condense several Name classes into one. Some strings also needed to be externalized, which was not a big deal, but now I am in the process of getting all the right strings for all multiple languages. Currently I have a doc open to the public where people can contribute to get the strings translated.

https://docs.google.com/spreadsheets/d/1b7LR7bj9KdySq-tMiPhPAoFO96CtBinucIb5xHot_Jo/edit#gid=0

The outcome
-----------

I have tested the Spanish translation and all the strings seem to be ready and the Census API also provides the correct values. The namespace support is 99% ready, currently just in the process of doing the last tests. If things keep going well, I should release a new version in the middle of May.
