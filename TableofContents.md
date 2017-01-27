---
layout: page
title: 博文目录
permalink: /tableofcontents/
---

<i>标题左侧是撰写时间，右侧方括号中的是最后更新时间。</i>

<ul>
  {% for post in site.posts %}
    <li>
      {{ post.date | date: '%Y-%m-%d'}}
      <a href="{{ post.url }}">{{ post.title }}</a>
      {% if post.update %}
          [{{ post.update }}]
      {% endif %}
    </li>
  {% endfor %}
</ul>
