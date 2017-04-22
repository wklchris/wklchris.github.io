---
layout: post
title: R语言（常用函数与数据管理）
categories: R
update: 2017-04-22
tags: R-learning
---


本节内容可应用在数据读取之后。包括基本的运算（包括统计函数）、数据重整（排序、合并、子集、随机抽样、整合、重塑等）、字符串处理、异常值（NA/Inf/NaN）处理等内容。也包括 apply() 这种函数式编程函数的使用。

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
    

### 基本数学函数

- 绝对值：abs()
- 平方根：sqrt()
- 三角函数：sin(), cos(), tan(), acos(), asin(), atan()
- 对数：
    - log(x, base=n) 以 n 为底 x 的对数
    - log10(x) 以 10 为底的对数
- 指数：exp()
- 取整：
    - 向上取整 ceiling()
    - 向下取整 floor()
    - 舍尾取整（绝对值减小） trunc()
    - 四舍五入到第 N 位 round(x, digits=N)
    - 四舍五入为有效数字共 N 位 singif(x, digits=N)

### 统计、概率与随机数

描述性统计等更多的统计内容，参考 [“描述性统计”一文]({{ site.url }}/R-descriptive-statistics.html)。

#### 统计函数

常用的统计函数：

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

#### 概率函数

常用的概率分布函数：

- 正态分布：norm
- 泊松分布：pois
- 均匀分布：unif
- Beta 分布：beta
- 二项分布：binom
- 柯西分布：cauchy
- 卡方分布：chisq
- 指数分布：exp
- F 分布：f
- t 分布：t
- Gamma 分布：gamma
- 几何分布：geom
- 超几何分布：hyper
- 对数正态分布：lnorm
- Logistic 分布：logis
- 多项分布：multinom
- 负二项分布：nbinom

以上各概率函数的缩写记为 *abbr*, 那么对应的概率函数有：

1. **密度函数**： d{abbr}()，例如对于正态就是 dnorm()
2. **分布函数**：p{abbr}()
3. **分位数函数**：q{abbr}()
4. **生成随机数**：r{abbr}()，例如常用的 runif() 生成均匀分布

#### 例子

通过 runif() 产生 $[0, 1]$ 上的服从均匀分布的伪随机数列。通过 set.seed() 可以指定随机数种子，使得代码可以重现。不过**作用域只有跟随其后的那个随机数函数。**


```R
set.seed(123)
print(runif(3))
```

    [1] 0.2875775 0.7883051 0.4089769
    


```R
# 位于 1.96 左侧的标准正态分布曲线下方的面积
pnorm(1.96)
```


0.97500210485178



```R
# 均值为500，标准差为100 的正态分布的0.9 分位点
qnorm(.9, mean=500, sd=100)
```


628.15515655446



```R
# 生成 3 个均值为50，标准差为10 的正态随机数
set.seed(123)
print(rnorm(3, mean=50, sd=10))
```

    [1] 44.39524 47.69823 65.58708
    

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

## 字符串处理

R 中的字符串处理函数有以下几种：

### 通用函数

| 函数 | 含义 |
| --- | --- |
| nchar(x) | 计算字符串的长度 |
| substr(x, start, stop) | 提取子字符串 |
| grep(pattern, x, ignore.case=FALSE, fixed=FALSE) | 正则搜索，返回为匹配的下标。如果 fixed=T，则按字符串而不是正则搜索。 |
| grepl() | 类似 grep()，只不过返回值是逻辑值向量。 |
| sub(pattern, replacement, x, ignore.base=FALSE, fixed=FALSE) | 在 x 中搜索正则式，并以 replacement 将其替换。如果 fixed=T，则按字符串而不是正则搜索 |
| strsplit(x, split, fixed=FALSE) | 在 split 处分割字符向量 x 中的元素，返回一个列表。 |
| paste(x1, x2, ..., sep="") | 连接字符串，连接符为 sep。也可以连接重复字串：`paste("x", 1:3, sep="")` |
| toupper(x) | 转换字符串为全大写 |
| tolower(x) | 转换字符串为全小写 |

一些例子。首先是正则表达式的使用：


```R
streg <- c("abc", "abcc", "abccc", "abc5")
re1 <- grep("abc*", streg)
re2 <- grep("abc\\d", streg)  # 注意反斜杠要双写来在 R 中转义
re3 <- sub("[a-z]*", "Hey", streg)
re4 <- sub("[a-z]*\\d", "NEW", streg)

print(list(re1, re2, re3, re4))
```

    [[1]]
    [1] 1 2 3 4
    
    [[2]]
    [1] 4
    
    [[3]]
    [1] "Hey"  "Hey"  "Hey"  "Hey5"
    
    [[4]]
    [1] "abc"   "abcc"  "abccc" "NEW"  
    
    

然后是字符串分割与连接。注意这里的 paste() 有非常巧妙的用法：


