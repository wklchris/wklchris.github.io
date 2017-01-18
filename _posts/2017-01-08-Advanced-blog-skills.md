---
layout: post
title: 怎样用 Github Pages 建立博客（2. 进阶）
category: Jekyll
tag: create-blog
---

本文是上一篇搭建 Jekyll 博客的进阶内容，包括：代码高亮、网站图标、数学公式、相关文章链接列表。

## 自定义 scss 

注意，在 assets/main.scss 的修改，优先级是高于 \_sass/minima/minima.scss 的。只要前者存在，后者形同虚设。本博客更改了 brand-color（超链接颜色）以及 content-width（页面文字宽）两个变量，其他并未修改。

## 插入代码和高亮

### 普通代码
插入普通代码很简单，行首缩进四个空格就可以了。如果你使用带有高亮功能的编辑器，此时插入的代码如果是 HTML，缩进到高亮消失即可。更通常地，如果你想要 Jekyll 提供更好的高亮效果，使用连续3个重音符（\`）并指明语言的环境来完成高亮。下面用尖号代替重音符作示意：

```python
^^^python
a = 2 ** 3
print(a)
^^^
```

### 带 Jekyll 语法的 HTML 代码
本来 Markdown 用来插入 HTML 代码是没有问题的，但是 Jekyll 语法内容直接在文中的任何地方都会被转换，所以也只能借助 Jekyll 语法来解决这一问题。比如，原本的变量：

    {% raw %}{{ post.date }}{% endraw %}

实质上在其左侧插入了`{ % raw % }`，在其右侧插入了`{ % endraw % }`。**注意，使用时花括号与百分号之间无空格。**如果你有大段代码需要应用，只需要把它们分别加到整个块的两端即可。

## 添加网站图标

一个好的网站怎么能没有图标呢？一个32$\times$32的 favicon.ico 文件能够解决你的烦恼。把它丢到根目录下，并在 default.html 中加上：

    <link rel="shortcut icon" type="image/x-icon" href="{% raw %}{{ site.url }}{% endraw %}/favicon.ico">

如果以上不成功，请使用 png 格式，或者尝试省略 site.url 变量。形如：

    <link rel="shortcut icon" type="image/png" href="/favicon.png">

p.s. 本站的图标来自 Noun Project 的[这个页面](https://thenounproject.com/term/open-book/793832/)，未去水印，只是重做为 ico 图标。在此对作者 ProSymbols 表示感谢。

## MathJax：数学公式支持

在 MathJax 的网页中，[这个页面](http://docs.mathjax.org/en/latest/start.html#tex-and-latex-input)给出了添加公式支持的方式。具体操作是打开 default.html 在其 `<head>` 代码段（可能是以 {% raw %}`{% include head.html %}`{% endraw %} 的形式存在的，那就添加到 head.html 里）添加：

```html
<script type="text/x-mathjax-config">
    MathJax.Hub.Config({
    tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
    });
</script>

<script type="text/javascript" async
    src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
