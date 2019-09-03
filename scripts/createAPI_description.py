import json
import os

mappedElements = {}
with open('index.json', 'r') as infile:
    data = json.load(infile)
    for element in data:
        elementId = element['plant_id']
        key = str(elementId)
	if (key not in mappedElements):
          mappedElements[key] = {}
        animalId = str(element['animal_id'])
        mappedElements[key][animalId] = element

for key in mappedElements:
    os.mkdir(key)
    for animalId in mappedElements[key]:
        os.mkdir(key + "/" + animalId)
        with open(key + "/" + animalId + '/index.json', 'w') as outfile:
            json.dump(mappedElements[key][animalId], outfile)
