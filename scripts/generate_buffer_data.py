#!/usr/bin/env python3

import requests
import datetime
import json
import math
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

def generateParam(key, value):
    return str(key) + "=" + str(value) + "&"

# This should be the first function called on the URL. It returns the url with the access token appended to the end of it
def appendAccessToken(url):
    return url + "?" +  generateParam("access_token", ACCESS_TOKEN)

# Return the url with the page, count and filter parameters appended to the end
def appendUpdatePage(url, page, count, filt, since):
    return url + generateParam("page", page) + generateParam("count", count) + generateParam("filter", filt) + generateParam("since", since)

# Returns the url to get the user info
def generateGetUserUrl():
    return appendAccessToken(URL_GET_ROOT + URL_GET_USER)

# Return the url to get the list of profiles of the current user
def generateGetProfilesUrl():
    return appendAccessToken(URL_GET_ROOT + URL_GET_PROFILES)

# Return the url to get the updates for a profile. This will not add any parameter to control the output
def generateGetUpdates(profileId):
    return appendAccessToken(URL_GET_ROOT + URL_GET_UPDATES_SEC1 + str(profileId) + URL_GET_UPDATES_SEC2)

# Wrapper to verify that an http request succeded with code 200. On success a json object will be returned, if the response if not in
# json format then an exception will be thrown. If the request returns a code other than 200, then None will be returned.
def getJSONObjectFromUrl(url):
    response = requests.get(url)
    if response.status_code != 200:
        print ("URL: " + url)
        print ("http status: " + str(response.status_code))
        print ("response: " + str(response.text))
        return None;
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

nowTime = datetime.datetime.now()
agoTimestamp = (nowTime - datetime.timedelta(days=14)).strftime("%s")

for service in services:
    updateCount = -1 # total number of updates
    pageCount = -1 # number of pages to iterate over
    pageIndex = 1 # current page index
    updatesRefactor = {'update_list': []} # This object will have all the updates for a profile/service.
    friendly_service_name = service['formatted_service'] +  "(" + service['formatted_username'] + ")"
    shouldRetry = False
    while True:
        targetURL = appendUpdatePage(generateGetUpdates(service['id']), pageIndex, PAGE_COUNT, UPDATE_FILTER, agoTimestamp)
        updatesResult = getJSONObjectFromUrl(targetURL) # Get a page of updates
        print ("Working with page " + str(pageIndex) + " from " + friendly_service_name)
        pageIndex = pageIndex + 1
        if updateCount is -1:
            # First iteration, set the updateCount and pageCount values
            updateCount = updatesResult['total']
            pageCount = math.ceil(updateCount / PAGE_COUNT)
            updatesRefactor['total'] = updateCount
            print ("Number of updates: " + friendly_service_name + " - count: " + str(updateCount) + " - pages: " + str(pageCount))
        elif updateCount is not updatesResult['total']:
            # The number of posts changed while we were iterating over the pages
            # Lets break out of the loop and retry this whole service/profile again
            print ("Number of updates for " + friendly_service_name + " changed while we were processing it")
            shouldRetry = True
            break
        # Add the updates from this page to updatesRefactor
        updatesRefactor['update_list'].extend(updatesResult['updates'])
        if pageIndex > pageCount:
            print ("Finished iterating for: " + friendly_service_name)
            break
    
    if shouldRetry:
        shouldRetry = False
        print("Retrying " + friendly_service_name)
        continue

    # Set the updatesRefactor as a child of the service
    service['updates'] = updatesRefactor

# Set the services list as a child of the user
user['services'] = services

# Write the resulting object to a file
fileHandler = open(OUTPUT_FILENAME, 'w')
# We need to encode->decode to remove unicode characters
output = json.dumps(user, indent=4, ensure_ascii=False).encode('ascii', 'ignore').decode('ascii', 'ignore')
fileHandler.write(output)
print("Data was written to file " + OUTPUT_FILENAME)
