---
layout: page
title: Photos
---

<script>
window.addEventListener('load', function(){
    var allimages= document.getElementsByTagName('img');
    for (var i=0; i<allimages.length; i++) {
        if (allimages[i].getAttribute('data-src')) {
            allimages[i].setAttribute('src', allimages[i].getAttribute('data-src'));
        }
    }
}, false)
</script>

{% assign photo_queue = site.data.flickr_queue.photos %}
{% for photo in photo_queue %}
  {% assign photo_data = site.data.flickr.photos[photo] %}
  {% include post_gallery.html image_id=photo_data %}
{% endfor %}
