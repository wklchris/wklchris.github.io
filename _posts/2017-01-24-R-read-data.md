---
layout: post
title: R语言（数据读写与操作）
categories: R
tags: R-learning
---
（*博文最后更新于 2017-01-26*）

本节介绍一些实用的数据处理函数（如行、列合并），以及如何从各种数据源读、写数据。

<!-- more -->

## 实用函数

| 函数 | 含义 |
| --- | --- |
| length() | 对象的长度。如 2 行 3 列的矩阵，其长度为 6。 |
| dim() | 对象的维度。如 2 3 表示对象是二维的，有 2 行 3 列。 |
| str() | 对象的结构。常用于查看数据框各列的数据类型、或者因子的分级数量。 |
| class() | 对象的类。比如矩阵的返回结果是 matrix。 |
| typeof() | 对象内数据的类型。比如矩阵的返回结果是 integer。 |
| mode() | 对象的模式。比如矩阵会返回 numeric。 |
| names() | 对象中各成分的名称。 |
| cbind() | 按列合并多个对象。 |
| rbind() | 按行合并多个对象。 |
| *objectname* | 输出对象。 |
| head() | 输出对象的前部，对于数据框而言是前6行。通过 head(*obj*, N) 来指定输出前 N 行。 |
| tail() | 类似地，输出对象的后部。 |
| ls(NULL) | 无参数函数。显示当前变量的列表。 |
| rm() | 删除单个或多个对象。使用 rm(list = ls()) 可以删除除句点

## 手动输入

使用需要赋值的 edit() 函数，或者无需写在赋值语句内的 fix() 函数。


```R
a <- matrix(1:6, nrow=2, ncol=3)
ls()
```


'a'



```R
dt <- data.frame(age = numeric(0), gender = character(0), weight = numeric(0))

# dt <- edit(dt)  # 需要自赋值
# fix(dt)  # 无需自赋值
```

遗憾的是，在 Jupyter Notebook 现行的版本中，尚且不支持 edit() 函数。不过用户可以使用 fix() 函数。

## 读取文件

关于怎样读取来自 URL 地址的网络文件，R 可以实现，但这里不做讨论。以下只讨论本地数据源的读写。

### 分隔符文件

利用 read.table() 函数即可。其常用的参数有：

    read.table(file, [header=T/F, sep=" ", row.names=, col.names=, na.strings=, 
           colClasses=, quote=, skip=, stringAsFactors=T/F,])
           
其中，可选参数的含义大多较好理解：header 表示文件首行是否是列名而不是数据；sep 是列间分隔符；na.strings 指定一个字符向量，内部所有的元素在读取时会被转换为 NA；colClasses 用于指派各列的类型，如 =c("numeric", "character", "NULL") 指定了前两列的类型并跳过了第三列；skip 用于跳过文件的最开始的若干行；stringAsFactors 为 TRUE（默认值）时表示字符向量按因子处理，设为 FALSE 可以提升大文本处理速度。


```R
data.path <- paste(getwd(), '/data/iris.data.csv', sep='')
dt <- read.table(data.path, header=T, sep=",")
head(dt)
```



| X5.1 | X3.5 | X1.4 | X0.2 | Iris.setosa |
| --- | --- | --- | --- | --- |
| 4.9         | 3.0         | 1.4         | 0.2         | Iris-setosa |
| 4.7         | 3.2         | 1.3         | 0.2         | Iris-setosa |
| 4.6         | 3.1         | 1.5         | 0.2         | Iris-setosa |
| 5.0         | 3.6         | 1.4         | 0.2         | Iris-setosa |
| 5.4         | 3.9         | 1.7         | 0.4         | Iris-setosa |
| 4.6         | 3.4         | 1.4         | 0.3         | Iris-setosa |





```R
# 利用 str() 函数查看其信息
str(dt)
```

    'data.frame':	149 obs. of  5 variables:
     $ X5.1       : num  4.9 4.7 4.6 5 5.4 4.6 5 4.4 4.9 5.4 ...
     $ X3.5       : num  3 3.2 3.1 3.6 3.9 3.4 3.4 2.9 3.1 3.7 ...
     $ X1.4       : num  1.4 1.3 1.5 1.4 1.7 1.4 1.5 1.4 1.5 1.5 ...
     $ X0.2       : num  0.2 0.2 0.2 0.2 0.4 0.3 0.2 0.2 0.1 0.2 ...
     $ Iris.setosa: Factor w/ 3 levels "Iris-setosa",..: 1 1 1 1 1 1 1 1 1 1 ...
    

须知：

- 如果列名中包含空格，R 会将空格替换为句点。
- 多数情况下，stringAsFactors 可以设为 FALSE。但是本例中的字符变量表示植物的种类，此处读成因子是正确的。
- 函数 read.csv() 能够读取 csv 文件，但是功能不如 read.table() —— 后者能处理非 csv 文本。

### 处理 Excel 文件

读取一个 Excel 文件最佳的方式，是**预先将其转为 csv 格式，并用上述的 read.table() 方法读取。**

你也可以查找关于 xlsx 包的相关内容，来获知如何直接操作 xlsx 文件。此处略过不提。

### 统计软件数据：SAS/SPSS/Stata

需要用到 foreign 包。

- SAS：使用 read.ssd()。如果你安装了 SAS，可以使用 Hmisc 包的 sas.get()。
- SPSS：使用 read.spss()，或者 Hmisc 包的 spss.get()。
- Stata：使用 read.data()。

### 数据库

一个方法是使用 ODBC 接口。针对你的数据库类型，安装 ODBC 驱动；然后在 R 中安装 RODBC 包。

另一个方法是使用 JDBC 接口，只不过需要 RJDBC 包。

## 写入文件

在我们对于数据进行清洗之后，往往需要把清洗结果输出到一个新文件中。这里就以 csv 格式为例吧。一个通常的 write.table()/write.csv() 的例子：

```{r}
write.csv(dt, "filename.csv", row.names=F)
```

其中 row.names 指定为 FALSE，否则第一列会生成行号一样的数据。
