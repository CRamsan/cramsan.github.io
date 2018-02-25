#!/bin/bash
# This helper script automates all the process to generate posts from 
# buffer updates. 

# Use the flickr API and get an updated list of all photos.
# The result will be stored as a json dictionary
./scripts/generate_flickrdb.py

# Use the Buffer API and get the updates/posts from a the last X 
# number of days or weeks. The result will be a json dictionary that 
# contains all the information retrieved from the API.
./scripts/generate_buffer_data.py

# Read the Buffer json posts file and generate a queue by combining 
# the posts from all the multiple services. This script will output 
# json file containing an array of objects containing all the 
# required data to create a jekyll post.
./scripts/generate_buffer_queue.py

# This step is important. It will go over all the pictures associated with 
# each post and find the one with the highest resolution. This picture will 
# be uploaded to flickr.
./scripts/generate_flickr_content.py

# Update the flickr photos dictionary to include the newly uploaded pictures.
./scripts/generate_flickrdb.py

# Read the list of posts generated previously. For each post a new file will 
# be created. If a file with the same name already exists, then a file with
# the sufix _resolve will be created. If the _resolve file already exists, 
# then it will be overwritten. 
./scripts/generate_buffer_posts.py
