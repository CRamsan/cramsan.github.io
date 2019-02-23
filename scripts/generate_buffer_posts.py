#!/usr/bin/env python3

# This script will take the queue of buffer posts previously generated and it will
# generate the jekyll posts. If the file already exists, then a new file with the 
# sufix _resolve will be created. If the _resolvef file already exists then the 
# file will be overwritten.

import datetime
import hashlib
import json
import os
import sys

import constants

fileHandler = open(constants.POST_QUEUE)
data = json.load(fileHandler)

flickrHandler = open(constants.FLICKR_DICT)
flickrdb = json.load(flickrHandler)

# Create a dictionary using the photo hash as the key
urlMap = {}
for key, value in flickrdb['photos'].items():
    urlMapKey = value["description"]["_content"]
    urlMap[urlMapKey] = key

for post in data:
    timestamp = post['created_at']
    value = datetime.datetime.fromtimestamp(timestamp)
    dateString = value.strftime('%Y-%m-%d %H:%M:%S')
    fileDateString = value.strftime('%Y-%m-%d')
    titleFull = post["title"]
    title = post["title"][:40]
    sanitazedTitle = title.replace('/', '').replace('\\', '').replace('!', '').replace('<', '').replace('>','')
    for character in [' ', '&', '?', ':', '^']:
        sanitazedTitle = sanitazedTitle.replace(character, '_')
    filename = os.path.join(constants.POST_FOLDER, fileDateString + "-Buff_" + sanitazedTitle + "_.md")
    if os.path.exists(filename):
        if constants.POST_SAVE_DUPLICATES:
            filename = os.path.join(constants.POST_FOLDER, fileDateString + "-Buff_" + sanitazedTitle + "_resolve.md")
            print ("File already exists, saving as " + filename)
        else:
            print ("File " + filename + " already exists, skipping file")
            continue

    fileHandler = open(filename, 'w')
    fileHandler.write("---\nlayout: post\ncategories: social\ntags: buffer\nbuffer: true\n")
    fileHandler.write("title: \"" + titleFull + "\"\n")
    fileHandler.write("date: " + dateString + "\n")
    fileHandler.write("services: \n")
    for service in post['services']:
        fileHandler.write("  - name: " + service["name"] + "\n")
        if "service_link" in service:
            fileHandler.write("    link: " + service["service_link"] + "\n")
    fileHandler.write("---\n\n")
    fileHandler.write(post["text"] + "\n")
    if 'key' in post:
        postHash = post['key']
        if postHash in urlMap:
            imageId = urlMap[postHash]
            fileHandler.write("\n{% include post_image.html image_id=site.data.flickr.photos." + imageId + " %}\n")
    print("Data was written to file " + filename)
