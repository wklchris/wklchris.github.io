---
layout: post
title: JavaScript 语法速记
categories: Web
tags: JavaScript
---

本文是我学习 JavaScript 的笔记。

<!-- more -->

# 执行与测试

## 执行

执行JavaScript有两种方式。第一种方式，是把 JavaScript 放在 `<script>...</script>` 标签对中。通常在 `header` 块中加载：

```html
<html>
<head>
    <script>alert("This is so called JavaScript!")</script>
</head>
...
<html>
```

另一种方式是通过文件调用：

```html
<html>
<head>
    <script src="/js/hello.js"></script>
</head>
...
<html>
```

显然，第二种方式更有利于维护和代码复用。

## 测试

如何在页面上测试 JavaScript 代码呢？比如 Chrome 浏览器，通过右键单击网页空白处，选择“审查元素(Inspect)”（或者直接按 F12 ），在弹出面板中切换到“控制台(Console)”选项卡，即可直接输入 JavaScirpt 代码。

你可以将上一小节中提到的 `alert` 命令输入到控制台中进行测试。其执行结果会弹出一个包含相应文字的提示窗口。本文中的所有 JavaScript 示例，读者都可以通过这种方式进行测试。

# 语法

## 基础

标准的 JavaScript 语句以分号 `;` 结尾，通过花括号组 `{...}` 来表示代码块，通过 `//` 和 `/*...*/` 分别进行行尾和多行注释。总体来说，语法类似于 Java 语言。

一个例子：
```javascript
var a = 1;
if (a < 0) {
    alert("Negative.") // Comments here
} else {
    alert("Non-negative.")
}
```

## 数据类型

JavaScript 中，合法的变量名由英文、数字、下划线 `_` 和美元符 `$` 组成，且不能以数字开头。通过 `var` 关键字引导一个声明语句。

### 数字 number

JavaScript 在数字下不再细分整型和浮点型。下面是一些特殊的数字：

```javascript
1.024e6;  // 科学计数法
0xff      // 十六进制数
NaN;      // Not a Number，非合法数。比如 1/0 的结果
Infinity; // 无穷
```

加减乘除运算不再赘述。取余是 `%` 。

如果要判断一个数是否是 `NaN` ，使用 `isNaN()` 函数。

### 字符串及其格式化

