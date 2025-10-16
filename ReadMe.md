# Welcome to wklchris' personal website

> 语言 / Language: English (Current), [中文](./ReadMe-cn.md).

-----

This is the code repository of my personal Github Pages website [wklchris.github.io](https://wklchris.github.io).

* The site is built using a theme I developed in my spare time named [Simrofy](https://github.com/wklchris/sphinx-simrofy-theme), which is based on [Sphinx](https://www.sphinx-doc.org/).
* For the blogs (in Chinese), please visit [Blog repo](https://github.com/wklchris/blog).

## Dependencies \& Running

See the [requirements.txt](./requirements.txt) for the Python packages needed for the environment. To run Sphinx (a possible outdated version is needed) for this project, use Pip or UV to sync the following settings to your virtual Python environment:

```
uv venv
uv pip sync requirements.txt
```
For pip users, run command: `pip install -r requirements.txt`.

Then activate your Python environment (say, in the folder .venv) and run the make.py file:
```
.venv/Scripts/Activate.ps1  # Windows
python make.py
```

## History

In 2017, I built the site using [Jekyll](https://jekyllrb.com/). If you are interested in those earlier codes, please view the commits history of this repo.


## License

[MIT](./LINCENSE)
