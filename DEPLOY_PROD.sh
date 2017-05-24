#!/bin/bash
# The instructions to set Jekyll are located at: https://help.github.com/articles/using-jekyll-with-pages
# To run the server:
./generate_index.sh
bundle exec jekyll clean --dest tmp_site
bundle exec jekyll build --trace --dest tmp_site
rm -rf _site
mv tmp_site _site