字符串用单引号或者双引号包围。需要转义的字符前加 `\` 符号即可：
```javascript
'Glad to meet you. I\'m Mr.Smith.'
```

其他例子：
```javascript
"\x4A";   // 显示"J"，其中"4A"是十六进制的 ASCII 码
"\u4e34"; // 显示"临"，这是汉字的 Unicode 编码
`Multi-
line`     // 多行字符，用重音符包围。从ES6标准开始支持 
```

字符串是**不可修改的**，对字符串的某位进行赋值操作是无效的。

下面是一些字符串的函数：
```javascript
s.substring(2, 3); // 返回[2,3)下标之间的子字符串
s.substring(3);    // 返回从3到末尾的子字符串
s.toUpperCase();   // 将字符串s变为全大写
s.toLowerCase();   // 将字符串s变为全小写
s.indexOf("abc");  // 搜索"abc"首次在s中出现的位置。若无，返回 -1
```

字符串格式化使用重音符和美元符来实现：
```javascript
var a = 1;
var b = "example";
var r = `This is ${a} brief ${b}.` // 注意是重音号
console.log(r); // 显示变量的值
```

### 布尔值

全小写的 `true` 和 `false` 表示布尔值。与或非运算分别是 `&&` , `||` 和 `!` 。

判断两个对象是否全等，使用三连等号 `===`。注意：如果使用双连等号，JavaScript 会自动转换数据类型以便于比较 —— 这往往是我们不需要的。所以，**请总是使用三连等号。**

浮点数的比较可能产生精度问题，所以可以借用 `Math.abs()` 和一个足够小的正数来判断两个浮点数是否相等：

```javascript
Math.abs(a - b) < 1e-8;
```

### 数组

JavaScript 的数组可以包含多种数据类型，包括子数组：
```javascript
[1, "Hello", false, [1, 2]];
```

调用与其他语言一样，例如 `a[0]` 表示数组 a 的第一个元素。

数组的一些操作方法：
```javascript
arr.length;  // 数组长。若给其赋值，会改变数组长度。扩展的数组会用 undefined 填充空位
arr.slice(0,3);  // 数组[0,3)下标之间的子数组切片
arr.concat(1, arr2);// 返回一个组合了数组 arr, 元素 1 与 数组 arr2 的新数组
arr.push(3, 4);  // 向数组尾添加两个元素 3 和 4
arr.pop();       // 从数组尾返回元素并将其删除
arr.shift();     // 从数组头返回元素并将其删除
arr.unshift(2);  // 向数组头添加元素 2
arr.splice(1, 2, "a");  // 从下标1处pop两个元素，再插入元素 "a"
arr.sort();      // 将数组排序（默认升序） 
arr.indexOf(12); // 搜索数字元素12首次出现的位置
arr.join(".");   // 用点号依次连接数组元素，返回字符串
arr.reverse();   // 反转数组
```

### 字典（对象）

与 Python 类似，JavaScript 的字典类型通过键值对的方式表示：
```javascript
var a = {
    id: 0001,
    text: "Hello world"
};  // 注意这里的分号
```

通过 `a.text` 或者 `a["text"]` 的方式调用字典中的值。其他操作：
```javascript
var p = {
    id: 001,
    name: "Chris",
    age: 3,
    isMale: true
};
delete p.id;  // 删除一个属性
"id" in p;  // 被删除的属性不再位于p的键中
p.hasOwnProperty("toString"); // 判断一个属性是否是继承得到
```

### 哈希 Map

在 ES6 标准之后，JS 开始使用 Map ，即哈希。它用来应对字典中键是非字符串的情况，一般认为查找时间是常数的。

```javascript
var m = new Map([["a", 123], ["b", 37], ["d", 52]]);
m.get("a");      // 返回键"a"对应的值，无则返回 undefined
m.set("c", 19);  // 添加一组新的键值对
m.has("e");      // 是否存在键"e"
m.delete("a");   // 删除键"a"
```

### 集合

集合同样是 ES6 标准后才支持，其元素不能重复。

```javascript
var s = new Set([1, 2, 4]);
s.add(3);    // 若元素重复，则无效果
s.delete(1); // 删除元素
```

### 空值

全小写的 `null` 表示空，相当于 Python 中的 None. 

还有一个 `undefined`， 表示一个未定义的值，只在少数情况（比如传参）下使用。例如：

```javascript
var b = [1, , 2, 3];
b[1]; // 显示 undefined
b[1] === undefined; // true
b[1] === null;      // false
```

## 判断和循环

### If 语句

```javascript
var a = 2;
if (a > 1) {
    alert("L");
} else if (a < 1) {
    alert("S");
} else {
    alert("Equal");
}
```

### for / forEach 语句

简单的 for 语句：
```javascript
var s = 0;
for (i=1; i<=100; i++) {
    s += i;
}
s; // 5050
```

for 语句配合 in 关键字，可以遍历字典的键（注意：如果对数字操作，得到的也是字符串，这个用下文的 for...of/forEach 解决）。

```javascript
var d = {
    name: "Chris",
    age: 100
}
for (var k in d) {
    console.log(k);
}  // 输出 "name", "age"
```

ES6 标准支持 for..of，不过作用对象是 iterable 类型的三种对象：数组 Array，哈希 Map，以及集合 Set. 
```javascript
var arr = [1, 2, 3, 4];
var m = new Map([["a", 1], ["b", 4]]);
var s = new Set([1, 2, 5, 7]);
var f = function (data) {
    for (var i of data) {
        console.log(i);
    }
};
f(arr);
f(m);
f(s);
```

forEach 则是另一种方法：
```javascript
arr.forEach(function(element, index, array) {
    console.log(`Arr[${index}] = ${element}`);
});  // Array 如果不关心 index 和 array，参数可省略。
m.forEach(function(value, key, map) {
    console.log(`Map["${key}"] = ${value}`);
});  // Map 用“键-值”代替“下标-元素”
s.forEach(function(ele1, ele2, set) {
    console.log(`Set(${ele1})`);
});  // Set 没有索引，前两个参数均为元素。因此后两个参数可省略。
```

### while 语句

```javascript
var i = 0;
var s = 0;
var w = 0;
while (s <= 100) {
    s += i;
    i++;
}
s; // 105
```

## 函数

在 for...of 的例子中，已经尝试着定义过一个函数。函数的定义有两种写法：一种是`var f = function(args) {...};`，而另一种则是 `function f(args) {...}`。注意分号的使用。