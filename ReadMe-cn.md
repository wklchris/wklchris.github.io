# 欢迎来到 wklchris 的个人主页

> 语言 / Language: 中文（当前），[English](./ReadMe-en.md)

-----

此处是我的个人 Github Pages 站点 [wklchris.github.io](https://wklchris.github.io) 的代码仓库。

* 本站点由我个人开发的、名为 [Simrofy](https://github.com/wklchris/sphinx-simrofy-theme) 主题的搭建，它基于 [Sphinx](https://www.sphinx-doc.org/)。
* 关于本站的博文（中文），请移步 [Blog 仓库](https://github.com/wklchris/blog)。


## 本站历史

在 2017 年，我使用 Jekyll 建设了该站点。如有兴趣，可访问历史代码以获得详细信息。

一个详细的本站点发展史可以阅读[本站历史](https://wklchris.github.io/blog/About.html).

## 依赖项与运行

请查看 [requirements.txt](./requirements.txt) 来了解 Python 环境所需的包。要为本项目执行 Sphinx 命令（可能需要一个过时的版本），使用 Pip 或者 UV 工具来同步以下设置到你的本地 Python 虚拟环境：
```
uv venv
uv pip sync requirements.txt
```
对于 pip 用户，则使用 `pip install -r requirements.txt` 命令。

之后激活 Python 环境（假设位于 .venv 目录），并允许 make.py 文件来构建网站：
```
.venv/Scripts/Activate.ps1  # Windows
python make.py
```

## 许可证

[MIT](./LINCENSE)
