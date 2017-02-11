---
layout: post
title: R语言（描述性统计）
categories: R
tags: R-learning
---


本文展示了 R 语言中描述性统计相关的内容。

<!-- more -->

## 描述性统计

最简单的是 summary() 函数，给出数值变量的的最值、四分位值、中位数（这五个又称为五位数总括，可以用 fivenum() 函数单独调用），以及均值；非数值变量的频数统计。


```R
dt <- data.frame(x=c(seq(1, 3), seq(2, 4), seq(4, 6))) 
dt$y <- dt$x + 1
dt$f <- as.factor(rep(c(1, 2, 3), 3))
dt
```



| x | y | f |
| --- | --- | --- |
| 1 | 2 | 1 |
| 2 | 3 | 2 |
| 3 | 4 | 3 |
| 2 | 3 | 1 |
| 3 | 4 | 2 |
| 4 | 5 | 3 |
| 4 | 5 | 1 |
| 5 | 6 | 2 |
| 6 | 7 | 3 |





```R
summary(dt)
```


           x               y         f    
     Min.   :1.000   Min.   :2.000   1:3  
     1st Qu.:2.000   1st Qu.:3.000   2:3  
     Median :3.000   Median :4.000   3:3  
     Mean   :3.333   Mean   :4.333        
     3rd Qu.:4.000   3rd Qu.:5.000        
     Max.   :6.000   Max.   :7.000        



```R
print(fivenum(dt$x))
```

    [1] 1 2 3 4 6
    

在 [这篇文章]({{ site.url }}/R-manage-data.html#%E6%95%B4%E5%90%88aggregate) 中介绍了利用 aggregate() 函数对二维数据进行分组统计的方法。不过该函数只能调用单返回值的统计函数，如果要调用多返回值的，请使用 by() 函数：


```R
mystats <- function(x) {
    return(c(Min=min(x), Max=max(x)))
}
# 分别统计列 x 与 列 y 中在 f 列各水平下的最值
by(dt[,c("x","y")], dt$f, function(data) sapply(data, mystats))
```


    dt$f: 1
        x y
    Min 1 2
    Max 4 5
    ------------------------------------------------------------ 
    dt$f: 2
        x y
    Min 2 3
    Max 5 6
    ------------------------------------------------------------ 
    dt$f: 3
        x y
    Min 3 4
    Max 6 7


### 频数表

函数 table() 与 prop.table() 分别统计频数或频率：


```R
print(list(table(dt$x), round(prop.table(dt$x), digits=2)))
```

    [[1]]
    
    1 2 3 4 5 6 
    1 2 2 2 1 1 
    
    [[2]]
    [1] 0.03 0.07 0.10 0.07 0.10 0.13 0.13 0.17 0.20
    
    

此外，如果要制作二维列联表，使用 table(A, B) 或者 xtabs(~ A + B, data=) 函数。其中 A 是行， B是列。


```R
tmp <- data.frame(x=c(1, 2, 2, 3, 3), y=c(2, 3, 4, 3, 2))
ct <- xtabs(~x+y, data=tmp)
ct
```


       y
    x   2 3 4
      1 1 0 0
      2 0 1 1
      3 1 1 0



```R
# 为列联表添加边际和；也可以通过 addmargins(ct, 1/2) 只累加列/行
addmargins(ct)
```



| # | 2 | 3 | 4 | Sum |
| --- | --- | --- | --- | --- |
| **1** | 1 | 0 | 0 | 1 |
| **2** | 0 | 1 | 1 | 2 |
| **3** | 1 | 1 | 0 | 2 |
| **Sum** | 2 | 2 | 1 | 5 |




边际频数使用 margin.table() 进行计算，比例使用 prop.table() 进行计算。参数 1 表示行，2 表示列。


```R
# 行内总计（每行累加）
margin.table(ct, 1)
```


    x
    1 2 3 
    1 2 2 



```R
# 行内比例（每行累加为 1）
prop.table(ct, 1)
```


       y
    x     2   3   4
      1 1.0 0.0 0.0
      2 0.0 0.5 0.5
      3 0.5 0.5 0.0


### 独立性检验：卡方

这里介绍卡方 $\chi^2$ 独立性检验。本例中，p = 0.44 > 0.05，接受了相互独立的假设，即认为它们是独立的。


```R
chisq.test(ct)
```

    Warning message in chisq.test(ct):
    "Chi-squared approximation may be incorrect"


    
    	Pearson's Chi-squared test
    
    data:  ct
    X-squared = 3.75, df = 4, p-value = 0.4409
    

