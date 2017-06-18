import requests
import json
import sys

ACCESS_TOKEN="1/2dbfd2b0e37518a915aefed94eb8759c"

URL_GET_ROOT="https://api.bufferapp.com/1/"
URL_GET_USER="user.json"
URL_GET_PROFILES="profiles.json"
URL_GET_UPDATES_SEC1="profiles/"
URL_GET_UPDATES_SEC2="/updates/sent.json"
OUTPUT_FILENAME="_data/buffer.json"

PAGE_COUNT=55
UPDATE_FILTER="default"

def appendParam(key, value):
    return str(key) + "=" + str(value) + "&"

def appendAccessToken(url):
    return url + "?" +  appendParam("access_token", ACCESS_TOKEN)

def appendUpdatePage(url, page, count, filt):
    return url + appendParam("page", page) + appendParam("count", count) + appendParam("filter", filt)

def generateGetUserUrl():
    return appendAccessToken(URL_GET_ROOT + URL_GET_USER)

def generateGetProfilesUrl():
    return appendAccessToken(URL_GET_ROOT + URL_GET_PROFILES)

def generateGetUpdates(userId):
    return appendAccessToken(URL_GET_ROOT + URL_GET_UPDATES_SEC1 + str(userId) + URL_GET_UPDATES_SEC2)

def getJSONObjectFromUrl(url):
    response = requests.get(url)
    if response.status_code != 200:
        print ("URL: " + url)
        print ("http status: " + str(response.status_code))
        print ("response: " + str(response.text))
        return;
    else:
        print ("Valid response for " + url)
        return response.json()

user = getJSONObjectFromUrl(generateGetUserUrl())
if user is None:
    print("Failed to get USER object")
    sys.exit()
services = getJSONObjectFromUrl(generateGetProfilesUrl())
if services is None:
    print("Failed to get SERVICES")
    sys.exit()
for service in services:
    updateCount = -1
    pageIndex = 0
    updatesRefactor = {'updates': []}
    friendly_service_name = service['formatted_service'] +  "(" + service['formatted_username'] + ")"
    shouldRetry = False
    while True:
        targetURL = appendUpdatePage(generateGetUpdates(service['id']), pageIndex, PAGE_COUNT, UPDATE_FILTER)
        updatesResult = getJSONObjectFromUrl(targetURL)
        print ("Working with page " + str(pageIndex) + " from " + friendly_service_name)
        pageIndex = pageIndex + 1
        if updateCount is -1:
            updateCount = updatesResult['total']
            print ("Number of updates: " + friendly_service_name + " - " + str(updateCount))
        elif updateCount is not updatesResult['total']:
            print ("Number of updates for " + friendly_service_name + " changed while we were processing it")
        updatesRefactor['total'] = updateCount
        updatesRefactor['updates'].append(updatesResult['updates'])
        if ((pageIndex) * PAGE_COUNT) > updateCount:
            print ("Finished iterating for: " + friendly_service_name)
            break
    
    if shouldRetry:
        shouldRetry = False
        print("Retrying " + friendly_service_name)
        continue

    service['updates'] = updatesRefactor

user['services'] = services
fileHandler = open(OUTPUT_FILENAME, 'w')
output = json.dumps(user, indent=4, ensure_ascii=False).encode('ascii', 'ignore').decode('ascii', 'ignore')
fileHandler.write(output)
print("Data was written to file " + OUTPUT_FILENAME)
