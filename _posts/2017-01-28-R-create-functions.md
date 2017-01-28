---
layout: post
title: R语言（函数编写）
categories: R
tags: R-learning
---


本文介绍 R 中的控制语句（条件 if/switch 与循环 for/while），抛出警告与异常（stop()/warning()/message()），以及如何自编写函数、如何把编写函数放入启动环境中。

<!-- more -->

## 条件语句

### if 语句

R 中的 if 语句有三种形式：

- If (cond) state 
- If (cond) yes-state else no-state
- Ifelse (cond, yes-state, no-state)


```R
# if 语句
if (2 > 1) {
    a <- TRUE
}
print(a)
```

    [1] TRUE
    


```R
# if-else 语句
if (2 != 1) {
    a <- TRUE
} else {
    a <- False
}
print(a)
```

    [1] TRUE
    


```R
# 三元选择器：ifelse()
ifelse(2 != 1, a <- TRUE, a <- False)
```


TRUE


### switch 语句


```R
dt <- c("a", "b", "c")
for (i in dt) {
    print(switch(i, a = "A", b = "B", c = "C"))
}
```

    [1] "A"
    [1] "B"
    [1] "C"
    

## 循环语句

之前在 [“数据管理”一文]({{ site.url }}/R-manage-data.html#函数式编程批量应用函数) 中介绍过函数式编程 apply()。如果可能，请尽量使用函数式编程，而不是使用循环语句。

### for 语句

在 switch() 中已经展示了 for 语句的用法。

### while 语句


```R
i <- 0
while (i < 3) {
    print(i)
    i <- i + 1
}
```

    [1] 0
    [1] 1
    [1] 2
    

## 自编写函数

R 中的函数声明与其他语言并没有什么不同：


```R
DfSum <- function(x, is.print=FALSE) {
    # Compute the sum of all columns and put the results into SUM column.
    #
    # Args: 
    #     x: Any data.frame object.
    #     is.print: if TRUE, print the new data.frame to the screen
    #
    # Returns:
    #     A data.frame combined by the original one and the SUM column.
    if (class(x) != "data.frame") {
        stop("Require data.frame input.")
    }
    x$SUM <- apply(x, 1, sum)
    if (is.print)
        print(x)
    return(x)
}

dt <- data.frame(X=c(1:3), Y=c(4:6))
DfSum(dt)
```



| X | Y | SUM |
| --- | --- | --- |
| 1 | 4 | 5 |
| 2 | 5 | 7 |
| 3 | 6 | 9 |




## R 启动环境：Startup

我们常常把函数写在 R 文件中，然后在需要使用时用 source() 命令引用它。你可以配置 R 的相关配置文件（R 的安装目录下 etc/Rprofile.site 文件），使得你可以在任何 R 项目中方便地调用本地自编写的函数。

你可以在其中创建一个名为 .First() 的函数，作为**每个 R 会话的启动函数**。一个例子：

```{r}
.First() <- function() {
    library(Hmisc)  # 加载 Hmisc 包
    source("c:/R-files/myfunctions.R")
}
```

同理可以设置的还有关闭函数，叫做 .Last()。例如自动保存历史文件：

```{r}
.Last() <- function() {
    history.name <- paste(paste("AutoSave", Sys.Date(), strsplit(date(), " ")[[1]][4], sep="-"), ".Rhistory", sep="")
    savehistory(paste(getwd(), history.name))
}
```

## 抛出异常

你可能注意到了 stop() 函数，它在自编写函数中用于停止编译，可能会被经常用到。

- stop(): 停止执行并报错。
- warning()：错误提示。
- message()：诊断信息提示。

我们可以测试刚才编写的 DfSum 函数中使用的 stop()，输入一个不符合输入要求的参数：


```R
DfSum("abc")
```


    Error in DfSum("abc"): Require data.frame input.
    Traceback:
    

    1. DfSum("abc")

    2. stop("Require data.frame input.")   # at line 11 of file <text>