```R
splt <- strsplit(streg, "c")  # 结果中不含分隔符 "c"
cat1 <- paste("a", "b", "c", sep="-")
cat2 <- paste("x", 1:3, sep="")  # 生成列名时非常有用

print(list(splt, cat1, cat2))
```

    [[1]]
    [[1]][[1]]
    [1] "ab"
    
    [[1]][[2]]
    [1] "ab" ""  
    
    [[1]][[3]]
    [1] "ab" ""   ""  
    
    [[1]][[4]]
    [1] "ab" "5" 
    
    
    [[2]]
    [1] "a-b-c"
    
    [[3]]
    [1] "x1" "x2" "x3"
    
    

### 日期型字符串

与其他类型相似，日期型字符串能够通过 as.Date() 函数处理。各格式字符的含义如下：

| 符号 | 含义 | 通用示例 | 中文示例 |
| --- | --- | --- | --- |
| %d | 日（1~31） | 22 | 22 |
| %a | 缩写星期 | Mon | 周一 |
| %A | 全写星期 | Monday | 星期一 |
| %m | 月（1~12） | 10 | 10 |
| %b | 缩写月 | Jan | 1月 |
| %B | 全写月 | January | 一月 |
| %y | 两位年 | 17 | 17 |
| %Y | 四位年 | 2017 | 2017 |


```R
# 对字符串数据 x，用法：as.Date(x, format=, ...)
dates <- as.Date("01-28-2017", format="%m-%d-%Y")
print(dates)
```

    [1] "2017-01-28"
    

要想获得当前的日期或时间，有两种格式可以参考，并可以用 format() 函数辅助输出。


```R
# Sys.Date() 返回一个精确到日的标准日期格式
dates1 <- Sys.Date()
format(dates1, format="%A")  # 可以指定输出格式
```


'星期六'



```R
# date() 返回一个精确到秒的详细的字串
dates2 <- date()
dates2
```


'Sat Apr 22 15:30:54 2017'


函数 difftime() 提供了计算时间差的方式。其中计量单位可以是以下之一："auto", "secs", "mins", "hours", "days", "weeks"。

截至本文最后更新，我有 1100+ 周大。唔……这好像听起来没什么感觉


```R
dates1 <- as.Date("1994-11-23")
dates2 <- Sys.Date()
difftime(dates2, dates1, units="weeks")
```


    Time difference of 1169.429 weeks


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




## 整合与重构

### 转置

常见的转置方法是 t() 函数：


```R
df = matrix(1:6, nrow=2, ncol=3)
t(df)
```




| 1 | 2 |
| 3 | 4 |
| 5 | 6 |




### 整合：aggregate()

这个函数是非常强大的。语法：

    aggregate(x, by=list(), FUN)
    
其中 x 是待整合的数据对象，by 是分类依据的列，FUN 是待应用的标量函数。


```R
# 这个例子改编自 R 的官方帮助 aggregate()
df <- data.frame(v1 = c(1,3,5,7,8,3,5,NA,4,6,7,9),
                     v2 = c(11,33,55,77,88,33,55,NA,44,55,77,99) )
by1 <- c("red", "blue", 1, 2, NA, "big", 1, 2, "red", 1, NA, 12)
by2 <- c("wet", "dry", 99, 95, NA, "damp", 95, 99, "red", 99, NA, NA)

# 按照 by1 & by2 整合原数据 testDF
# 注意(by1, by2)=(1, 99) 对应 (v1, v2)=(5, 55) 与 (6,55) 两条数据
# 因此第三行的 v1 = mean(c(5, 6)) = 5.5
aggregate(x = df, by = list(b1=by1, b2=by2), FUN = "mean")
```



| b1 | b2 | v1 | v2 |
| --- | --- | --- | --- |
| 1    | 95   | 5.0  | 55   |
| 2    | 95   | 7.0  | 77   |
| 1    | 99   | 5.5  | 55   |
| 2    | 99   |  NA  | NA   |
| big  | damp | 3.0  | 33   |
| blue | dry  | 3.0  | 33   |
| red  | red  | 4.0  | 44   |
| red  | wet  | 1.0  | 11   |





```R
# 用公式筛选原数据的列，仅整合这些列
# 注意：v1中的一个含 NA 的观测被移除
aggregate(cbind(df$v1) ~ by1+by2, FUN = "mean")
```



| by1 | by2 | V1 |
| --- | --- | --- |
| 1    | 95   | 5.0  |
| 2    | 95   | 7.0  |
| 1    | 99   | 5.5  |
| big  | damp | 3.0  |
| blue | dry  | 3.0  |
| red  | red  | 4.0  |
| red  | wet  | 1.0  |




还有一个强大的整合包 reshape2，这里就不多介绍了。

## 函数式编程：apply 函数族

函数式编程是每个科学计算语言中的重要内容；操作实现的优先级依次是**矢量运算（例如 df+1）、函数式书写，最后才是循环语句**。在 R 中，函数式编程主要是由 apply 函数族承担。R 中的 apply 函数族包括：

- apply()：指定轴向。传入 data.frame，返回 vector.
- tapply()：
- vapply()：
- lapply()：
- sapply()：
- mapply()：
- rapply()：
- eapply()：

