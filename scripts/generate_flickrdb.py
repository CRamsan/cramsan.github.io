#!/usr/bin/env python3

import flickrapi
import functools
import json

api_key = u'92ff58ce873ed2a3fea11dc8f746f0cf'
api_secret = u'bc4c31a72cc5a92d'
target_user = '149389453@N05'
OUTPUT_FILENAME = "_data/flickr.json"
OUTPUT_QUEUE_FILENAME = "_data/flickr_queue.json"
flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')

current_page = 1
last_page = 1
out_photo_dict = {}
while(current_page <= last_page):
    result = flickr.photos.search(user_id=target_user, per_page=10, page=current_page, extras="description,date_upload") # Get a page of the list of photos for this user
    last_page = result['photos']['pages']
    total = result['photos']['total']
    page = result['photos']['page']
    photo_list = result['photos']['photo']
    for photo in photo_list:
        # Use this information to generate the links
        photo_id = photo['id']
        photo_secret = photo['secret']
        photo_server = photo['server']
        photo_farm = photo['farm']
        photo['web_page_url'] = 'https://www.flickr.com/photos/' + target_user + '/' + photo_id
        photo['photo_source_url'] = 'https://c' + str(photo_farm) + '.staticflickr.com/' + str(photo_server) + '/' + str(photo_id) + '_' + str(photo_secret) + '_z.jpg'
        out_photo_dict[photo_id] = photo
    # Next page
    current_page += 1

current_page = 1
last_page = 1
out_photoset_dict = {}
while(current_page <= last_page):
    result = flickr.photosets_getList(user_id=target_user, per_page=10, page=current_page)
    last_page = result['photosets']['pages']
    total = result['photosets']['total']
    page = result['photosets']['page']
    photoset_list = result['photosets']['photoset']
    for photoset in photoset_list:
        photoset_id = photoset['id']
        print (photoset_id)
        # Use this information to generate the links
        out_photoset_dict[photoset_id] = photoset
    # Next page
    current_page += 1

fileHandler = open(OUTPUT_FILENAME, 'w')
# Pretty print the dictionary of pictures
flickr_data = {'photos' : out_photo_dict, 'photosets' : out_photoset_dict}
output = json.dumps(flickr_data, indent=4, ensure_ascii=False).encode('ascii', 'ignore').decode('ascii', 'ignore')
fileHandler.write(output)
print("Data was written to file " + OUTPUT_FILENAME)

photo_queue = []
photoset_queue = []
# Generate the queue file 
for key, value in sorted(out_photo_dict.items(), key=functools.cmp_to_key(lambda k,v: int(v[1]['dateupload']))):
  photo_queue.append(key)
for key, value in sorted(out_photoset_dict.items(), key=functools.cmp_to_key(lambda k,v: int(v[1]['date_create']))):
  photoset_queue.append(key)

fileHandler = open(OUTPUT_QUEUE_FILENAME, 'w')
# Pretty print the queue
flickr_data = {'photos' : photo_queue, 'photosets' : photoset_queue}
output = json.dumps(flickr_data, indent=4, ensure_ascii=False).encode('ascii', 'ignore').decode('ascii', 'ignore')
fileHandler.write(output)
print("Data was written to file " + OUTPUT_QUEUE_FILENAME)
