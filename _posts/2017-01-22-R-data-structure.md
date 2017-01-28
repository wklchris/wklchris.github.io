---
layout: post
title: R语言（数据结构）
categories: R
update: 2017-01-27
tags: R-learning
---


本节介绍 R 的数据类型，包括 data.frame 相关的重要命令；也给出了转换数据类型的函数。

<!-- more -->

## 数据类型

R 中标志的数据类型有（部分在下文详细介绍）：

- 数字：numeric
- 字符：character
- 向量：vector
- 矩阵：matrix
- 数据框：data.frame
- 因子：factor
- 逻辑：logical

### 类型判断与转换

对于上述的每个类型的缩写 *abbr*，对应的判断与转换函数：

- 判断：is.{abbr}()，例如判断是否是数字 is.numeric()
- 转换：as.{abbr}()


```R
tmp <- c(1:4)
tmp.ch <- as.character(tmp)
list(tmp, tmp.ch)
```


<ol>
	<li><ol class=list-inline>
	<li>1</li>
	<li>2</li>
	<li>3</li>
	<li>4</li>
</ol>
</li>
	<li><ol class=list-inline>
	<li>'1'</li>
	<li>'2'</li>
	<li>'3'</li>
	<li>'4'</li>
</ol>
</li>
</ol>



此外，还有 class() 与 typeof() 函数可以参考：


```R
print(c(class(tmp),
        typeof(tmp)))
```

    [1] "integer" "integer"
    

### 经典的数据类型

由一系列数据组成的变量，按照通常数据处理的分类，有：

- 数值变量（或定量变量，quantitative）：
    - 连续型（continuous）：又称定比。比如试卷在班级的及格率，其可以是 $[0,1]$ 之间的任意值。连续型变量内各数据间的大小（或优劣）关系是显然的。
    - 离散型（discrete）：又称定距。比如班级的同学个数。这类变量常常是通过计数得到的，其任两个数据之间的差值必定为某基础值的整数倍，如不可能有 16.5 个同学。
- 非数值变量（或定性变量，qualitative）：
    - 类别型（categorical）：又称定类。比如同学的主修专业。这类变量中各数据点往往是字符，互相之间无优劣关系。
    - 有序型（ordinal）：又称定序。比如成绩的等级，ABCD。互相之间有优劣顺序。

对于一般的二维数据集，其行与列在不同领域的称呼不同：

| 领域 | 行 | 列 |
| --- | --- | --- |
| 统计学（本文） | 观测(observation) | 变量(variable) |
| 数据库 | 记录(record) | 字段(field) |
| 数据挖掘/机器学习 | 示例(example) | 属性(attribute) |

## 因子(factor)

在 R 中，将非数值变量统称为**因子**（factor），并分为有序因子与无序因子两种。例如，我们有主修专业数据：


```R
prog <- c("Math", "Engineering", "Social Science", "Math")
tmp <- factor(prog)

print(levels(tmp))  # 返回因子的类别
```

    [1] "Engineering"    "Math"           "Social Science"
    


```R
str(tmp)  # 显示因子类别数。str 是 structure 的缩写
```

     Factor w/ 3 levels "Engineering",..: 2 1 3 2
    

从上面的 str(tmp) 中可以看到，Level 1对应 Engineering，2对应Math，3对应Social Science。因为这是根据字符串首字母顺序编号的。

如果你想从数值记录的变量生成一个因子，使用参数 levels 与 labels ：


```R
tmp <- factor(c(1, 2, 3, 1), levels=c(1,2,3), 
              labels=c("Math", "Engineering", "Social Science"))
str(tmp)
```

     Factor w/ 3 levels "Math","Engineering",..: 1 2 3 1
    

如果想把有序型变量转成因子，并指定顺序，可以使用参数 order= ：


```R
tmp <- factor(c("A", "B", "C", "B", "C", "A"), order=TRUE,
             levels=c("B", "A", "C"))
str(tmp)
```

     Ord.factor w/ 3 levels "B"<"A"<"C": 2 1 3 1 3 2
    

## 同类元素集：向量、矩阵与数组

**同类型元素**的一维堆叠叫向量，二维堆叠叫矩阵。更高维的叫数组。

### 向量

如果向量只有一个元素，称为标量。


```R
vector <- c(1:3)
print(vector)
```

    [1] 1 2 3
    

### 矩阵

矩阵的建立方法就复杂一些：


```R
# matr <- matrix(d, nrow=N, ncol=N, byrow=T/F, [dimnames=list(rownamestr,colnamestr)])

matr <- matrix(1:12, nrow=3, ncol=4, byrow=T)
print(matr)
```

         [,1] [,2] [,3] [,4]
    [1,]    1    2    3    4
    [2,]    5    6    7    8
    [3,]    9   10   11   12
    


```R
# 按列填充，并加上行名与列名
rowname <- c('A', 'B', 'C')
colname <- c(as.character(1:4))  # 转为字符串
matr <- matrix(1:12, nrow=3, ncol=4, byrow=F, dimnames=list(rowname, colname))
print(matr)
```

      1 2 3  4
    A 1 4 7 10
    B 2 5 8 11
    C 3 6 9 12
    

