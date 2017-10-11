---
layout: post
title: Introduction to Linear Regression
categories: Basic
tags: Prob-Stats
---


This post briefly tells the general idea of linear regression. Examples are also included.

<!-- more -->

This post will cover:
- Fundamental Knowledge before Get Started
- Simple Linear Regression

## Fundamental Knowledge

Before get started, recall some basic things in statistic:
$\newcommand{\uE}{\mathop{}\negthinspace\mathrm{E}}
\newcommand{\ucov}{\mathop{}\negthinspace\mathrm{Cov}}
\newcommand{\uvar}{\mathop{}\negthinspace\mathrm{Var}}$

### Expected Value

Properties:

$$\uE(a+bX) = a+b\uE(X)$$

### Variance and Covariance

Definition of variance: 

$$\uvar(Y) = \uE\Big[(Y-\uE(Y))^2\Big] = \uE(Y^2) - \Big[\uE(Y)\Big]^2$$

Definition of covariance:

$$\ucov(Y,Z) = \uE\Big[(Y-\uE(Y))\cdot(Z-\uE(Z))\Big]$$

Properties:

$$\uvar(a+cY)=c^2(\uvar(Y))$$

$$\ucov(a+bY, c+dZ)=bd\ucov(Y,Z)$$

And there's a significant property when calculate the variance of summation of random variables:

$$\uvar(\sum_{i=1}^n a_iY_i) = \sum_{i=1}^n\sum_{i=j}^n a_ia_j\ucov(Y_i,Y_j),$$

which also has a special form when $Y_i$ are mutually independent:

$$\uvar(\sum_{i=1}^n a_iY_i) = \sum_{i=1}^n a_i^2\uvar(Y_i)$$

### Coefficient of Correlation

In case that we might use this later, the definition of coefficient of correlation is introduced here:

$$\rho(Y,Z) = \frac{\ucov(Y,Z)}{\sqrt{\uvar(Y)\uvar(Z)}} \in [-1,1]$$

When $Y$ and $Z$ are independent, we know $\ucov(Y,Z)=0, \rho(Y,Z)=0$.
