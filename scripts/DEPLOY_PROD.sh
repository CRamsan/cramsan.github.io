#!/bin/bash
# This script will create the site in a temporary folder and once the
# creation process is completed, move the site to the _site folder. 
# The collection index generation is not part of this script
# The instructions to set Jekyll are located at: https://help.github.com/articles/using-jekyll-with-pages

echo "The collection index is not being generated. Make sure generate_index.sh was already called."
sleep 5

# To run the server:
bundle exec jekyll clean --dest tmp_site
bundle exec jekyll build --trace --dest tmp_site
rm -rf _site
mv tmp_site _site
