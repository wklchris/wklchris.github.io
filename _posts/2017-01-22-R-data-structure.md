---
layout: post
title: R语言学习与速查（数据结构）
categories: R
tags: R-learning
---


本节介绍 R 的数据类型，包括 data.frame 与实用的 attach()/with() 命令。

## 数据类型

R 中包含的数据类型有：

- 数值；以及复数
- 字符
- 逻辑（TRUE/FALSE)
- 字节

对于一般的二维数据集，其行与列在不同领域的称呼不同：

| 领域 | 行 | 列 |
| --- | --- | --- |
| 统计学（本文） | 观测(observation) | 变量(variable) |
| 数据库 | 记录(record) | 字段(field) |
| 数据挖掘/机器学习 | 示例(example) | 属性(attribute) |

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
# matr <- matrix(vector, nrow=N, ncol=N, byrow=T/F, [dimnames=list(rownamestr,colnamestr)])

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

arr <- array(1:24, c(2, 3, 4), dimnames=list(c('A1', 'A2'), c('B1', 'B2','B3'), c('C1', 'C2', 'C3', 'C4')))
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
    
    

### 数据框：data.frame

数据框是多个等长向量的按列堆叠。这是 R 中最常用的数据结构。


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
    

#### 临时环境：attach() 与 with()

df\$age 从语法上说很清晰，但是可读性却不高。因为我们一般总是在处理一个数据集，因此‘df’显得多余。这里可以借助 attach()/detach() 命令组：


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
    
