#!/usr/bin/env python3

# When a photos is posted to Buffer, a new photo is generated for each of the 
# services used. This script will download each photo and compare their 
# resolutions. The largest image will be uploaded to flickr.

import struct
import imghdr
import json
import hashlib
import os
import sys
import urllib.request
import tempfile
import flickrapi

INPUT_FILENAME = "_data/post_queue.json"
INPUT_FLICKRDB = "_data/flickr.json"

api_key = u'92ff58ce873ed2a3fea11dc8f746f0cf'
api_secret = u'bc4c31a72cc5a92d'
target_user = '149389453@N05'
flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
flickr.authenticate_via_browser(perms='delete')

def get_image_size(fname):
    '''Determine the image type of fhandle and return its size.
    from draco'''
    with open(fname, 'rb') as fhandle:
        head = fhandle.read(24)
        if len(head) != 24:
            return
        if imghdr.what(fname) == 'png':
            check = struct.unpack('>i', head[4:8])[0]
            if check != 0x0d0a1a0a:
                return
            width, height = struct.unpack('>ii', head[16:24])
        elif imghdr.what(fname) == 'gif':
            width, height = struct.unpack('<HH', head[6:10])
        elif imghdr.what(fname) == 'jpeg':
            try:
                fhandle.seek(0) # Read 0xff next
                size = 2
                ftype = 0
                while not 0xc0 <= ftype <= 0xcf:
                    fhandle.seek(size, 1)
                    byte = fhandle.read(1)
                    while ord(byte) == 0xff:
                        byte = fhandle.read(1)
                    ftype = ord(byte)
                    size = struct.unpack('>H', fhandle.read(2))[0] - 2
                # We are at a SOFn block
                fhandle.seek(1, 1)  # Skip `precision' byte.
                height, width = struct.unpack('>HH', fhandle.read(4))
            except Exception: #IGNORE:W0703
                return
        else:
            return
        return width, height

fileHandler = open(INPUT_FILENAME)
data = json.load(fileHandler)

flickrHandler = open(INPUT_FLICKRDB)
flickrdb = json.load(flickrHandler)

largestSize = (0,0)
imageSize = 0
imageUrl = ''

urlMap = set()
for key, value in flickrdb['photos'].items():
    urlMap.add(value['description']['_content'])

for post in data:
    for media in ["media_twitter", "media_facebook", "media_google", "media_instagram"]:
        if media in post:
            postMedia = post[media]
            if "picture" in postMedia:
                try:
                    fileUrl = postMedia["picture"]
                    local_filename, headers = urllib.request.urlretrieve(fileUrl)
                    new_dimensions = get_image_size(local_filename)
                    largest_dimensions = largestSize[0] * largestSize[1]
                    new_size = new_dimensions[0] * new_dimensions[1]
                    print ("Size(" + media + "): " + str(new_dimensions))
                    if new_size >= largest_dimensions:
                        largestSize = new_dimensions
                        imageurl = local_filename
                        imageSize = new_size
                except urllib.error.URLError as e:
                    print(e.reason)
    # Now we should know which photo will be uploaded. 
    # Lets upload it to flickr.
    title = post['title']
    description = post['key']
    if imageSize == 0:
        print ("Image was not found or size was 0.");
        continue
    if description in urlMap:
        print ("Image with title (" + title + ") and tag (" + description + ") was already uploaded");
        continue
    print ("Uploading file: " + imageUrl)
    print ("Size: " + str(largestSize))
    print ("Title: " + title)
    resp = flickr.upload(imageurl, is_public=1, title=title, description=description, format='rest')
