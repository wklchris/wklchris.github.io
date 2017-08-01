---
layout: post
title: Python科学计算：Cython基础
categories: Python
tags: Py-compute
---


本文将介绍基于 Python3 的 Cython 的基础使用，探索如何写出更快的代码。

<!-- more -->

安装 Cython 的过程就不多说了。可能需要预先安装 [Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/en-us/download/details.aspx?id=48145)。在安装之前，我也安装了 Numpy+mkl 以及 matplotlib，pandas 等科学计算必备组件。虽然没有经过我的验证，但我认为这些组件不是 Cython 必需的。

官方的 Cython 教程 pdf 版可以在 [这个官方页面](https://media.readthedocs.org/pdf/cython/latest/cython.pdf) 下载（英文版）。本文大幅参考了2017年7月31日 Cython 0.26 的官方教程。

本文最后修改时使用的 Cython 版本：


```python
!cython -V
```

    Cython version 0.25.2
    

## 编译流程

Cython 代码必须被**编译**，就像 C 一样；这与纯 Python 代码是不同的。主要的步骤为：
- 通过 Cython 将 .pyx 文件编译为 .c 文件。
- 通过 C 编译器将 .c 文件编译为 .so 文件（如在 Windows 上，则是 .pyd 文件）。

最广为使用的是命令行流程与 distutils 流程。

### 命令行流程

一个 Linux 下使用 gcc 的命令行代码例子：

```bash
$ cython -a yourmod.pyx
$ gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing \ 
   -I/usr/include/python2.7 -o yourmod.so yourmod.c
```

### distutils 流程

distutils 包是 Python 的标准包之一。例如，对于待编译的 hello.pyx 文件，先创建一个 setup.py 文件：
```python
from distutils.core import setup
from Cython.Build import cythonize

setup(
   name = "My hello app",
   ext_modules = cythonize('hello.pyx'), 
   include_path = [numpy.get_include()],  # 需要include其他内容的场合
)
```

然后，在命令行运行：
```cmd
python setup.py build_ext --inplace
```

以上完成了基本的 distutils 流程。在需要使用 C 外部库的场合，需要借助 distutils.extensions.Extension：
```python
from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

sourcefiles = ['example.pyx', 'helper.c', 'another_helper.c']
extensions = [Extension("example", sourcefiles, 
                 include_dirs = [...],
                 libraries = [...],
                 library_dirs = [...])]
setup(
    ext_modules = cythonize(extensions)
)
```

Extension 类拥有许多参数，请参考 distutils 文档。以上 include_dirs, libraries, library_dirs 用于寻找与使用 .h 文件与库。

### pyximport 流程

在没有额外的 C 库需要使用的时候，此方法才可以使用。
```python
import pyximport; pyximport.install()
import hello
```

### cython.inline 流程

单行代码的执行可以使用。
```python
import cython
def f(a):
    ret = cython.inline("return a+b", b=3)
```

## 语言基础

Cython 有三种文件类型：
- pyx 文件：执行文件（Implementation files）：它可以包含任何 Cython 可接受的内容。
- pxd 文件：定义文件（Definition files）。它可以包含 C 类型声明、C 外部库等；不可以使用 Python 类定义。注意命令 `cimport` 的使用。
  1. 在其他的 pxd 文件或 pyx 文件中引用时，使用 cimport 而不是 import 命令。
  2. 在 pyx 文件中引用**同名**的 pxd 文件时，不需要 cimport；因为它们位于同一命名空间。
  3. 为使 cimport 找到已存在的 pxd 文件，其路径必须加在 cython 编译命令的 `-I` 选项后。
- pxi 文件：包含文件（Include files）：通过 include 命令来使用它。

### 数据类型

Python 的动态数据类型牺牲了性能，以换取代码编写过程的轻松。Cython 既然是注重性能的工具，当然会要求以 C 的方式（预指定数据类型）来声明变量。

```python
cdef int i, j, k  # 单个变量
cdef float f, g[4], *h  # 数组
cdef struct Stud:  # 结构体
    int age
    char x
    double y
cdef union Food:  # 共用体
    char *spam
    float *eggs
cdef enum FoodType:  # 枚举类型
    a, b, c
cdef int func(unsigned long l, float f):  # 函数
    ...
cdef class ShootingStar:  # 类
    ...
```

常量可以通过匿名枚举类型来定义：
```python
cdef enum:
    constant_a = 1
```

当需要大量改写时，可以把定义写在 cdef 语法块中：
```python
cdef:
    struct Stud:
        int age
        char x
    int i
    float f
```

Python 中的字符串相当于 Cython 中的 `char*` 定义。需要注意的是，Python 向 Cython 传递 Python 类型字符串变量时仍然存在问题：
```python
cdef char *s
# 可能报错：
s = pystr1 + pystr2  

# 解决方案：
p = pystr1 + pystr2
s = p
```

### 函数定义

函数定义的关键字有如下三种：
- `def`：Python 可调用的函数。
- `cdef`：Cython 可调用的函数。
- `cpdef`：两者均可调用的函数。

（待续）
