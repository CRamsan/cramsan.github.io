#!/usr/bin/python

import argparse
import sys
import os
import re
import json

import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the {{ Google Cloud Console }} at
# {{ https://cloud.google.com/console }}.
CLIENT_SECRETS_FILE = 'client_secret.json'

# This OAuth 2.0 access scope allows for read-only access to the authenticated
# user's account, but not other types of account access.
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

# File names for output files
FILE_DICT = 'youtube.json'
FILE_ARRAY = 'youtube_queue.json'

# Authorize the request and store authorization credentials.
def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def get_my_uploads_list():
  # Retrieve the contentDetails part of the channel resource for the
  # authenticated user's channel.
  channels_response = youtube.channels().list(
    mine=True,
    part='contentDetails'
  ).execute()

  for channel in channels_response['items']:
    # From the API response, extract the playlist ID that identifies the list
    # of videos uploaded to the authenticated user's channel.
    return channel['contentDetails']['relatedPlaylists']['uploads']

  return None

def list_my_uploaded_videos(uploads_playlist_id):
  # Retrieve the list of videos uploaded to the authenticated user's channel.
  playlistitems_list_request = youtube.playlistItems().list(
    playlistId=uploads_playlist_id,
    part='snippet',
    maxResults=5
  )

  json_data = {}
  print 'Videos in list %s' % uploads_playlist_id
  while playlistitems_list_request:
    playlistitems_list_response = playlistitems_list_request.execute()

    # Print information about each video.
    for playlist_item in playlistitems_list_response['items']:
      title = playlist_item['snippet']['title']
      video_id = playlist_item['snippet']['resourceId']['videoId']
      # Add the video item to the dictionary 
      json_data[video_id] = playlist_item
      print '%s (%s)' % (title, video_id)
    playlistitems_list_request = youtube.playlistItems().list_next(
      playlistitems_list_request, playlistitems_list_response)
  return json_data
  
# Remove keyword arguments that are not set
def remove_empty_kwargs(**kwargs):
  good_kwargs = {}
  if kwargs is not None:
    for key, value in kwargs.iteritems():
      if value:
        good_kwargs[key] = value
  return good_kwargs

def playlists_list_mine(client, **kwargs):
  # See full sample for function
  kwargs = remove_empty_kwargs(**kwargs)

  response = client.playlists().list(
    **kwargs
  ).execute()

  json_data = {}
  # Print information about each video.
  for playlist_item in response['items']:
    title = playlist_item['snippet']['title']
    playlist_id = playlist_item['id']
    # Add the video item to the dictionary 
    json_data[playlist_id] = playlist_item
    print '%s (%s)' % (title, playlist_id)
  return json_data

if __name__ == '__main__':
  if len(sys.argv) < 4:
      print 'Arguments: python2 download_youtube.py \"DICT_FILENAME\" \"ARRAY_FILENAME\" \"CLIENT_SECRET\"'
      sys.exit()

  FILE_DICT = sys.argv[1]
  FILE_ARRAY = sys.argv[2]
  CLIENT_SECRETS_FILE = sys.argv[3]

  youtube = get_authenticated_service()
  try:
    video_data, playlist_data = None, None
    id_array = []
    uploads_playlist_id = get_my_uploads_list()
    if uploads_playlist_id:
      video_data = list_my_uploaded_videos(uploads_playlist_id)
    else:
      print('There is no uploaded videos playlist for this user.')
    
    playlist_data = playlists_list_mine(youtube,
        part='snippet,contentDetails',
        mine=True,
        onBehalfOfContentOwner='',
        onBehalfOfContentOwnerChannel='')

    # Iterate the dictionary and sort based on their date(position in the queue)
    for key, value in sorted(video_data.iteritems(), key=lambda (k,v): v['snippet']['position']):
      id_array.append(key)
    # Now save the video queue
    with open('youtube_queue.json', 'w') as outfile:
      json.dump(id_array, outfile)

    json_data = {'videos' : video_data, 'playlists' : playlist_data}
    # Now that we are done iterating the dictionary 
    # save the dictionary
    with open('youtube.json', 'w') as outfile:
      json.dump(json_data, outfile)

  except HttpError, e:
    print 'An HTTP error %d occurred:\n%s' % (e.resp.status, e.content)
