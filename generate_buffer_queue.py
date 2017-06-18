import json
import hashlib

INPUT_FILENAME = "_data/buffer.json"
OUTPUT_FILENAME = "_data/post_queue.json"

fileHandler = open(INPUT_FILENAME)
data = json.load(fileHandler)

# This dictionary will use a key based on the data of the post. By doing this we can group 
# posts that share similar characteristics.
buffDict = {}

for service in data['services']:
    # The 'updates' property has two properties "total" and "update_list"
    for update in service['updates']['update_list']:
        # For updates from instagram, facebook and google, their media is embedded in the "media" property.
        # But for twitter, any media is just an appended URL. It is usually at the end of the text but this
        # is not always the case. To address this disparity I am using this hack, it it not perfect but it 
        # should apply to most cases.
        # If the service is of 'type' twitter, then use the text from the beggining until the first '<'.
        # If the service if of other type, then just use the text from the first 140 characters.
        # This text is going to be used as part of the key to identity posts.
        if update['profile_service'] == "twitter" and update['type'] == "link":
            textToTrim = update['text_formatted'][:update['text_formatted'].find("<")]
        else:
            textToTrim = update['text']
        # Now grab the first 140 characters
        textToTrim = str(textToTrim)[:140]
        shouldUseEllipsis = len(textToTrim) > 140

        # For facebook posts, the an entire blog post can be embedded in the text. If there is any new line, 
        # also cut the text there and then trim any white spaces and tabs.
        newLineIndex = textToTrim.find('\n')
        if newLineIndex != -1:
            textToTrim = trimmedText[0:newLineIndex]
        trimmedText = textToTrim.strip(' \t\n\r')
        keyText = trimmedText + "-"  + update['day']

        # Lets consume extra cicles and hash the key
        key = hashlib.md5(keyText.encode('utf-8')).hexdigest()

        # If the key does not exist, create an object that contains the creation date and the update with it's properties.
        # When the key exists just update this values
        if not key in buffDict:
            buffDict[key] = {"created_at": 0, "services": []}
        updateObject = buffDict[key]
        updateObject["created_at"] = update["created_at"]
        updateObject["services"].append(service['service'])
        updateObject["text"] = trimmedText + "..." if shouldUseEllipsis else trimmedText
        
        buffDict[key] = updateObject

# Now extract the list of updates from the dictionary. This list is unsorted so let's sort if by creation time
unsortedList = list(buffDict.values())
sortedList = sorted(unsortedList, key=lambda update: update['created_at'])

fileHandler = open(OUTPUT_FILENAME, 'w')
# Pretty print the list of updates
output = json.dumps(sortedList, indent=4, ensure_ascii=False).encode('ascii', 'ignore').decode('ascii', 'ignore')
fileHandler.write(output)
print("Data was written to file " + OUTPUT_FILENAME)
