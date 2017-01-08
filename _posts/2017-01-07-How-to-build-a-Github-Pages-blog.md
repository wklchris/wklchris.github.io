---
layout: post
title: 怎样用 Github Pages 来建立一个博客
category: Jekyll
---

## 安装 Ruby 和 dev-kit

前往 [Ruby 站点](http://rubyinstaller.org/downloads/) 下载 Ruby，下载Ruby后，将页面下拉，下载符合版本要求的 Development Kit. 在本文的测试中，环境是 Windows 10 x64，Ruby 版本 2.3.3 x64，dev-kit 版本 DevKit-mingw64-64-4.7.2-20130224-1432-sfx. 

安装 Ruby；将 dev-kit 解压到指定目录即完成安装。

## 安装 Jekyll 和 Bundle
请确保电脑的 Internet 连接正常。转到 dev-kit 目录，空白处Shift+鼠标右键呼出运行cmd，输入：
```
ruby dk.rb init  
ruby dk.rb install  
gem install jekyll  
gem install bundle
```

下载和安装会自动进行。

## 初始化博客文件夹
切换到 *username*.github.io 仓库所在本地文件夹，进行普通的初始化。使用 bash 命令输入（以我的博客为例）：
```
git init
git remote add origin https://github.com/wklchris/wklchris.github.io.git
```

然后进行一系列的新建操作：

- \_includes 文件夹
- \_layouts 文件夹，内含default.html，留空。
- \_posts 文件夹
- \_site 文件夹
- \_config.yml 文件，内容：  

```
title: wklchris 的博客 - wklchris' blog
author: wklchris
email: wklchris AT hotmail DOT com
description: > # this means to ignore newlines until "baseurl:"
  [页面右下角文字]
baseurl: ""
twitter_username: wklchris
github_username:  wklchris

defaults:
  -
    scope:
      path: "posts" # 空字符串所有的文件。这里指posts文件夹
    values:
      layout: "default"
      theme: minima
      permalink: date  # 这是指博客文章的网址格式

# Build settings
markdown: kramdown
theme: minima
exclude:
  - Gemfile
  - Gemfile.lock
```

- index.html 文件：

```
layout: home
```

- gemfile 文件，内容（墙内可能需要改成 http://ruby.taobao.org/ ）。其中第二行是我使用的主题，参考[此页面](https://pages.github.com/themes/)。

```
source "https://rubygems.org"

gem "minima"
```

关于 Github 仓库，你还可能需要的文件有：

- .gitignore 文件：屏蔽 _site 和 .sass-cache 文件夹。
- readme.md 文件

## 写博文

在 posts 文件夹内新建一个 Markdown 文件，文件名形如：

    1900-01-20-this-is-the-title.md

然后用 Markdown 进行书写即可。注意要加上文件头：

```
---
layout: post
title: 怎样用 Github Pages 来建立一个博客
---
```

如果在文件头中不更改 parmalink 属性，那么该博文发布后的网址将是：

    username.github.io/1900/01/20/this-is-the-title.html

## 发布前的测试

仍然是仓库文件夹，在cmd命令下输入：
```
bundle install
bundle exec jekyll serve
```

如果后续对 \_config.yml 文件进行了修改，就需要执行第一行；否则只用执行第二行即可。

此时服务器会运行，你可以通过访问[http://127.0.0.1:4000](http://127.0.0.1:4000)预览你的博客页面。