---
layout: post
title: Updating site and generating index
tags: jekyll
categories: other
---

I finally cleaned up this blog. I moved the "Game Collection" and "List of Applications" pages to collections in the "docs" folder. My plan was to have a location where I can drop documents and pages that do not change often but that also do not need to be located in the root level. To accomplish this I used Jekyll's collection which was both a blessing and a curse.

Jekyll's [Collections](https://jekyllrb.com/docs/collections/) are useful to hold documents that share a common characteristic, in a similar way as categories. But where they differ is that you will have more power and control over a collection, with the power to define properties and variables across all pages of the same collection. The problem for me was that I wanted my pages to have hierarchical structure as well as an index on the first page, two features that are not available natively.

The solution was to use a bash script(of course) to generate an json file that contained the structure of the collection and then this file could be exposed via site.data. The script is located [here](https://github.com/CRamsan/cramsan.github.io/blob/master/generate_index.sh) and it currently works based on how I wanted to present my collection, but the plan is for the future to make it more flexible.

The result is neat and I can have pages organized across folders of different depths. Currently I only have two pages but I tested multiple pages and depths and it was working correctly. As I develop this blog I am sure more pages will be added.

A picture of what my Pixel C looked like while I was working on finishing the changes.
{% include post_image.html image_id=site.data.flickr.photos.34033125200 %}
