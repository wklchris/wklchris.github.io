---
layout: post
title: 怎样用 Github Pages 建立博客（3. 绘图/科学计算）
category: Jekyll
tag: create-blog
---


本文基于前两篇的搭建 Jekyll 的基础上，向博客添加能够方便地撰写科学计算内容的功能，主要是通过 Jupyter Notebook 将 ipynb 文件转换为 Markdown 文件，实现方便地插入 Python/R 的代码及其图像。

该功能在 Jekyll 中并没有原生支持，因此我编写了 Python 脚本，来帮助我完成这一系列自动化工作。

## Python 例子

由于在 Jupyter Notebook 中，一篇文章只能是单内核的（不能同时使用 Python 和 R），因此这里只演示 Python 代码的部分。如果需要显示两种代码，应当另外新建基于另一种代码内核的 ipynb 文件。

此例基于 matplotlib. 语法 Python 3.


```python
import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xticks(np.arange(0, 3 * np.pi, np.pi / 2))
ax.set_xticklabels(['0', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$'])

plt.axis([0, 2 * np.pi, -1.2, 1.2])
plt.show()
```


![png](https://wklchris.github.io/assets/ipynb-images/Data-science-support-blog-skills_1_0.png)


## 实现原理

Jupyter 支持将 ipynb 转为 Markdown 文件，步骤是：

1. 在 ipynb 文件所在文件夹，Shift + 鼠标右键呼出命令行，输入：`Jupyter nbconvert -- to markdown filename.ipynb`，其中 *filename* 请自行根据文件名替换。  
2. 自动生成的文件：
    - 生成一个名为 *filename*\_files 文件夹，存放 ipynb 生成的图片；  
    - 生成同名的 *filename*.md 文件，图片以如下形式链接（以本文为例）：

```
![png](data-science-support-blog-skills_files/data-science-support-blog-skills_1_0.png)
```

因此我们要做的事情就很简单了：

1. 在博客下新建一个名为 ipynb 的文件夹，以后 Jupyter Notebook 文件都放在里面；  
2. 在主文件夹（ipynb 文件夹的上级）下，建立一个 python 文件 \_to-ipynb.py，用于转换。具体代码见下一节。
3. 将 ipynb 文件夹下不需要进行版本控制的内容添加到 .gitignore 文件中。

以后每次写完 ipynb ，用 \_to-ipynb.py 脚本运行一遍即可（或者写一个 server.bat 文件，更粗暴）。对应的图片会自动归档到 `assets/ipynb-images` 目录下，并修复转换好的 markdown 文件中的图片链接。

## \_to-ipynb.py 文件内容

**~ 下载链接在此：[点我](https://github.com/wklchris/wklchris.github.io/blob/master/_to-ipynb.py)**

所有的博客记录在 /ipynb/\_post_head.csv 中，这个就不用上传了。

- 每一列依次是（以下以本博客为例）：
    - 日期：2017-01-08
    - 博客主文件名 (fname)：Data-science-support-blog-skills，也即对应的 ipynb 文件名。
    - 博客标题：怎样用 Github Pages 建立博客（3. 绘图/科学计算）
    - 博客类别：Jekyll
    - 博客系列标签：create-blog
- csv 文件的首行是想要转换的 ipynb 博客的 **主文件名**，如 Data-science-support-blog-skills。

这样做的好处：

- 提供了一个文件可以直接查阅所有博客信息
- 主文件夹的 server.bat 文件只需两行，就可以自动转换 ipynb 并提供本地博客预览：  
      python "_to-ipynb.py"
      jekyll serve
- 无需手动添加 YAML 文件头。**重要的是**：修改以前的、由 ipynb 转换得到的日志变得十分方便，因为 csv 中都记录好了文件头。

首先，检测路径，从 csv 中读取博客信息，确定要转换的 ipynb 文件，以及转换后应添加到 Markdown 文件的 YAML 文件头。

```python
import os, re
import shutil
import csv

# Main
thepath = os.getcwd()
ipynb_path = os.path.join(thepath, 'ipynb')
yaml_csv_path = os.path.join(ipynb_path, r'_post_head.csv')

# Read head string from "_post_head.csv"
with open(yaml_csv_path, 'r', encoding="utf8") as f:
    hasPost = False
    for row in csv.reader(f):
        if len(row) == 1:  # First line is the default post name
            fname = row[0]
            continue
        if fname == row[1]:
           # If the post was not written by Jupyter, skip converting
           if not os.path.isfile(os.path.join(ipynb_path, '{}.ipynb'.format(fname))):
                print('\n\tWarning: "{}.ipynb" doesn\'t exist.\n\n'.format(fname))
                exit()
            date = row[0]
            headstr = '---\n'
            headstr += 'layout: post\n'
            headstr += 'title: {}\n'.format(row[2])
            headstr += 'categories: {}\n'.format(row[3])
            headstr += 'tags: {}\n---\n\n'.format(row[4])
            hasPost = True
            break
    if not hasPost:
        print('No record relevant to "{}" in csv file'.format(fname))
        exit()
```

然后指定 Jupyter 文件目录。转换 ipynb 为 markdown，再将其从 /ipynb 移动到 /\_posts 下，并把相关的图片从 /ipynb/*fname*_files 下移动到 /assets/ipynb-images 下。最后将 /ipynb 下的图片文件夹删除。

```python
ipynb_image_path = os.path.join(ipynb_path, r'{}_files'.format(fname))
destination_path = os.path.join(os.path.join(thepath, 'assets'), 'ipynb-images')
post_path = os.path.join(thepath, r'_posts/{}.md').format(date + '-' + fname)

# Convert ipynb to markdown; 
os.system('jupyter nbconvert --to markdown ipynb/{}.ipynb'.format(fname))
# Move it to "/_posts" and renameit
shutil.move(os.path.join(ipynb_path, '{}.md'.format(fname)), 
            os.path.join(thepath, r'_posts/{}.md').format(fname))
if os.path.isfile(post_path):
    os.remove(post_path)
os.rename(os.path.join(thepath, r'_posts/{}.md').format(fname), post_path)

# Move the images under "/ipynb/<fname>_files" to "/assets/ipynb-images"
def moveallfiles(origindir, destinationdir):
    if not os.path.exists(origindir):
        return
    for file in os.listdir(origindir):
        originfile = os.path.join(origindir, file)
        destinationfile = os.path.join(destinationdir, file)
        # If it exists, then delete it and then conduct the movement
        if os.path.isfile(destinationfile):
            os.remove(destinationfile)
        shutil.move(originfile, destinationfile)
    # Delete the origin image path
    shutil.rmtree(ipynb_image_path)

moveallfiles(ipynb_image_path, destination_path)
```

再就是修复 markdown 文件夹存在的问题。有：

- 修复图片链接。这些图片会随 assets 文件夹传到 Github 中，指定链接位置即可。注意：**图片直链的位置是以博客网址而不是 github 网址开头的。**
- 添加 YAML 文件头（变量 headstr）。
- 修复表格显示问题。从 ipynb 直接转换得到的 HTML 表格总是不能正常显示，我选择将其转换为 Markdown。关于表格的风格问题，参考[这里]({{ site.url }}/Advanced-blog-skills.html#表格样式)进行设置。

```python
with open(post_path, 'r', encoding='utf8') as f:
    fstr = f.read()

# Replace the image link strings
image_link = r'https://wklchris.github.io/assets/ipynb-images'
fstr = re.compile(r'{}_files'.format(fname)).sub(image_link, fstr)
fstr = headstr + fstr

# Convert HTML table to markdown table
def transfertable(tablehtml):
    tablehtml = re.compile(r'<table>').sub('', tablehtml)
    tablehtml = re.compile(r'</tbody>[\n]</table>').sub('', tablehtml)

    # Table head
    tablehtml = re.compile(r'<tr><th>').sub(r'#', tablehtml)
    tablehead = re.compile(r'<thead>[\S\s]*?</thead>').findall(tablehtml)
    tablehead = tablehead[0]
    # Headline
    col_num = len(re.compile(r'</th>').findall(tablehead))
    tablehtml = re.compile(r'<tbody>').sub('|' + ' --- |' * col_num, tablehtml)

    headcontent = re.compile(r'(?<=>)[\S]*?(?=</th>)').findall(tablehead)
    newhead = '| ' + ' | '.join(headcontent) + ' |'
    tablehtml = re.compile(tablehead).sub(newhead, tablehtml)

    # First column
    firstcol = re.compile(r'(?<=\s)<tr>[\S\s]*?<td>').findall(tablehtml)
    for cell in firstcol:
        origincell = cell
        cell = re.compile(r'<tr><th[^>]*?>').sub('| **', cell)
        cell = re.compile(r'</th><td>').sub('** | ', cell)
        tablehtml = re.compile('\t' + origincell).sub(cell, tablehtml)

    # Table body
    tablehtml = re.compile(r'<tr><td>').sub('| ', tablehtml)
    tablehtml = re.compile(r'</td></tr>').sub(' |', tablehtml)
    tablehtml = re.compile(r'</th><td>').sub(' | ', tablehtml)
    tablehtml = re.compile(r'</td><td>').sub(' | ', tablehtml)

    return tablehtml

tablehtmllst = re.compile(r'<table>[\s\S]*?</table>').findall(fstr)
if tablehtmllst:
    for table in tablehtmllst:
        fstr = re.compile(table).sub(transfertable(table), fstr)
``` 

最后，把 /\_posts 下原有的同名 md 文件删除，用一个新文件替换它。

```python
os.remove(post_path)
with open(post_path, 'w', encoding='utf8') as f:
    f.write(fstr)
```
