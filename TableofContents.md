---
layout: page
title: 博文目录 Blog ToC
permalink: /tableofcontents/
---

<div>
  <p><i>鼠标悬停于标题链接上方，以预览博文摘要。<br>标题名右侧方括号中的是最后更新时间。</i></p>
</div>

<ul>
  {% for post in site.posts %}
    <li>
      {{ post.date | date: '%Y-%m-%d'}}
      <a href="{{ post.url }}" title="{{ post.excerpt | remove: '<p>' | remove: '</p>' }}">{{ post.title }}</a>
      {% if post.update %}
          [{{ post.update }}]
      {% endif %}
    </li>
  {% endfor %}
</ul>
