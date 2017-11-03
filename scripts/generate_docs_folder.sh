HELP_MESSAGE="generate_docs_folder.sh [PAGE TITLE]"

if [ $# -eq 0 ]; then
  echo $HELP_MESSAGE
  exit
fi

if [ -z "$1" ]; then
  echo "No argument supplied"  
  exit
fi

INPUT=$1
TITLE="${INPUT//[^a-zA-Z0-9]/_}"
NEW_FOLDER="$TITLE"
NEW_FILE="$NEW_FOLDER/$TITLE.md"


echo "New collection folder $NEW_FOLDER will be created."
echo "File $NEW_FILE will be created as the index.html of this folder."

mkdir "NEW_FOLDER"

echo "---" > $NEW_FILE
echo "layout: page" >> $NEW_FILE
echo "title: $INPUT" >> $NEW_FILE
echo "---" >> $NEW_FILE
echo >> $NEW_FILE