```

讽刺的是，MathJax 指出以上 script 最好不要写到 `<body>` 中，尽管它可以运行。但是我写到 `<head>` 中是无法运行的，只有写到 default.html 下的`<body>`中才可以。

以上的 script 第一部分实质是把一对美元符号（`$...$`）也添加成为行内公式的输出方式；原本支持的只有`\(...\)`的行内形式。带来的副作用是如果使用它作为货币单位，你需要在其左侧额外添加一个反斜杠（`\`）。行间公式还是熟悉的`$$ ... $$`。

例子：

    $$ \int_0^{\pi} \sin x \,\mathrm{d}x = -\cos x \,\bigg| ^{\pi}_{0} = 2 $$

$$ \int_0^{\pi} \sin x \,\mathrm{d}x = -\cos x \,\bigg| ^{\pi}_{0} = 2 $$

    行内公式 $\sum_{i=0}^n a_i = 1$ 与前后字大小一致。

行内公式 $\sum_{i=0}^n a_i = 1$ 与前后字大小一致。

## JS：添加“返回顶部”功能

很常用的一个功能，用 JavaScript 实现：

```html
<a href="javascript:scroll(0,0)">-- 返回顶部 --</a>
```

## JS：添加文章目录与侧边栏

这里需要用到 JavaScript. 从我的 [js 仓库](https://github.com/wklchris/wklchris.github.io/tree/master/js)可以下载到需要的 toc.js 文件。此文件出处在[这里](https://github.com/ghiculescu/jekyll-table-of-contents)。

侧边栏这里使用 `<aside>` 标签进行处理。找到 assets/main.scss，并把以下内容放在 `@import "minima";` 的下方：

```css
@media screen and (min-width:1024px) {
	.wrapper{
		margin-right: 30%; // 文字右侧到页边30%
	}

	aside{
		position:fixed;
		left:75%;  // 侧边栏宽25%
		top:0;
		right:0;
		height:100%;
		overflow:hidden;
        background-color:#eeeeee;
		padding:2em 3em;
		box-shadow:5px 0 5px rgba(0,0,0,.1) inset;
	}
}

@media screen and (max-width: 1023px) {
	aside{
		padding: 1em;
	}
}
```

上面指明的 left 75% 表示侧边栏宽度是靠右的 25%.

然后在 post.html 文件中，post-content 这个 `<div>` 标签的上方，添加以下内容。当然，jquery支持的那部分（jquery-1.7.2.min.js）可以直接从其网站上引用，我是直接下载到文件夹中了。

```html
  <aside>
    <h2>本文目录</h2><p><a href="javascript:scroll(0,0)">-- 返回顶部 --</a></p>
    <script src="/js/jquery-1.7.2.min.js"></script>
    <script type="text/javascript" src="/js/toc.js"></script>
    <div id="toc"></div>
    <script type="text/javascript">
      $(document).ready(function() {
      $('#toc').toc();
    });
    </script>
  </aside>
```

以上这段也可以写成 sidebar-toc.html ，放在 \_includes 下，然后在 post.html 中换成：

```html
{% raw %}{% include sidebar-toc.html %}{% endraw %}
```

此外，非博文页我另做了一份 sidebar.html，真是麻烦。侧边栏还是略显空荡，以后再更新吧。

## 添加相关文章栏目

利用 Jekyll 自带的 site.tags 变量，将所有相关文章的文件头打上同一个 tag，就可以实现了。比如本文：

```
---
layout: post
title: 怎样用 Github Pages 来建立一个博客（进阶）
category: Jekyll
tag: 搭建博客
---
```
所有博客页面的 layout 类型都是 post，因此我们可以从 \_layouts/post.html 文件中下手：

```html
<div class="related-post">
  {% for eachtag in site.tags %}
    {% if page.tags.first != eachtag.first %}
      {% continue %}
    {% endif %}

    <h3 style="font-family: Microsoft YaHei">{{ eachtag.first }} 系列博文</h3>
    <ul class="arc-list">
    {% for post in eachtag.last %}
        <li>{{ post.date | date: '%Y-%m-%d'}} <a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
  {% endfor %}
</div>
```

其中，`site.tags` 是一个文章列表，里面的每个元素 eachtag 都是一个 tag 下辖的所有博文。其 first 成员则是 tag 名称。如果该名称与本页面所属 tag 一致（注：本站所有页面都只有一个 tag，用作相关文章列表），那么输出该 tag 下所有博文标题与链接。

然后在 \_sass/minima/\_layout.scss 中，添加：

    .related-post {
      background-color: lightgray;
      margin-bottom: 10pt;
    }

## Jekyll 官方文档

详细的教程请参考：  
- 全文英文站点：[链接](https://jekyllrb.com/docs/home/)  
- 部分中翻站点：[链接](http://jekyllcn.com/docs/home/)

相比 Jekyll 官方站点纷乱的内容，以下 Liquid 的 Designer 页面非常有参考价值：
- 仅英文：[链接](https://github.com/Shopify/liquid/wiki/Liquid-for-Designers)
