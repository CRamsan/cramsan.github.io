#!/bin/bash
# The instructions to set Jekyll are located at: https://help.github.com/articles/using-jekyll-with-pages
# To run the server:
python generate_flickrdb.py > _data/flickr.json
./generate_index.sh
bundle exec jekyll clean --dest tmp_site
bundle exec jekyll build --trace --dest tmp_site
rm -rf _site
mv tmp_site _site
