---
layout: post
title: 概率论
categories: Basic
update: 2017-05-06
tags: Prob-Stats
---

本文回顾概率论中的基础内容。

<!-- more -->

$\newcommand{\ud}{\mathop{}\negthinspace\mathrm{d}}$

## 概率的基础

### 随机现象与样本空间

现象可以分为两种，概率论研究的是随机现象。
- **随机现象(Random Phenomenon)**：并不总是显现相同结果。两个特点：
    1. 可能的结果不止一种。
    2. 无法预知显现的结果。
- **必然现象(Certain Phenomenon**)：只有一个结果。

对相同条件下的可重复随机现象的观察、记录与实验称为**随机试验(Random Experiment)**，比如掷骰子的点数。

随机现象一切可能结果组成的集合称为**样本空间(Sample Space)**，记为 $ \Omega=\lbrace\omega\rbrace $，其中 $ \omega $ 表示基本结果，称为**样本点(Sample Point)**。例如，掷骰子的样本空间是 $\Omega = \lbrace 1, 2, 3, 4, 5, 6\rbrace$。

样本空间分为两种：
- 离散(discrete)样本空间：例如骰子的点数。
- 连续(continuous)样本空间：例如灯泡的寿命：$\Omega = \lbrace t: t\geq 0 \rbrace$。

### 随机事件

由随机现象的某些样本点组成的集合，称为**随机事件(Random Event)**，简称**事件**，一般用大写字母 $A, B, C, \ldots$ 标记。例如事件 $A = $ “出现奇数点”，即 $A = \lbrace 1, 3, 5 \rbrace$ 就是一个事件；同时，它是样本空间 $\Omega = \lbrace 1, 2, 3, 4, 5, 6\rbrace$ 的一个子集。

在需要图示时，通常用长方形表示样本空间 $\Omega$；用其内部的圆表示随机事件，同时暗示其是样本空间的一个子集。这样的图示称为**维恩图(或文氏图，Venn diagram)**。

事件根据其基数(cardinality)可以分类：
  - 单元素集：**基本事件(Elementary Event)**，例如掷骰子的点数为1。
  - 最小子集：即空集 $\varnothing$，**不可能事件(Impossible Event)**，例如掷骰子的点数小于1。
  - 最大子集：即样本空间本身，**必然事件(Certain Event)**，例如掷骰子的点数大于等于1。

#### 事件间的关系

事件间的基本关系有如下三种：
  - 如果事件A发生必然使得事件B发生，称A包含于B，或B**包含(contain)**A，记为 $A\subset B$。对任意事件A，均有：$\varnothing\subset A\subset\Omega$。
  - 如果A包含于B，且B包含于A，称A与B**相等(equivalent)**，记为 $A=B$。
  - 如果事件A与B不会同时发生，称A与B互不相容，或**互斥(mutually exclusive)**。特别地，如果A不发生时B一定发生，称为A与B互为**对立(complementation)**。必然事件与不可能事件互为对立事件。

#### 事件间的运算

事件的本质是集合，也可以像集合一样运算：
  - **并(Union)**：记为$A\cup B$，即A与B至少有一个发生。
  - **交(Intersection)**：记为$A\cap B$ 或 $AB$，即事件A与B同时发生。
  - **差(Difference)**：事件A对B的差，记为$A-B$，即事件A发生而B不发生。
  - 对立：事件A的对立，记为$\overline{A}$。满足$\overline{A}=\Omega-A$。注意，$A\overline{B}=A-B$。

