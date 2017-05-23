function getThumbnailURL {
    echo $1 | cut -d "=" -f 2 | cut -d ']' -f 1
}

function getImageURL {
    echo $1 | cut -d "]" -f 3 | cut -d '[' -f 1
}

function getUniqueId {
    echo $1 | cut -d "=" -f 2 | cut -d ']' -f 1 | cut -d '/' -f 5
}

function processImage {
    echo "Generating Image data"
    THUMBNAILURL=$(getThumbnailURL "$1")
    IMAGEURL=$(getImageURL "$1")
    UNIQUEID=$(getUniqueId "$1")
    echo "GetThumbnailURL: $THUMBNAILURL"
    echo "GetImageURL: $IMAGEURL"
    echo "ID: $UNIQUEID"
    echo "Generated yaml data:"
    echo
    echo "$UNIQUEID:"
    echo "    original:$IMAGEURL"
    echo "    inline: $THUMBNAILURL"
    echo 
    echo "Include this in your page:"
    echo
    echo "{% include post_image.html image_id=site.data.image_repo.images.$UNIQUEID %}"
}

function processAlbum {
    echo TEST
}

HELP_MESSAGE="generate_media.sh [MEDIA_DATA]\nMEDIA_DATA depends on what you are trying to include. Currently this script supports:\nFlickr Image: Copy the BB code to share this image.\nFlickr Album: Copy the embed code for the album\n"

if [ $# -eq 0 ]; then
  printf "$HELP_MESSAGE"
  exit
fi

# Determine the data type of what we are going to parse
if [[  ${1:0:1} == "<" ]]; then 
    processAlbum $1
elif [[ ${1:0:1}  == "[" ]]; then 
    processImage $1
else 
    echo "Format not valid"
fi


