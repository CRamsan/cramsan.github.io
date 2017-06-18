import json
import hashlib
import datetime
import os

INPUT_FILENAME = "_data/post_queue.json"
OUTPUT_FOLDER = "_posts/"

fileHandler = open(INPUT_FILENAME)
data = json.load(fileHandler)

for post in data:
    timestamp = post['created_at']
    value = datetime.datetime.fromtimestamp(timestamp)
    dateString = value.strftime('%Y-%m-%d %H:%M:%S')
    fileDateString = value.strftime('%Y-%m-%d')
    title = post["text"][:40].replace(':','')
    sanitazedTitle = title.replace('/', '').replace('\\', '').replace(' ', '_')
    filename = os.path.join(OUTPUT_FOLDER, fileDateString + "-" + sanitazedTitle + ".md")
    fileHandler = open(filename, 'w')
    fileHandler.write("---\nlayout: post\ncategories: social\ntags: buffer\nbuffer: true\n")
    fileHandler.write("title: " + title + "\n")
    fileHandler.write("date: " + dateString + "\n")
    fileHandler.write("---\n")
    fileHandler.write(post["text"])
    print("Data was written to file " + filename)
