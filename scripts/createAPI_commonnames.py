import json
import os

mappedElements = {}
with open('index.json', 'r') as infile:
    data = json.load(infile)
    for element in data:
        elementId = element['plant_id']
        key = str(elementId)
	if (key not in mappedElements):
          mappedElements[key] = []
        mappedElements[key].append(element)

for key in mappedElements:
    os.mkdir(key)
    with open(key + '/index.json', 'w') as outfile:
        json.dump(mappedElements[key], outfile)
