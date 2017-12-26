---
layout: post
title: Run Jupyter Notebook on Android
categories: Jupyter
tags: Jupyter
---

This article talks about the installation of Jupyter Notebook on Andriod via Termux, including installation of scientific packages/libraries, such as Numpy, pandas, matplotlib, SciPy, scikit-learn,  statsmodels, etc.

本文将介绍 Jupyter Notebook 在安卓上的安装步骤，同时也包括 Numpy, pandas, matplotlib, SciPy, scikit-learn, statsmodels 等其他科学计算包或库的安装。

<!-- more -->

# Jupyter Notebook Installation on Android

If you don't want to go through this article, here's a brief summary:
1. Download the Termux app.

2. Download a coder keyboard (including keys like `Ctrl`, `Alt`, etc.). I use Hacker's Keyboard.

3. Ensure Internet connection.

4. Main steps:
    ```bash
    $ pkg install curl
    $ curl -L https://its-pointless.github.io/setup-pointless-repo.sh | sh

    $ apt install python python-dev clang fftw
    $ apt install freetype freetype-dev libpng libpng-dev pkg-config
    $ apt install libzmq libzmq-dev
    $ pkg install numpy scipy
    $ pip install --upgrade pip  # Could probably be omitted
    $ pip install pandas matplotlib jupyter

    ```
    And `cython` and `statsmodels` are kind of annoying:

    ```bash
    $ LDFLAGS=" -liconv" pip install cython

    $ apt install git
    $ git clone git://github.com/statsmodels/statsmodels.git
    ```

    You may also install other packages such as `scikit-learn` via Termux, but need some tricks:

    ```bash
    $ pkg install proot
    $ termux-chroot
    $ pip install scikit-learn
    ```

    After those installations, you can disconnect your Internet if you want.

5. Then input `jupyter notebook` in the terminal

6. Paste the link shown in the bottom of 5-th step to your browser.

## References

About Numpy and Scipy:
- [@tigran123's Answer in Issue 605](https://github.com/termux/termux-packages/issues/605)
- [Install Scipy the Easy Way](https://wiki.termux.com/wiki/Installing_Scipy_The_Easy_Way)

About Jupyter Notebook:
- [Running Jupyter and the Scipy stack on Android](http://www.leouieda.com/blog/scipy-on-android.html)

About scikit-learn:
- [@ryan15858's Answer in Issue 1618](https://github.com/termux/termux-packages/issues/1618)

About statsmodels (I raised a question here and it has been solved):
- [Issue 1111](https://github.com/termux/termux-packages/issues/1111)