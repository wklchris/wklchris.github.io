---
layout: post
title: R语言学习与速查（入门）
category: R
tag: R-learning
---


本系列文章可以作为一份快速的 R 上手指南，或者一份在线速查手册。操作系统基于 Windows。系列文章的参考资料在这里列出：

1. Kabacoff R I. *R 语言实战（第二版）*[M]. 人民邮电出版社, 2016.

## 入门

### 安装 R 与 RStudio

前往 [CRAN 站点](https://cran.r-project.org/)可以找到 R 的相关下载。安装好之后，建议安装 RStudio 作为编辑环境，这应该是主流的选择。

- 如果你还使用 Github，那么我向你强烈推荐 Jupyter Notebook，它生成的 ipynb 文件在 Github 上可以直接在线以**可读性极佳**的形式预览——尤其是你需要把图片和绘图代码放在一起的时候。效果可以参考我的[这个页面](https://github.com/wklchris/wklchris.github.io/blob/master/ipynb/Data-science-support-blog-skills.ipynb)。
- 如果你不仅使用 Github，还使用 Python，那你**千万一定**要用 Jupyter Notebook！我的 Github 中[这个页面的 Readme 文件](https://github.com/wklchris/Note-by-Jupyter)大体介绍了怎样安装 Jupyter Notebook 和添加 R 内核支持。
- 如果你只是想要在本地的 RStudio 上把图片和绘图代码一起展示，不想理会什么 Jupyter ，那就搜索“Rmarkdown”吧。

建议先配置好你的 R 工作环境，再继续向下阅读。同时，建议你将 R 放置在 PATH 环境变量中。

### 简单的例子

R 的常见身份是统计或数据语言，那就画个散点图当例子吧。


```R
x <- c(1, 3, 4, 5, 6)
y <- c(4, 7, 2, 1, 6)
plot(x, y)
```


![png](https://wklchris.github.io/assets/ipynb-images/R-learning-basic_1_0.png)


### 查找帮助

以下几个命令是常用的帮助命令：

```r
help.start()  # 帮助首页
help("function")  # 查看函数 function 的帮助
?function  # 同上
```

### 工作目录

工作目录不是一个陌生的概念，简单来说就是在哪个文件夹下进行文件操作（包括部分临时文件、读取设置、读写数据等）。但是指定工作目录似乎没有 Python 那样方便，在不同设备上运行时很是头痛。

```r
getcwd()  # 显示当前工作目录
setcwd(*where)  # 设置工作目录到某路径
```

### 输入/输出选项

R 可以在当前环境有运行已有的 R 文件，算一种广义输入。调用函数是 source(*filename*)。

R 的文字、图片输出可以分离，分别使用 sink(*filename*) 和 以下图片输出函数：bmp (.bmp), pdf (.pdf), jpeg (.jpg), png (.png), postscript (.ps), svg (.svg), win.metafile (.wmf)。例如：

```r
# 直接输出到屏幕
source("script1.R")
# 文本追加模式 append ，输出到文件的同时输出到屏幕 split
sink("myoutput", append=TRUE, split=TRUE) 
pdf("mygraphs.pdf")
source("script2.R")
# 不保存输出
sink()
dev.off()
source("script3.R")
```

### 包的安装与使用

例如 install.packages("gclus")，其中双引号是不能少的。

如果包已经安装，使用 library(gclus) 这样的形式在文件中加载包。
