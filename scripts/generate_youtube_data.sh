#!/bin/bash

FILE_DICT="youtube.json"
FILE_ARRAY="youtube_queue.json"
CLIENT_SECRETS_FILE="scripts/client_secret.json"

python2 scripts/download_youtube.py $FILE_DICT $FILE_ARRAY $CLIENT_SECRETS_FILE
mv $FILE_DICT _data/
mv $FILE_ARRAY _data/
