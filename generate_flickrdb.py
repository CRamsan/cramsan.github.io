import flickrapi
import json

api_key = u'92ff58ce873ed2a3fea11dc8f746f0cf'
api_secret = u'bc4c31a72cc5a92d'
target_user = '149389453@N05'
OUTPUT_FILENAME = "_data/flickr.json"
flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')

current_page = 1
last_page = 1
out_photo_dict = {}
while(current_page <= last_page):
    result = flickr.photos.search(user_id=target_user, per_page=10, page=current_page) # Get a page of the list of photos for this user
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

fileHandler = open(OUTPUT_FILENAME, 'w')
# Pretty print the list of pictures
output = json.dumps(out_photo_dict, indent=4, ensure_ascii=False).encode('ascii', 'ignore').decode('ascii', 'ignore')
fileHandler.write(output)
print("Data was written to file " + OUTPUT_FILENAME)