对于事件 $A_1, A_2, \ldots$ 的交与并（推广到有限或者无限可列的情形），$\bigcup\limits_{i=1}^n A_i$ 称为**有限并**，$\bigcup\limits_{i=1}^\infty A_i$ 称为**可列并**。类似地，有**有限交**与**可列交**。

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
4.  对偶率(德摩根定律，De Morgan's laws)：
    - 并的对立等于对立的交：$\overline{A\cup B}=\overline{A}\cap \overline{B}$
    - 交的对立等于对立的并：$\overline{A\cap B}=\overline{A}\cup \overline{B}$
    - 均可推广到有限或可列的场合：$\overline{\bigcup\limits_i A_i}=\bigcap\limits_i \overline{A_i}$，$\overline{\bigcap\limits_i A_i}=\bigcup\limits_i \overline{A_i}$。


### 随机变量与概率

用于表示随机现象结果的变量称为**随机变量(Random Variable)**，常用大写字母$X, Y, Z$表示。用大写字母P表示其发生的概率，例如用$X$表示掷骰子一次的点数，则掷骰子的点数大于5的概率：

$$ P(X>5) = \frac{1}{6} $$

#### 公理化定义

设 $\mathscr{F}$ 是样本空间 $\Omega$ 的一个事件域，对任意事件 $A\in \mathscr{F}$，定义在 $\mathscr{F}$ 上的一个实值函数 $P(A)$，使其满足：

1. **非负性**：若 $A\in \mathscr{F}$，则 $P(A)\geq 0$，
2. **正则性**：$P(\Omega) = 1$，
3. **可列可加性**：对于互不相容的 $A_1, A_2, \ldots$，有：

$$P\left(\bigcup\limits_{i=1}^\infty A_i\right)=\sum_{i=1}^\infty P(A_i),$$

则称 $P(A)$ 为事件 $A$ 的**概率(Probability)**，三元素 $(\Omega, \mathscr{F}, P)$ 为**概率空间(Probability Space)**。

#### 古典概型

定义概率的古典模型，又称**古典概型(Classical Probability Model)**，用于定义有限个、等可能性的 $n$ 个样本点的随机现象概率。对于含有 $k$ 个样本点的事件，其概率即为 $P(A) = k/n$。

例如，记掷硬币两次的结果为事件 $A$，用 $(x, y)$ 表示结果（0为反，1为正）。其样本空间是：

$$\Omega = \lbrace (0, 0), (0, 1), (1,0), (1, 1) \rbrace$$

因此两次均为正面的概率是 $1/4$。

#### 几何概型

如果事件与样本空间都能够以几何方式进行度量（长度、面积、体积等），那么事件 $A$ 的概率为 $P(A) = S_A / S_\Omega$。这样求得概率的方式称为**几何概型(Geometric Probability Model)**。

#### 随机模拟：蒙特卡罗法

通过大量重复试验来求近似值的方法，称为随机模拟，或**蒙特卡罗法(Monte Carlo Method)**。例如著名的**布丰投针问题(Buffon's Needle Problem)**：平面上画有间隔为 $d$ 的等距平行线，向平面投掷一枚长度为 $l (l<d)$ 的针，求其与任一平行线相交的概率。

以 $x$ 表示针的中点到最近的一条平行线的距离，以 $\varphi$ 表示针与此直线的交角，那么：$0\leq x\leq d/2, 0\leq \varphi\leq \pi$。样本空间的面积为 $S_\Omega = \pi d/2$。将“针与平行线相交”记为事件 $A$，其充要条件是：$x\leq \frac{l}{2}\sin\varphi $。因此概率为：

$$ P(A) = \frac{S_A}{S_\Omega} = \frac{\int_0^\pi \frac{l\sin\varphi}{2}\ud\varphi}{\frac{d}{2}\pi}
=  \frac{2l}{d\pi} $$

因此通过大量重复试验的方法（比如在 $N$ 次试验中事件发生了 $k$ 次），可以近似用频率估计概率：$ k/N \approx P(A) = \frac{2l}{d\pi} $，从而能够以此求 $\pi$ 的近似值：

$$ \pi \approx \frac{2lN}{kd}$$

### 概率的运算性质

1. 不可能事件概率为0：$P(\varnothing) = 0$ （$\Omega = \Omega + \varnothing + \varnothing +\ldots$，而它们互不相容）
2. 有限可加性：$P\left(\bigcup\limits_{i=1}^n A_i\right)=\sum_{i=1}^n P(A_i)$ （通过无限可加性与性质 1 可证）
3. 对立事件的概率：$P(\overline{A})=1-P(A)$（由正则性与性质 2 可证）
4. 单调性：若 $B\subset A$，则 $P(A-B)=P(A)-P(B)$（B 发生则 A 必然发生，说明 A 更容易发生，其概率更大）
    - 推论：若 $B\subset A$，则 $P(A)\geq P(B)$
5. 概率的差公式：对任意事件 $A, B$, 有：$P(A-B) = P(A) - P(AB)$
6. 概率的并公式：对任意两个事件 $A, B$，有：$P(A\cup B)=P(A)+P(B)-P(AB)$
    - 推广到 $n$ 的情形：$$P\left(\bigcup\limits_{i=1}^n A_i\right)=\sum\limits_{i=1}^n A_i - \sum\limits_{1\leq i<j\leq n} P(A_iA_j) + \sum\limits_{1\leq i<j<k\leq n} P(A_iA_jA_k) +\ldots + (-1)^{n-1}P(A_1A_2\cdots A_n)$$
    - 推论 - 半可加性：$P(A\cup B)\leq P(A)+P(B)$，对 $n$ 的情形：$P\left(\bigcup\limits_{i=1}^n A_i\right)\leq \sum\limits_{i=1}^n P(A_i)$

### 条件概率

在事件 $B$ 发生的条件下事件 $A$ 发生的概率，称为**条件概率(Conditional Probability)**，记作 $P(A\vert B)$。其计算式：

$$ P(A\vert B) = \frac{P(AB)}{P(B)} $$

#### 全概率公式

对于样本空间 $\Omega$ 的一个分割 $B_1, B_2, \ldots, B_n$（即诸 $B_i$ 互不相容，且 $\bigcup_{i=1}^n B_i=\Omega$），如果诸 $P(B_i) > 0$，则对任意事件 $A$ 均有：

$$ P(A) = \sum_{i=1}^n P(B_i)P(A\vert B_i)， $$

特别地，其最简形式：$P(A)=P(B)P(A\vert B)+P(\overline{B})P(A\vert \overline{B})$。这个公式称为**全概率公式(Law of total probability)**。

其重要的应用之一是敏感调查(Sensitive Data Collection)。例如设置两个问题 V 与 W，其中 W 是敏感问题，但两者的选项相同（例如都是“是”与“否”）。在调查时，调查者事先从一个红球比率为 s、只装有红白两种球的黑箱中摸球，抽到红球则回答敏感问题 W，抽到白球回答常规问题 V；而调查员对被调查者抽球的颜色并不知情 —— 此过程可以减少被调查者回答敏感问题时的顾虑。那么，回答“是”的概率 P 可以通过总调查数 $N$ 与回答“是”总数 $k$ 进行估计。假设回答 V 为“是”的概率是已知的 $q$, 回答 W 为“是”的概率是待求的 $p$，有：

$$ \frac{k}{N} \approx P = q\times (1-s) + p\times s, $$

因此： $p = \frac{k/N - q(1-s)}{s}$ 即为敏感问题 W 回答“是”的概率估计。

#### 贝叶斯公式

贝叶斯公式，或称**贝叶斯定理(Bayes' theorem)**，是从全概率公式的基础上推导的。对于样本空间的一个分割 $B_1, B_2, \ldots, B_n$，其形式：

$$ P(B_i\vert A) = \frac{P(B_i)P(A\vert B_i)}{\sum_{j=1}^n P(B_j)P(A\vert B_j)} = \frac{P(B_i)P(A\vert B_i)}{P(A)}$$

其同样有最简形式：

$$ P(B\vert A) = \frac{P(B)P(A\vert B)}{P(B)P(A\vert B)+P(\overline{B})P(A\vert \overline{B})} $$

贝叶斯公式在应用中一个著名的例子是毒品测试（Drug Test, 或者癌症检测）。假设人群中吸毒者占 $0.5\%$，毒品测试对于吸毒者以 $0.99$ 的概率成阳性，对非吸毒者以 $0.99$ 的概率成阴性。记“被检测者是吸毒者”为事件B，“检测结果呈阳性”为事件A；那么一个随机抽取者的吸毒测试结果是阳性，其实际是吸毒者的概率为：

$$ P(B\vert A) = \frac{P(B)P(A\vert B)}{P(B)P(A\vert B)+P(\overline{B})P(A\vert \overline{B})}
               = \frac{0.005\times 0.99}{0.005\times 0.99 + 0.995\times 0.01} \approx 0.332$$

这表示即使抽选结果为阳性，其不吸毒的概率是比吸毒的概率更高的。如果吸毒者在人群中的比例更低，计算出的被检测者实际吸毒的概率也会相应降低（因此癌症检测呈阳性的误诊可能性比本例会更高）。为了减小误测，最简单的办法是复查：

$$ P(B\vert A)' = \frac{0.332\times 0.99}{0.332\times 0.99 + 0.668\times 0.01} \approx 0.980$$

即复查也呈阳性的误测率仅有 $2\%$。

### 独立性

独立性是指一个事件的发生不影响另一个事件的发生。对于条件概率 $P(A\vert B)$，如果事件 $A$ 与 $B$ 是独立的，那么 $P(A\vert B)=P(A), P(B\vert A)=P(B)$。此时再由条件概率的定义式：$P(A\vert B)=P(AB)/P(B)$ ，推出：

$$ P(AB) = P(A)P(B) $$

显然上式对于 $P(A)=0$ 或者 $P(B)=0$ 的情形也是成立的。我们把满足上式的事件 $A$ 与 $B$ 定义为相互独立的，简称为 $A$ 与 $B$ **独立(Independent)**；否则，则称 $A$ 与 $B$ 不独立（或相依）。

如果 $A$ 与 $B$ 独立，那么 $\overline{A}$ 与 $B$ 独立， $A$ 与 $\overline{B}$ 独立，且 $\overline{A}$ 与 $\overline{B}$ 独立。

#### 多事件的独立性

对于三个事件 $A, B, C$，如果：$P(AB)=P(A)P(B), P(AC)=P(A)P(C), P(BC)=P(B)P(C)$，那么称它们**两两独立(Pairwise Independent)**；若在此外还有：$P(ABC)=P(A)P(B)P(C)$，那么称事件 $A, B, C$ **相互独立(Mutually Independent)**。

推广到 $n$ 个事件的情形：对事件 $A_1, A_2, \ldots, A_n$，如果满足（其中 $i, j, k$ 两两不相同）：

$$ \begin{align*}
P(A_iA_j) &= P(A_i)P(A_j),\\
P(A_iA_jA_k) &= P(A_i)P(A_j)P(A_k),\\
&\vdots \\
P(A_1A_2\cdots A_n) &= P(A_1)P(A_2)\cdots P(A_n),
\end{align*} $$

那么，称此 $n$ 个事件相互独立。

#### 多重独立重复试验

试验的任一结果都是一个事件；如果试验 $E_1, E_2, \ldots, E_n$ 的试验 $E_i$ 的任一结果与试验 $E_j (j\neq i)$ 的任一结果都是独立的，那么称此 $n$ 个试验相互独立。如果这 $n$ 个试验是等同的，则称为 $n$ 重**独立重复试验(Independent Repeated Trials)**。如果在此独立重复试验下，每次试验的结果只有两种（$A$ 与 $\overline{A}$，通常是“成功”与“失败”），那么称为 $n$ 重**伯努利试验(Bernouli Trial, or Binomial Trial)**；例如掷硬币 $n$ 次。

## 随机变量及其分布

随机变量常用大写字母 $X, Y, Z$ 表示，其取值一般用 $x, y, z$ 表示。如果一个随机变量的取值是有限个或者可列个，那么称为离散随机变量；否则，称为连续随机变量。对于随机变量 $X$ 与任意实数 $x$，如果函数 $F(x)$ 满足：

$$ F(x) = P(X\leq x) $$

那么称其为随机变量 $X$ 的**分布函数(Distribution Function)**，或**累计分布函数(Cumulative Distribution Function, or cdf)**。对于离散随机变量，其分布函数是分段函数，也被称为分布列，形如：$F(x_i) = c_i$，其中 $\lbrace c_i\rbrace$ 是一个递增的常数数列。

如果实数轴上存在一个非负可积函数 $p(x)$，使得对任意 $x$：

$$ F(x) = \int_{-\infty}^x p(t)\ud t $$

那么，称此 $p(x)$ 为 $X$ 的**概率密度函数(Probability Density Function, or pdf)**或密度函数。在导数存在的点，有：$F'(x)=p(x)$。

### 期望

离散随机变量的分布列：$p(x_i)=P(X=x_i)$，如果 $\sum_{i=1}^\infty \vert x_i\vert p(x_i) < \infty$，则称 $E(X)=\sum_{i=1}^\infty x_i p(x_i)$ 为随机变量 $X$ 的**期望(Expectation)**，或称均值。连续随机变量的密度函数：$p(x)$，如果$\int_{-\infty}^\infty \vert x\vert p(x)\ud x < \infty$，那么 $E(x) = \int_{-\infty}^\infty x p(x)\ud x$ 为随机变量 $X$ 的期望，或称均值。

如果以上式不是有限值，那么对应期望不存在。

期望的性质（用 $p(x_i)$ 表示离散随机变量 $X$ 的分布列，$p(x)$ 表示连续随机变量 $X$ 的密度函数）：
1. $X$ 的某一函数 $g(X)$ 的期望（若存在，下同）：

$$ E[g(X)] = \begin{cases}
\sum_i g(x_i)p(x_i), X\text{ is discrete},\\
\int_{-\infty}^\infty g(x)p(x)\ud x, X\text{ is continuous}.
\end{cases} $$

2. 对于常数 $c$，$E(c)=c$。
3. 对于任意常数 $a$，$E(aX) = aE(X)$。
4. 对于任意两个函数 $g_1, g_2$，$E[g_1(X)\pm g_2(X)] = E[g_1(X)]\pm E[g_2(X)]$。

### 方差与标准差

如果随机变量 $X^2$ 的期望存在，则 $X$ 的**方差(Variance)**定义为偏差平方 $(X - EX)^2$ 的数学期望：

$$ Var(X) = \begin{cases}
\sum_i (x_i-EX)^2 p(x_i), X\text{ is discrete},\\
\int_{-\infty}^\infty (x-EX)^2 p(x)\ud x, X\text{ is continuous}.
\end{cases} $$

并将方差的算术平方根定义为**标准差(Standard Deviation, or SD)**，记为 $\sigma (X)$ 或 $\sigma_X$。

#### 方差的性质

方差（如果存在）有如下的性质：
- $Var(X) = E(X^2) - [E(X)]^2$。
- 对任意常数 $c$，$Var(c)=0$。
- 对任意常数 $a, b$，$Var(aX\pm b)=a^2Var(X)$。

#### 切比雪夫不等式

下面给出一个不等式，用于确定大偏差 $\vert X-EX\vert \geq \varepsilon$ 的概率的上界，称为切比雪夫（Chebyshev）不等式：

$$ P(\vert X-EX\vert\geq \varepsilon) \leq \frac{Var(X)}{\varepsilon^2} $$

证明：$$ P(\vert X-EX\vert\geq \varepsilon) = \int\limits_{x: \vert X-EX\vert\geq \varepsilon} p(x)\ud x \leq \int\limits_{x: \vert X-EX\vert\geq \varepsilon} \frac{(x-EX)^2}{\varepsilon^2} p(x)\ud x\leq \int\limits_{-\infty}^\infty \frac{(x-EX)^2}{\varepsilon^2} p(x)\ud x= \frac{Var(X)}{\varepsilon^2} $$

### 常用离散分布

#### 二项分布

## 参考文献

[1] 茆诗松，程依明，濮晓龙. *概率论与数理统计教程（第二版）*. 高等教育出版社. 2010 