#!/bin/bash
# This script will work in the _site/debug folder so we do can run both the
# production and debug version of the site.
# The instructions to set Jekyll are located at: https://help.github.com/articles/using-jekyll-with-pages

# Generate the index of collections in the docs folder
./scripts/generate_index.sh

# Now clear and build the site with --trace for debugging purposes
bundle exec jekyll clean --destination _site/debug/
bundle exec jekyll build --destination _site/debug/ --trace
