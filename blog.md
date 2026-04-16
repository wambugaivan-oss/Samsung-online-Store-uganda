---
layout: default
title: Blog
permalink: /blog/
---

# Samsung Store Uganda Blog

{% for post in site.posts %}
  ### [{{ post.title }}]({{ post.url }})
  *Published on {{ post.date | date_to_string }}*
  
  {{ post.excerpt }}
{% endfor %}
