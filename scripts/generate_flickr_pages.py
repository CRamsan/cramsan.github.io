#!/usr/bin/env python3

import json
import shutil
import math
import os

FILENAME_QUEUE = '_data/flickr_queue.json'
FILENAME_DICT = '_data/flickr.json'
PER_PAGE = 30
OUTPUT_FOLDER = '_resources/Media/'

HEADER_STRING = """---
layout: page
title: Photos
---

"""

def generate_paginator(page, pages):
    result_string = '<div class="paginator"><span>'
    if page > 1:
        result_string += '<button onclick="cramsanHelper.goToUrl(\'{{ site.url }}/resources/Media/Photos/page' + str(page - 1) + '\')">Previous</button>'
    result_string += "Page: " + str(page) + "/" + str(pages)
    if page < pages:
        result_string += '<button onclick="cramsanHelper.goToUrl(\'{{ site.url}}/resources/Media/Photos/page' + str(page + 1) + '\')">Next</button>'
    result_string += '</span></div>'
    return result_string

def generate_liquid_string(photo_array, page, pages):
    array_string = ",".join(photo_array)
    result_string = "<div class=\"floatContentFix\">\n"
    result_string += "{% assign photo_queue = '" + array_string + "' | split: ',' %}\n"
    result_string += """{% for photo in photo_queue %}
  {% assign photo_data = site.data.flickr.photos[photo] %}
  {% include post_gallery.html image_id=photo_data %}
{% endfor %}
</div>
"""
    return HEADER_STRING + result_string + generate_paginator(page, pages)

def write_page_file(file_content, page):
    output_file = OUTPUT_FOLDER + "Photos.md"
    if page != 1:
        output_file = OUTPUT_FOLDER + "Photos/page" + str(page) + ".md"
   
    print ("Writting to file " + output_file)
    with open(output_file, 'w') as f:
        f.write(file_content)

photo_queue, photo_dict = None, None
with open(FILENAME_QUEUE, 'r') as f:
    photo_queue = json.load(f)

with open(FILENAME_DICT, 'r') as f:
    photo_dict = json.load(f)

photo_array = []
current_page = 1
pages = math.ceil(len(photo_queue['photos']) / PER_PAGE)
print ("Pages: " + str(pages))
for photo_enum in enumerate(photo_queue['photos']):
    page_break = photo_enum[0] % PER_PAGE == 0
    if photo_enum[0] != 0 and page_break:
        write_page_file(generate_liquid_string(photo_array, current_page, pages), current_page)
        current_page = current_page + 1
        photo_array = []

    photo_array.append(photo_enum[1])
write_page_file(generate_liquid_string(photo_array, current_page+1, pages), current_page)
