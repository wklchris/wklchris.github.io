---
layout: post
title: R语言（数学函数与数据管理）
categories: R
tags: R-learning
---


本节内容可应用在数据读取之后。包括基本的运算（包括统计函数）、数据重整（排序、合并、子集、随机抽样等）、异常值（NA/Inf/NaN）处理等内容，也包括函数声明部分的内容。字符串处理的内容会单独归纳到本系列的另一篇文章中。

<!-- more -->

## 数学函数

数学运算符和一些统计学上需要的函数。

### 数学运算符

| 四则 | 幂运算 | 求余 | 整除 |
| --- | --- | --- | --- |
| +, -, \*, / | ^ 或 \*\* | %% | %/% |

例子：


```R
a <- 2 ^ 3
b <- 5 %% 2
c <- 5 %/% 2
print(c(a, b, c))
```

    [1] 8 1 2
    

### 统计函数

- 均值：mean()
- 中位数：median()
- 标准差：sd()
- 方差：var()
- 绝对中位差：mad(x, center=median(x), constant=1.4826, ...)，计算式：

$$ \mathrm{mad}(x) = constant * \mathrm{Median}(|x - center|)$$

- 分位数：quantile(x, probs)，例如 quantile(x, c(.3, 84%)) 返回 x 的 30% 和 84% 分位数。
- 极值：min() & max()
- 值域与极差：range(x)，例如 range(c(1, 2, 3)) 结果为 c(1, 3)。极差用 diff(range(x))
- 差分：diff(x, lag=1)。可以用 lag 指定滞后项的个数，默认 1
- 标准化：scale(x, center=TRUE, scale=TRUE)。可以使用 scale(x) * SD + C 来获得标准差为 SD、均值为 C 的标准化结果。

## 数据框操作

数据框是最常使用的数据类型。下面给出数据框使用中一些实用的场景，以及解决方案。

### 行、列操作

#### 新建

创建一个新的列（变量）是很常见的操作。比如我们现在有数据框 df ，想要在右侧新建一个列，使其等于左侧两列的和。


```R
df = data.frame(x1=c(1, 3, 5), x2=c(2, 4, 6))
# 直接用美元符声明一个新列
df$sumx <- df$x1 + df$x2
df
```



| x1 | x2 | sumx |
| --- | --- | --- |
| 1  | 2  |  3 |
| 3  | 4  |  7 |
| 5  | 6  | 11 |





```R
# 或者使用 transform 函数
df <- transform(df, sumx2=x1+x2)
df
```



| x1 | x2 | sumx | sumx2 |
| --- | --- | --- | --- |
| 1  | 2  |  3 |  3 |
| 3  | 4  |  7 |  7 |
| 5  | 6  | 11 | 11 |




#### 重命名


```R
colnames(df)[4] <- "SUM"
print(colnames(df))
```

    [1] "x1"   "x2"   "sumx" "SUM" 
    

#### 选取/剔除: subset()


```R
# 选取前两列
df[,1:2]  # 或者 df[c("x1", "x2")]
```



| x1 | x2 |
| --- | --- |
| 1 | 2 |
| 3 | 4 |
| 5 | 6 |





```R
# 剔除列 sumx
df <- df[!names(df) == "sumx"]
df
```



| x1 | x2 | SUM |
| --- | --- | --- |
| 1  | 2  |  3 |
| 3  | 4  |  7 |
| 5  | 6  | 11 |





```R
# 剔除第三列
df <- df[-c(3)]  # 或者 df[c(-3)]
df
```



| x1 | x2 |
| --- | --- |
| 1 | 2 |
| 3 | 4 |
| 5 | 6 |




至于选取行，与列的操作方式是类似的：


```R
# 选取 x1>2 且 x2为偶数的观测（行）
df[df$x1 > 2 & df$x2 %% 2 ==0,]
```



| # | x1 | x2 |
| --- | --- | --- |
| **2** | 3 | 4 |
| **3** | 5 | 6 |




再介绍一个 subset() 指令，非常简单粗暴。先来一个复杂点的数据集：


```R
DF <- data.frame(age    = c(22, 37, 28, 33, 43),
                 gender = c(1, 2, 1, 2, 1),
                 q1     = c(1, 5, 3, 3, 2),
                 q2     = c(4, 4, 5, 3, 1),
                 q3     = c(3, 2, 4, 3, 1))
DF$gender <- factor(DF$gender, labels=c("Male", "Female"))

DF
```



| age | gender | q1 | q2 | q3 |
| --- | --- | --- | --- | --- |
| 22     | Male   | 1      | 4      | 3      |
| 37     | Female | 5      | 4      | 2      |
| 28     | Male   | 3      | 5      | 4      |
| 33     | Female | 3      | 3      | 3      |
| 43     | Male   | 2      | 1      | 1      |





```R
# 选中年龄介于 25 与 40 之间的观测
# 并只保留变量 age 到 q2
subset(DF, age > 25 & age < 40, select=age:q2)
```



| # | age | gender | q1 | q2 |
| --- | --- | --- | --- | --- |
| **2** | 37     | Female | 5      | 4      |
| **3** | 28     | Male   | 3      | 5      |
| **4** | 33     | Female | 3      | 3      |




#### 横向合并

如果你有两个**行数相同**的数据框，你可以使用 merge() 将其进行内联合并（inner join），他们将通过一个或多个共有的变量进行合并。


