---
layout: post
title: 概率论
categories: Basic
update: 2017-03-12
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
