#!/bin/bash

# This script will build the site in the _site folder and then serve it through
# the default url: http://127.0.0.1:4000
# The instructions to set Jekyll are located at: https://help.github.com/articles/using-jekyll-with-pages

cd _wiki
mkdocs build
cd ..
bundle exec jekyll serve
