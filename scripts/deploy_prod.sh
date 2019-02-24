#!/bin/bash
# This script will create the site in a temporary folder and once the
# creation process is completed, move the site to the _site folder. 
# The instructions to set Jekyll are located at: https://help.github.com/articles/using-jekyll-with-pages

cd _wiki
mkdocs build
cd ..

bundle exec jekyll clean --dest tmp_site
bundle exec jekyll build --trace --dest tmp_site
rm -rf _site
mv tmp_site _site
