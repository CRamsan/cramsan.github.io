# This script makes heavy use of local variables due to some unexpexted
# behaviours with variables being considered global. 

function listFiles() {
  local ORIGINAL_FOLDER=$(pwd)
  local TARGET_COLLECTION=$1
  local TARGET_DEPTH=$2
  local ROOT_FOLDER=$3
  local ROOT_LABEL=$4
  local FIRST_ITER=true;

  echo "{\"node\":\"$ROOT_LABEL\","
  cd $TARGET_COLLECTION
  echo "\"list\": ["
  find . -maxdepth 1 -name '*' | while read line; do
    if [ "$line" = "." ]; then
      continue
    fi
    if [ "$FIRST_ITER" = true ]; then
      local FIRST_ITER=false;
    else
      echo ","
    fi
    local FILE_PATH=$(dirname $line)
    local FILE_BASENAME=$(basename $line)
    local FILE_EXTENSION="${FILE_BASENAME##*.}"
    local FILE_FILENAME="${FILE_BASENAME%.*}"
    local FILE_TITLE="$(grep "title:" $line | sed 's/title: //g')"
    if [ -z "$FILE_TITLE" ]; then
      local FILE_TITLE="UNTITLED"
    fi
    if [ -f $line ]; then
      if [ ! -z $ROOT_FOLDER ]; then
        local LINK_URL="$ROOT_FOLDER/"
      else
	local LINK_URL=""
      fi
      local LINK_URL="$LINK_URL$FILE_FILENAME"
      echo "{\"level\": \"$TARGET_DEPTH\","
      echo "\"link\": \"$LINK_URL\","
      echo "\"name\": \"$FILE_TITLE\"}"
    else 
      if [ -d $line ]; then
       	local NEW_DEPTH=$((TARGET_DEPTH+1))
        if [ ! -z $ROOT_FOLDER ]; then
          local NEW_ROOT="$ROOT_FOLDER/$FILE_BASENAME"
        else
	  local NEW_ROOT="$FILE_BASENAME"
        fi
	listFiles $line $NEW_DEPTH $NEW_ROOT $FILE_BASENAME
      else
        echo "Found something that is not file or directory!"
        echo $line
      fi
    fi
  done
  echo "]}"
  cd $ORIGINAL_FOLDER
}
listFiles "_docs" 1 "" "docs" > _data/collection_docs.json

