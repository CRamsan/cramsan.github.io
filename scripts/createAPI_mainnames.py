import json
import os

with open('index.json', 'r') as infile:
    data = json.load(infile)
    for element in data:
        elementId = element['plant_id']
        os.mkdir(str(elementId))
        with open(str(elementId) + '/index.json', 'w') as outfile:
            json.dump(element, outfile)