下面依次介绍。

### apply()：指定多维对象的轴

在 R 中，通过 apply() 可以将函数运用于多维对象。基本语法是：

    apply(d, N, FUN, ...)

其中，N 用于指定将函数 FUN 应用于数据 d 的第几维（1为行，2为列）。省略号中可以传入 function 的参数。


```R
df <- data.frame(x=c(1, 2, 3), y=c(5, 4, 2), z=c(8, 6, 9), s=c(3, 7, 4))
df
```



| x | y | z | s |
| --- | --- | --- | --- |
| 1 | 5 | 8 | 3 |
| 2 | 4 | 6 | 7 |
| 3 | 2 | 9 | 4 |





```R
# 计算 df 各列的中位数
colmean <- apply(df, 2, median)
# 计算 df 各行的 25 分位数
rowquan <- apply(df, 1, quantile, probs=.25)

print(list(colmean, rowquan))
```

    [[1]]
    x y z s 
    2 4 8 4 
    
    [[2]]
    [1] 2.50 3.50 2.75
    
    

### lapply()：列表式应用

lapply 函数的本意是对 list 对象进行操作。返回值是 list 类型。


```R
lst <- list(a=c(0,1), b=c(1,2), c=c(3,4))
lapply(lst, function(x) {sum(x^2)})
```


<dl>
	<dt>$a</dt>
		<dd>1</dd>
	<dt>$b</dt>
		<dd>5</dd>
	<dt>$c</dt>
		<dd>25</dd>
</dl>



但同样可以作用于 DataFrame 对象的各个列（因为 DataFrame 对象是类似于各列组成的 list）：


```R
lapply(df, sum)
```


<dl>
	<dt>$x</dt>
		<dd>6</dd>
	<dt>$y</dt>
		<dd>11</dd>
	<dt>$z</dt>
		<dd>23</dd>
	<dt>$s</dt>
		<dd>14</dd>
</dl>



### sapply()/vapply()：变种 lapply()

sapply() 实质上是一种异化的 lapply()，返回值可以转变为 vector 而不是 list 类型。 


```R
class(sapply(lst, function(x) {sum(x^2)}))
class(lapply(lst, function(x) {sum(x^2)}))
```


'numeric'



'list'



```R
print(sapply(df, sum))
```

     x  y  z  s 
     6 11 23 14 
    

参数 simplify=TRUE 是默认值，表示返回 vector 而不是 list。如果改为 FALSE，就退化为 lapply() 函数。


```R
sapply(df, sum, simplify=FALSE)
```


<dl>
	<dt>$x</dt>
		<dd>6</dd>
	<dt>$y</dt>
		<dd>11</dd>
	<dt>$z</dt>
		<dd>23</dd>
	<dt>$s</dt>
		<dd>14</dd>
</dl>



vapply() 函数可以通过 FUN.VALUE 参数传入行名称，但这一步往往可以借助 lapply()/sapply() 加上外部的 row.names() 函数完成。

### mapply()：多输入值的应用

mapply() 函数支持多个输入值：

    mapply(FUN, [input1, input2, ...], MoreArgs=NULL)
    
其中各 input 的**长度应该相等或互为整数倍数**。该函数的用处在于避免了事先将数据合并。


```R
print(mapply(min, seq(0, 2, by=0.5), -2:7))
```

     [1] -2.0 -1.0  0.0  1.0  2.0  0.0  0.5  1.0  1.5  2.0
    

### tapply()：分组应用

tapply() 函数可以借助 factor 的各水平进行分组，然后进行计算。类似于 group by 操作：

    tapply(X, idx, FUN)

其中 X 是数据，idx 是分组依据。


```R
df <- data.frame(x=1:6, groups=rep(c("a", "b"), 3))
print(tapply(df$x, df$groups, cumsum))
```

    $a
    [1] 1 4 9
    
    $b
    [1]  2  6 12
    
    

其他的 apply() 函数很少用到，在此就不介绍了。

## 其他实用函数

在本系列的 [“数据读写操作”一文]({{ site.url }}/R-read-data.html#section) 中，也介绍了一些实用的函数，可以参考。

此外还有：

| 函数 | 含义 |
| --- | --- |
| seq(from=N, to=N, by=N, [length.out=N, along.with=obj]) | 生成数列。参数分别是起、止、步长、数列长、指定数列长度与某对象等长。 |
| rep(x, N) | 重复组合。比如 rep(1:2, 2) 会生成一个向量 c(1, 2, 1, 2) |
| cut(x, N, [ordered_result=F]) | 分割为因子。 将连续变量 x 分割为有 N 个水平的因子，可以指定是否有序。 | 
| pretty(x, N) | 美观分割。将连续变量 x 分割为 N 个区间（N+1 个端点），并使端点为取整值。 绘图中使用。|
| cat(obj1, obj2, ..., [file=, append=]) | 连接多个对象，并输出到屏幕或文件。 |
