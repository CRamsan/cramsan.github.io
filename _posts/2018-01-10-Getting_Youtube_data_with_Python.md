---
layout: post
title: Getting Youtube data with Python
tags: programming youtube python
categories: programming
---

This is done with python 2 becuase most of the Youtube DATA libraries seem to support Python 2 better than 3. There may be versions of some of the libraries for Python 3 but I did not spend anytime investigating this route.

This link goes over most of the setup process pretty well:
https://developers.google.com/youtube/v3/getting-started

 1. Go to the developers console and create a new project
 https://console.developers.google.com/

 2. Now on the project page go to **Credentials** and create an **OAuth 2 Client ID** of type **Other**. Now download the json file which we will use to authenticate our app.

 3. To install the Youtube Data library you can use pip. I got the instructions from the Youtube api-samples [github page](https://github.com/youtube/api-samples/tree/master/python). As previously mentioned, we will use Python2.
```
pip install --upgrade google-api-python-client
```
 4. Now install other google libraries that will also be needed
```
pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2
```
 5. Now move the downloaded file and rename it to client_secrets.json, since that is what the script is expecting. I am using  [my_uploads.py](https://github.com/youtube/api-samples/blob/master/python/my_uploads.py) as a reference. If you run this script now you will be prompted to visit a URL and enter the resultingauthorization code.
```
cramsan@kururu ~/git/cramsan.github.io/scripts $ python2 demo.py 
Please visit this URL to authorize this application: https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=743336358314-o1grlivilob3pb4k3ra4b45kulgu20oa.apps.googleusercontent.com&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fyoutube.readonly&state=plvu3RkeSZL8Laj3wtz6IHsuvXBgY9&prompt=consent&access_type=offline
Enter the authorization code:
```
 6. This happens becuase the **OAuth2** credentials previously created requiere manual copy/paste. There are four types of [redirect methods](https://developers.google.com/youtube/v3/guides/auth/installed-apps) and in this case we are are using the **Manual copy/paste** mode.
Now you have everything you need to access the Youtube Data API. You can run the examples from the Youtube api-samples [github page](https://github.com/youtube/api-samples/tree/master/python) or the scrips from the repo of this blog.

Acessing the API is rather simple.

 - Create the YoutubeAPI object
{% highlight python %}
def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)
youtube = get_authenticated_service()
{% endhighlight %}
 - Now get the list of uploaded videos. This  function will return the Id of the playlist that represents the upload list of the authenticated channel
{% highlight python %}
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
{% endhighlight %}
 - Now that you have the Id of the uploads playlist, you can use it to iterate over every video
{% highlight python %}
def list_my_uploaded_videos(uploads_playlist_id):
  # Retrieve the list of videos uploaded to the authenticated user's channel.
  playlistitems_list_request = youtube.playlistItems().list(
    playlistId=uploads_playlist_id,
    part='snippet',
    maxResults=5
  )
  print 'Videos in list %s' % uploads_playlist_id
  while playlistitems_list_request:
    playlistitems_list_response = playlistitems_list_request.execute()
    # Print information about each video.
    for playlist_item in playlistitems_list_response['items']:
      title = playlist_item['snippet']['title']
      video_id = playlist_item['snippet']['resourceId']['videoId']
      print '%s (%s)' % (title, video_id)
    playlistitems_list_request = youtube.playlistItems().list_next(
      playlistitems_list_request, playlistitems_list_response)
{% endhighlight %}
