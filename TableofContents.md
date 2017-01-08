---
layout: page
title: 博文目录
permalink: /tableofcontents/
---

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>  <i>{{ post.date | date: '%Y-%m-%d'}}</i>
    </li>
  {% endfor %}
</ul>
