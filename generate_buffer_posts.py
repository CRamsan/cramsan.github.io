import json
import hashlib
import datetime
import os

INPUT_FILENAME = "_data/post_queue.json"
INPUT_FLICKRDB = "_data/flickr.json"
OUTPUT_FOLDER = "_posts/"

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
    titleFull = post["text"]
    title = titleFull[:40]
    sanitazedTitle = title.replace('/', '').replace('\\', '').replace(' ', '_')
    filename = os.path.join(OUTPUT_FOLDER, fileDateString + "-" + sanitazedTitle + ".md")
    if os.path.exists(filename):
        print ("File " + filename + " already exists and not going to overwrite.")
        continue
    fileHandler = open(filename, 'w')
    fileHandler.write("---\nlayout: post\ncategories: social\ntags: buffer\nbuffer: true\n")
    fileHandler.write("title: \"" + titleFull + "\"\n")
    fileHandler.write("date: " + dateString + "\n")
    fileHandler.write("services: \n")
    for service in post['services']:
        fileHandler.write("  - " + service + "\n")
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
