#!/bin/bash

# Generate a new post file with the current date 
# and the provided title. This helper script will
# also populate the front matter.

HELP_MESSAGE="generate_post.sh [POST TITLE]"

if [ $# -eq 0 ]; then
  echo $HELP_MESSAGE
  exit
fi

if [ -z "$1" ]; then
  echo "No argument supplied"  
  exit
fi

DATE=`date +%Y-%m-%d`
INPUT=$1
TITLE="${INPUT//[^a-zA-Z0-9]/_}"
NEW_FILE="_posts/$DATE-$TITLE.md"

echo "File $NEW_FILE will be created"

echo "---" > $NEW_FILE
echo "layout: post" >> $NEW_FILE
echo "title: $INPUT" >> $NEW_FILE
echo "tags: random" >> $NEW_FILE
echo "categories: other" >> $NEW_FILE
echo "---" >> $NEW_FILE
echo >> $NEW_FILE

vim $NEW_FILE