```R
df1 <- data.frame(ID=c(1, 2, 3), Sym=c("A", "B", "C"), Oprtr=c("x", "y", "z"))
df2 <- data.frame(ID=c(1, 3, 2), Oprtr=c("x", "y", "z"))

# 按 ID 列合并
merge(df1, df2, by="ID")
```



| ID | Sym | Oprtr.x | Oprtr.y |
| --- | --- | --- | --- |
| 1 | A | x | x |
| 2 | B | y | z |
| 3 | C | z | y |





```R
# 由于 ID 与 Oprtr 一致的只有一行，因此其余的都舍弃
merge(df1, df2, by=c("ID", "Oprtr"))
```



| ID | Oprtr | Sym |
| --- | --- | --- |
| 1 | x | A |




或者直接用 cbind() 函数组合。


```R
# 直接组合。注意：列名相同的话，在按列名调用时右侧的会被忽略
cbind(df1, df2)
```



| ID | Sym | Oprtr | ID | Oprtr |
| --- | --- | --- | --- | --- |
| 1 | A | x | 1 | x |
| 2 | B | y | 3 | y |
| 3 | C | z | 2 | z |




#### 纵向合并

相当于追加观测。两个数据框必须有**相同的变量**，尽管顺序可以不同。如果两个数据框变量不同请：

- 删除多余变量；
- 在缺少变量的数据框中，追加同名变量并将其设为缺失值 NA。


```R
df1 <- data.frame(ID=c(1, 2, 3), Sym=c("A", "B", "C"), Oprtr=c("x", "y", "z"))
df2 <- data.frame(ID=c(1, 3, 2), Oprtr=c("x", "y", "z"))
df2$Sym <- NA

rbind(df1, df2)
```



| ID | Sym | Oprtr |
| --- | --- | --- |
| 1  | A  | x  |
| 2  | B  | y  |
| 3  | C  | z  |
| 1  | NA | x  |
| 3  | NA | y  |
| 2  | NA | z  |




### 逻辑型筛选

通过逻辑判断来过滤数据，或者选取数据子集，或者将子集作统一更改。在前面的一些例子中已经使用到了。


```R
df$x3 <- c(7, 8, 9)
# 把列 x3 中的奇数换成 NA
df$x3[df$x3 %% 2 == 1] <- NA
df
```



| x1 | x2 | x3 |
| --- | --- | --- |
| 1  | 2  | NA |
| 3  | 4  |  8 |
| 5  | 6  | NA |





```R
df$y <- c(7, 12, 27)
# 把所有小于 3 的标记为 NaN
# 把所有大于 10 的数按奇偶标记为正负Inf

df[df < 3] <- NaN
df[df > 10 & df %% 2 == 1] <- Inf
df[df > 10 & df %% 2 == 0] <- -Inf
df
```



| x1 | x2 | x3 | y |
| --- | --- | --- | --- |
| NaN  | NaN  | NA   |    7 |
|   3  |   4  |  8   | -Inf |
|   5  |   6  | NA   |  Inf |




### 排序

排序使用 order() 命令。


```R
df <- data.frame(age   =c(22, 37, 28, 33, 43),
                 gender=c(1, 2, 1, 2, 1))
df$gender <- factor(df$gender, labels=c("Male", "Female"))

# 按gender升序排序，各gender内按age降序排序
df[order(df$gender, -df$age),]
```



| # | age | gender |
| --- | --- | --- |
| **5** | 43     | Male   |
| **3** | 28     | Male   |
| **1** | 22     | Male   |
| **2** | 37     | Female |
| **4** | 33     | Female |




### 随机抽样

从已有的数据集中随机抽选样本是常见的做法。例如，其中一份用于构建预测模型，另一份用于验证模型。

```{r}
# 无放回地从 df 的所有观测中，抽取一个大小为 3 的样本
df[sample(1:nrow(df), 3, replace=F)]
```

随机抽样的 R 包有 sampling 与 survey，如果可能我会在本系列下另建文章介绍。

### SQL语句

在 R 中，借助 sqldf 包可以直接用 SQL 语句操作数据框（data.frame）。一个来自书中的例子：

```{r}
newdf <- sqldf("select * from mtcars where carb=1 order by mpg", row.names=TRUE)
```

这里就不过多涉及了。

## 异常值处理

异常值包括三类：

- NA：缺失值。
- Inf：正无穷。用 -Inf 表示负无穷。**无穷与数可以比较大小，**比如 -Inf < 3 为真。
- NaN：非可能值。比如 0/0。

使用 is.na() 函数判断数据集中是否存在 NA 或者 NaN，并返回矩阵。注意 NaN 会被判断为缺失值。


```R
is.na(df)
```



| age | gender |
| --- | --- |
| FALSE | FALSE |
| FALSE | FALSE |
| FALSE | FALSE |
| FALSE | FALSE |
| FALSE | FALSE |




另外也有类似的函数来判断 Inf 与 NaN，但只能对一维数据集使用：


```R
print(c(is.infinite(c(Inf, -Inf)), is.nan(NA)))
```

    [1]  TRUE  TRUE FALSE
    

在进行数据处理之前，处理 NA 缺失值是必须的步骤。如果某些数值过于离群，你也可能需要将其标记为 NA 。行移除是最简单粗暴的处理方法。


```R
# NA 行移除
df <- na.omit(df)
df
```



| age | gender |
| --- | --- |
| 22     | Male   |
| 37     | Female |
| 28     | Male   |
| 33     | Female |
| 43     | Male   |



