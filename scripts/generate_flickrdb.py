#!/usr/bin/env python3

import flickrapi
import functools
import json

import constants
import res.flickr_secret

# Initialize a FlickrAPI object as an unauthenticated user.
flickr = flickrapi.FlickrAPI(res.flickr_secret.API_KEY, res.flickr_secret.API_SECRET, format='parsed-json')

# List all photos. The result will be split in separate pages, 
# we need to iterate over ever page to get all the photos.
current_page = 1
last_page = 1
out_photo_dict = {}
print ("Generating photo dictionary")
while(current_page <= last_page):
    result = flickr.photos.search(user_id=constants.FLICKR_USER, per_page=10, page=current_page, extras="description,date_upload") # Get a page of the list of photos for this user
    last_page = result['photos']['pages']
    total = result['photos']['total']
    page = result['photos']['page']
    photo_list = result['photos']['photo']
    print ("Parsing page: " + str(current_page) + "/" + str(last_page))
    for photo in photo_list:
        # Use this information to generate the links
        photo_id = photo['id']
        photo_secret = photo['secret']
        photo_server = photo['server']
        photo_farm = photo['farm']
        photo['web_page_url'] = 'https://www.flickr.com/photos/' + constants.FLICKR_USER + '/' + photo_id
        photo['photo_source_url'] = 'https://c' + str(photo_farm) + '.staticflickr.com/' + str(photo_server) + '/' + str(photo_id) + '_' + str(photo_secret) + '_z.jpg'
        # Add this photo to the dictionary, using the photo id as the key.
        out_photo_dict[photo_id] = photo
    # Next page
    current_page += 1

current_page = 1
last_page = 1
out_photoset_dict = {}
# Now iterate over all the photosets or albums.
print ("Generating album dictionary")
while(current_page <= last_page):
    result = flickr.photosets_getList(user_id=constants.FLICKR_USER, per_page=10, page=current_page)
    last_page = result['photosets']['pages']
    total = result['photosets']['total']
    page = result['photosets']['page']
    photoset_list = result['photosets']['photoset']
    print ("Parsing page: " + str(current_page) + "/" + str(last_page))
    for photoset in photoset_list:
        photoset_id = photoset['id']
        # Use this information to generate the links
        out_photoset_dict[photoset_id] = photoset
    # Next page
    current_page += 1


fileHandler = open(constants.FLICKR_DICT, 'w')
# Pretty print the dictionary of pictures
flickr_data = {'photos' : out_photo_dict, 'photosets' : out_photoset_dict}
output = json.dumps(flickr_data, indent=4, ensure_ascii=False).encode('ascii', 'ignore').decode('ascii', 'ignore')
fileHandler.write(output)
print("Data was written to file " + constants.FLICKR_DICT)

photo_queue = []
photoset_queue = []
# Generate the queue file 
for key, value in sorted(out_photo_dict.items(), key=functools.cmp_to_key(lambda k,v: int(v[1]['dateupload']))):
  photo_queue.append(key)
for key, value in sorted(out_photoset_dict.items(), key=functools.cmp_to_key(lambda k,v: int(v[1]['date_create']))):
  photoset_queue.append(key)

fileHandler = open(constants.FLICKR_QUEUE, 'w')
# Pretty print the queue
flickr_data = {'photos' : photo_queue, 'photosets' : photoset_queue}
output = json.dumps(flickr_data, indent=4, ensure_ascii=False).encode('ascii', 'ignore').decode('ascii', 'ignore')
fileHandler.write(output)
print("Queue was written to file " + constants.FLICKR_QUEUE)