下标的使用很简单。


```R
print(matr[2,])  # 第二行
```

     1  2  3  4 
     2  5  8 11 
    


```R
matr[2:3,c(1,3)]  # 第2、3行，第1、3列
```



| # | 1 | 3 |
| --- | --- | --- |
| **B** | 2 | 8 |
| **C** | 3 | 9 |





```R
matr[,-c(1:2)]  # 除前2列外所有列
```



| # | 3 | 4 |
| --- | --- | --- |
| **A** | 7  | 10 |
| **B** | 8  | 11 |
| **C** | 9  | 12 |




### 数组

array() 语法类似于 matrix() 。


```R
# arr <- array(vector, dimensions, dimnames)
# dimensions: 指定数组有几维，以及各维的长度

arr <- array(1:24, c(2, 3, 4), 
             dimnames=list(c('A1', 'A2'), c('B1', 'B2','B3'), c('C1', 'C2', 'C3', 'C4')))
print(arr)
```

    , , C1
    
       B1 B2 B3
    A1  1  3  5
    A2  2  4  6
    
    , , C2
    
       B1 B2 B3
    A1  7  9 11
    A2  8 10 12
    
    , , C3
    
       B1 B2 B3
    A1 13 15 17
    A2 14 16 18
    
    , , C4
    
       B1 B2 B3
    A1 19 21 23
    A2 20 22 24
    
    

## 列表

列表是一系列变量的有序组合。声明方式：

    lst <- list(name1=obj1, name2=obj2, ...)


```R
lst <- list(prog=c("Math", "Engineering"), gender=c(1, 2), grade="No grade")
lst
```


<dl>
	<dt>$prog</dt>
		<dd><ol class=list-inline>
	<li>'Math'</li>
	<li>'Engineering'</li>
</ol>
</dd>
	<dt>$gender</dt>
		<dd><ol class=list-inline>
	<li>1</li>
	<li>2</li>
</ol>
</dd>
	<dt>$grade</dt>
		<dd>'No grade'</dd>
</dl>



你可以通过美元符来调用它们，如：


```R
print(lst$prog)
```

    [1] "Math"        "Engineering"
    

## 数据框：data.frame

数据框是多个等长向量的按列堆叠。这是 R 中最常用的数据结构。由于此内容的重要性，我将其提升了一级大纲。


```R
# df <- data.frame(<col1, col2, ...>, [row.names=])

name <- c('Allen', 'Bruth', 'Chris', 'Daisy')
age <- c(20:23)
gender <- c('Male', 'Male', 'Male', 'Female')

df <- data.frame(name, age, gender)
print(df)
```

       name age gender
    1 Allen  20   Male
    2 Bruth  21   Male
    3 Chris  22   Male
    4 Daisy  23 Female
    


```R
# 指定唯一标识的一列作为行名
df <- data.frame(name, age, gender, row.names=name)
print(df)
```

           name age gender
    Allen Allen  20   Male
    Bruth Bruth  21   Male
    Chris Chris  22   Male
    Daisy Daisy  23 Female
    

数据框默认按照列进行选取：


```R
df[c(1,3)]
```



| # | name | gender |
| --- | --- | --- |
| **Allen** | Allen  | Male   |
| **Bruth** | Bruth  | Male   |
| **Chris** | Chris  | Male   |
| **Daisy** | Daisy  | Female |





```R
# 可以按列名选取
df[c("name", "gender")]
```



| # | name | gender |
| --- | --- | --- |
| **Allen** | Allen  | Male   |
| **Bruth** | Bruth  | Male   |
| **Chris** | Chris  | Male   |
| **Daisy** | Daisy  | Female |





```R
# 可以通过标识符 '$' 选取
print(df$age)
```

    [1] 20 21 22 23
    


```R
# 双参数时，先行后列
print(df[1:3,"gender"])
```

    [1] Male Male Male
    Levels: Female Male
    

### 临时环境：attach() 与 with()

df\$age 从语法上说很清晰，但是可读性却不高。因为我们一般总是在处理一个数据集，因此‘df’显得多余。这里可以借助 attach()/detach() 命令组：

*请注意：此命令出于容错性、可读性考虑，在任何情况下均__不建议__使用。*


```R
# 删除原有的全局变量，否则 age 会覆盖 df$age
rm(age, gender, name)

attach(df)
print(age)
detach(df)
```

    [1] 20 21 22 23
    

或者使用 with() 命令：


```R
tmp <- 1
with(df, {
    print(name)
    tmp <<- 2  # 特殊赋值符可以传值到 with() 之外
})
print(tmp)
```

    [1] Allen Bruth Chris Daisy
    Levels: Allen Bruth Chris Daisy
    [1] 2
    

### 更多内容

更多关于数据管理和 data.frame 处理的内容在本系列文章的 [数据管理]({{ site.url }}/R-manage-data.html#section-7) 一文中可以找到。
