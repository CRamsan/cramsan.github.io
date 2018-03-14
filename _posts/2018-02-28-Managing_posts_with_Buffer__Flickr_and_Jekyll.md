---
layout: post
title: Managing posts with Buffer, Flickr and Jekyll
tags: blog
categories: other
---

Having a blog that relies on static pages can be quiet cumbersome. This site currently runs on Jekyll, which means there is no database, no CMS, no image storage. For the most part, the site is just HTLM, CSS, JS, Markdown, Liquid and JSON files. This used to work fine when I would not post things for several months, but as I want to post more, it became clear that I needed to come up with a better sollution. What I will describe here is not a system developed to handle the limitation of Jekyll, but rather a evolving sytem that fits my needs of how I do things.

The initial plan of my blog was to host longer-form content, while social media would house regular updates and content such as photos and videos. Due to the lack of hosting space for photos and videos, I was not planning on including them into most of the posts. The process to include photos and videos into posts previously would be something like:
 1. Upload images to Imgur or videos to YouTube
 2. Get the embeddable HTLM
 3. Open the markdown file and include the HTLM code

Even though this process is not that horrible, there are a few things that would them a real pain for me in particular.
 1. I am usually working on my PixelC, so uploading images and videos is more cumbersome that uploading through a regular computer.
 2. Same as 1. I am on mobile, and getting the HTLM code is usually more complicated on these platforms.
 3. By preference, I try to keep markdown files clean of any HTLM. Otherwise changing CSS may require to update posts files as well.
 4. Some services require more than one single Id to generate embedable code, this is specially true with Flickr. This would make it more complicated to use something like includes to handle embedded images and videos.

Due to these complications, I had made the decision to focus on uploading photos and videos to social media while using Jekyll for mostly text. When required I would include media into jekyll posts, but this would be a manual proccess. 

### Enter Buffer

I don't mind posting to social media, but as time went on, I grew tired of posting to Facebook, Google+, Twitter, Instagram, LinkedIn, and the list goes on. For the most part each service does the same thing, post some text and maybe attach some images or links. Afterwards the users of each platform can interact by linking or sharing your content. Despite of this, there seems to be void of services that allow you to post to multiple services at once. On my research, Buffer was the only one that was able to post to multiple services, including Google+.

Additionally, Buffer has an API which allows us to access the list of updates(a.k.a. posts) along with all required metadata. This is a crucial part this blog because we can use it to integrate posts in Buffer within Jekyll. To do this I have `generate_buffer_data.py` to download all the buffer data from the last two weeks.

The next step is to merge all the posts from all the services from Buffer into a single queue. The script that does this is `generate_buffer_queue.py`, which will generate a hash using the post date and title. Then this hash can be used to identity the same post across all services. The result will be an array of posts that contains links to any media that was attached to the post.

### Using Flickr

After the last step, we will have an array of posts which may contain links to pictures. The next step will be to check if we need to update any shared photo to Flickr. First we will use `generate_flickrdb.py` to use the Flickr API to generate a dictionary of photos and albums. Now I use `generate_flickr_content.py` to iterate over each image attached to each posts. It will identity the highest resolution picture and then it will check if the picture is already uploaded. This is done by checking if there is already a picture that contains the post hash in the tag section. Now I need to run `generate_flickrdb.py` to generate an updated dictionary that contains the recently uploaded photos.

### Mixing Flickr, Buffer and Jekyll

At this point we have a dictionary of photos in Flickr that will have the post's hash value in the tag. We also have a queue of posts that contains all the data of a post, including the it's hash. The last script to run is `generate_buffer_posts.py` that will generate a markdown file that contains all the post information, at the end of the post there will be an include to the embedable version of the picture.

### YouTube
I dont usually upload to YouTube, but I also have `generate_youtubedb.py` to generate a json file with all my videos and playlists. If I want to embed a video or playlist, I can simply use an include with the id of the video.

### The results

After automating all these steps, I can post though Buffer to Google+, Facebook, Twitter and Instagram. Then a few times a week I can run a wrapper script to embed all the posts into the blog. This allows me to update my blog with my unfrequent social media posts. Even though I know it is not the best sollution, I really like how it works and the control I have over the entire process. I hope this was of help for you.

