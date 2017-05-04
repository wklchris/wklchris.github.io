---
layout: post
title: 概率论
categories: Basic
update: 2017-05-04
tags: Probability
---

本文回顾概率论中的基础内容。

<!-- more -->

## 概率的基础

### 随机现象 

现象可以分为两种，概率论研究的是随机事件。
- **随机现象(Random Phenomenon)**：并不总是显现相同结果。两个特点：
    1. 可能的结果不止一种。
    2. 无法预知显现的结果。
- **必然现象(Certain Phenomenon**)：只有一个结果。

对相同条件下的可重复随机现象的观察、记录与实验称为**随机试验(Random Experiment)**，比如掷骰子的点数。

### 样本空间

随机现象一切可能结果组成的集合称为**样本空间(Sample Space)**，记为 $ \Omega=\lbrace\omega\rbrace $，其中 $ \omega $ 表示基本结果，称为**样本点(Sample Point)**。例如，掷骰子的样本空间是 $\Omega = \lbrace 1, 2, 3, 4, 5, 6\rbrace$。

样本空间分为两种：
- 离散(discrete)样本空间：例如骰子的点数。
- 连续(continuous)样本空间：例如灯泡的寿命：$\Omega = \lbrace t: t\geq 0 \rbrace$。

### 随机事件

由随机现象的某些样本点组成的集合，称为**随机事件(Random Event)**，简称**事件**，一般用大写字母$A, B, C, \ldots$标记。例如事件 $A = $ “出现奇数点”，即 $A = \lbrace 1, 3, 5 \rbrace$ 就是一个事件；同时，它是样本空间 $\Omega = \lbrace 1, 2, 3, 4, 5, 6\rbrace$ 的一个子集。

在需要图示时，通常用长方形表示样本空间 $\Omega$；用其内部的圆表示随机事件，同时暗示其是样本空间的一个子集。这样的图示称为**维恩图(或文氏图，Venn diagram)**。

事件根据其基数(cardinality)可以分类：
  - 单元素集：**基本事件(Elementary Event)**，例如掷骰子的点数为1。
  - 最小子集：即空集$\varnothing$，**不可能事件(Impossible Event)**，例如掷骰子的点数小于1。
  - 最大子集：即样本空间本身，**必然事件(Certain Event)**，例如掷骰子的点数大于等于1。

#### 事件间的关系

事件间的基本关系有如下三种：
  - 如果事件A发生必然使得事件B发生，称A包含于B，或B**包含(contain)**A，记为$A\subset B$。对任意事件A，均有：$\varnothing\subset A\subset\Omega$。
  - 如果A包含于B，且B包含于A，称A与B**相等(equivalent)**，记为$A=B$。
  - 如果事件A与B不会同时发生，称A与B互不相容，或**互斥(mutually exclusive)**。特别地，如果A不发生时B一定发生，称为A与B互为**对立(complementation)**。必然事件与不可能事件互为对立事件。

#### 事件间的运算

事件的本质是集合，也可以像集合一样运算：
  - **并(Union)**：记为$A\cup B$，即A与B至少有一个发生。
  - **交(Intersection)**：记为$A\cap B$ 或 $AB$，即事件A与B同时发生。
  - **差(Difference)**：事件A对B的差，记为$A-B$，即事件A发生而B不发生。
  - 对立：事件A的对立，记为$\overline{A}$。满足$\overline{A}=\Omega-A$。注意，$A\overline{B}=A-B$。

运算性质：
1. 交换率：
     - $A\cap B=B\cap A$
     - $AB=BA$。
2. 结合率：
     - $(A\cup B)\cup C=A\cup(B\cup C)$
     - $(AB)C=A(BC)$
3.  分配率：
     - $(A\cup B)\cap C=AC\cup BC$
     - $(A\cap B)\cup C= (A\cup C)\cap (B\cup C)$
4.  对偶率：
    - 并的对立等于对立的交：$\overline{A\cup B}=\overline{A}\cap \overline{B}$
    - 交的对立等于对立的并：


### 随机变量

用于表示随机现象结果的变量称为**随机变量(Random Variable)**，常用大写字母$X, Y, Z$表示。用大写字母P表示其发生的概率，例如用$X$表示掷骰子一次的点数，则掷骰子的点数大于5的概率：

$$ P(X>5) = \frac{1}{6} $$

