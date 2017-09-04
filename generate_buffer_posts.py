import json
import hashlib
import datetime
import os
import sys

INPUT_FILENAME = "_data/post_queue.json"
INPUT_FLICKRDB = "_data/flickr.json"
OUTPUT_FOLDER = "_posts/"
SAVE_DUPLICATES = True

fileHandler = open(INPUT_FILENAME)
data = json.load(fileHandler)

flickrHandler = open(INPUT_FLICKRDB)
flickrdb = json.load(flickrHandler)

urlMap = {}
for key, value in flickrdb.items():
    urlMap[value["title"]] = key

for post in data:
    timestamp = post['created_at']
    value = datetime.datetime.fromtimestamp(timestamp)
    dateString = value.strftime('%Y-%m-%d %H:%M:%S')
    fileDateString = value.strftime('%Y-%m-%d')
    titleFull = post["title"]
    title = post["title"][:40]
    sanitazedTitle = title.replace('/', '', '!').replace('\\', '')
    for character in [' ', '&', '?', ':', '^']:
        sanitazedTitle = sanitazedTitle.replace(character, '_')
    filename = os.path.join(OUTPUT_FOLDER, fileDateString + "-Buff_" + sanitazedTitle + ".md")
    if os.path.exists(filename):
        if SAVE_DUPLICATES:
            filename = os.path.join(OUTPUT_FOLDER, fileDateString + "-Buff_" + sanitazedTitle + "_resolve.md")
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
        if service["name"] == "instagram":
            # Currently instagram posts do not have a media link and therefore we cannot link directly to the post
            continue
        fileHandler.write("  - name: " + service["name"] + "\n")
        if "service_link" in service:
            fileHandler.write("    link: " + service["service_link"] + "\n")
    fileHandler.write("---\n")
    fileHandler.write(post["text"] + "\n")
    for media in ["media_twitter", "media_facebook", "media_google", "media_instagram"]:
        if media in post:
            postMedia = post[media]
            if "picture" in postMedia:
                key = postMedia["picture"]
                if key in urlMap:
                    imageId = urlMap[key]
                    fileHandler.write("{% include post_image.html image_id=site.data.flickr." + imageId + " %}\n")
                    break;
    print("Data was written to file " + filename)
