#!/usr/bin/env python3

# This script will read all the buffer posts across all services and 
# merge them. The result will be a queue of posts sorted by creation
# time. Each post also contains metadate linking it to the specific 
# post of each one of the services it was posted to.

import hashlib
import json

import constants

fileHandler = open(constants.BUFFER_DATA)
data = json.load(fileHandler)

# This dictionary will use a key based on the data of the post. By doing this we can group 
# posts that share similar characteristics.
buffDict = {}

for service in data['services']:
    # The 'updates' property has two properties "total" and "update_list"
    for update in service['updates']['update_list']:
        if service["service"] == "twitter" and update["type"] == "link":
            textToTrim = update["text_formatted"]
            textToTrim = textToTrim[:textToTrim.find('<')]
        else:
            textToTrim = update['text']
        # Now grab the first 140 characters
        textToTrim = str(textToTrim)[:140]

        # For facebook posts, the an entire blog post can be embedded in the text. If there is any new line, 
        # also cut the text there and then trim any white spaces and tabs.
        newLineIndex = textToTrim.find('\n')
        if newLineIndex != -1:
            textToTrim = textToTrim[0:newLineIndex]
        trimmedText = textToTrim.strip(' \t\n\r')
        keyText = str(update['text'])[:140] + "-" + update['day']

        # Lets consume extra cicles and hash the key
        key = hashlib.md5(keyText.encode('utf-8')).hexdigest()

        # If the key does not exist, create an object that contains the creation date and the update with it's properties.
        # When the key exists just update this values
        if not key in buffDict:
            buffDict[key] = {"created_at": 0, "services": [], "text": "", "key": key}
        updateObject = buffDict[key]
        updateObject["created_at"] = update["created_at"]
        local_service = {"name": service['service']}
        if "service_link" in update:
            local_service["service_link"] = update["service_link"]
        updateObject["services"].append(local_service)
        updateObject["title"] = trimmedText
        if update["text_formatted"]:
            newText = update["text_formatted"]
        else:
            newText = trimmedText#(trimmedText + "...") if shouldUseEllipsis else trimmedText
        #if service["service"] == "facebook" or service["service"] == "google":
        #    if "media" in update and "link" in update["media"]:
        #1        newText = newText + " " + update["media"]["link"]

        if len(newText) > len(updateObject["text"]):
            updateObject["text"] = newText
        if "media" in update:
            updateObject["media_" + service["service"]] = update["media"]
        buffDict[key] = updateObject

# Now extract the list of updates from the dictionary. This list is unsorted so let's sort if by creation time
unsortedList = list(buffDict.values())
sortedList = sorted(unsortedList, key=lambda update: update['created_at'])

fileHandler = open(constants.POST_QUEUE, 'w')
# Pretty print the list of updates
output = json.dumps(sortedList, indent=4, ensure_ascii=False).encode('ascii', 'ignore').decode('ascii', 'ignore')
fileHandler.write(output)
print("Data was written to file " + constants.POST_QUEUE)
