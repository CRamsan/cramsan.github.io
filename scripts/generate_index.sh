#!/bin/bash
# This script makes heavy use of local variables due to some unexpeicted
# behaviours with variables being considered global. 

# Parameters:
# $1 The folder of the collection. 
# $2 Current depth. This is provided by the caller to determine the current depth. This is used to determine the root/'0' level
# $3 Root folder. The parent folder
# $4 Root label. The name to be used for the parent folder
function listFiles() {
  local ORIGINAL_FOLDER=$(pwd)
  local TARGET_COLLECTION="$1"
  local TARGET_DEPTH="$2"
  local ROOT_FOLDER="$3"
  local ROOT_LABEL="$4"
  local FIRST_ITER=true;

  # First we will check the data for the current folder or node. We will its properties and tthen we will check if there overrider. You can apply overrides to a node 
  # by creating an .md file that has the same name as the ROOT_LABEL. THis file can also contain a title, will be used as the name of this node.
  # The root label is the name for this page, it may not be necesarily the same as the name of the parent folder because we allow overriding the folder name
  # The level will be incremented by 1 before calling listFiles for a folder
  echo "{\"node\":\"$ROOT_LABEL\","
  echo "\"level\": \"$TARGET_DEPTH\","

  # Check if there is an .md file that has the same name as the 
  # label of the current folder. If there is, then there will be a link
  # to the current folder since there is content in this file
  local FOLDER_INDEX="$(basename "$ROOT_LABEL").md"
  if [ -f "$FOLDER_INDEX" ]; then
    echo "\"link\": \"$ROOT_LABEL\","
    # Now grep this file and extract the title. If there is a title, we will use that as the 
    # title of this node, otherwise fallback to using the ROOT_LABEL
    local FOLDER_TITLE="$(grep "title:" "$FOLDER_INDEX" | sed 's/title: //g')"
    if [ -z "$FOLDER_TITLE" ]; then
      local FOLDER_TITLE="$ROOT_LABEL"
    fi
    echo "\"name\": \"$FOLDER_TITLE\","
  fi

  # Now lets list each chilren of this node.
  cd "$TARGET_COLLECTION"
  echo "\"list\": ["
  find . -maxdepth 1 -name '*' -print | sort -f | while read line; do
    if [ "$line" = "." ]; then
      continue
    fi
    local FILE_PATH=$(dirname "$line")
    local FILE_BASENAME=$(basename "$line")
    local FILE_EXTENSION="${FILE_BASENAME##*.}"
    local FILE_FILENAME="${FILE_BASENAME%.*}"
    local NEW_DEPTH=$((TARGET_DEPTH+1))

    # If it is a file
    if [ -f "$line" ]; then
      
      # If there is a folder with the same name as this file, then ignore it.
      # This file will be processed when the folder is proccesd for overrides
      if [ -d "$FILE_FILENAME" ]; then
	# Now we allow the no_index file to prevent traversing folders. If this file is present then it is 
	# as if this directory did not exist. So even if there is a matching folder, if this file exists then 
	# we can continue traversing this folder
        if [ ! -f "$FILE_FILENAME/no_index" ];then
          continue
        fi
      fi
    
      if [ "$FIRST_ITER" = false ]; then
        echo ","
      fi
 
      # If the page has a title, extract it
      local FILE_TITLE="$(grep "title:" "$line" | sed 's/title: //g')"
      if [ -z "$FILE_TITLE" ]; then
        local FILE_TITLE="UNTITLED"
      fi

      # If the root folder is provided, append it to the LINK_URL. That will allow us to create the right URL as
      # we keep traversing the tree
      if [ ! -z "$ROOT_FOLDER" ]; then
        local LINK_URL="$ROOT_FOLDER/"
      else
	local LINK_URL=""
      fi
      local LINK_URL="$LINK_URL$FILE_FILENAME"

      echo "{\"level\": \"$NEW_DEPTH\","
      echo "\"link\": \"$LINK_URL\","
      echo "\"name\": \"$FILE_TITLE\"}"
    else 
      # If the no_index file exists, ignore this folder.
      if [ -f "$FILE_BASENAME/no_index" ]; then
        continue
      fi
      if [ "$FIRST_ITER" = false ]; then
        echo ","
      fi
      if [ -d "$FILE_BASENAME" ]; then

	# We know we found a folder. If there is a ROOT_FOLDER, append it to the current folder name.
	# We will pass this as the NEW_ROOT 
        if [ ! -z "$ROOT_FOLDER" ]; then
          local NEW_ROOT="$ROOT_FOLDER/$FILE_BASENAME"
        else
	  local NEW_ROOT="$FILE_BASENAME"
        fi
	listFiles "$FILE_BASENAME" "$NEW_DEPTH" "$NEW_ROOT" "$FILE_BASENAME"
      fi
    fi
    if [ "$FIRST_ITER" = true ]; then
      local FIRST_ITER=false;
    fi
  done
  echo "]}"
  cd $ORIGINAL_FOLDER
}
listFiles "_resources" "0" "" "resources" > _data/collection_resources.json
