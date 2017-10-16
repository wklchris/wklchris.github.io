---
layout: post
title: Basic Algorithms written in Python
categories: Algorithm
update: 2017-10-16
tags: Py-compute
---


This article introduces basic algorithms and their Python 3 implementation. 

<!-- more -->

*__K. Wu, Oct 2017__*

## Introduction

The basic algorithms, in general, include following topics (sections with '\*' are optional):
- Basic Algorithm Thought
  - Recursion & Divide-and-Conquer
  - Induction
  - Reduction\*
- Sorting
  - Selection Sort
  - Insertion Sort
- Searching
- Graph Algos
- String Algos

Let's get started. 


```python
# Import some necessary modules
import random
%load_ext line_profiler
```

## Basic Algorithm Thought

Before learning a specific algorithm, we need to know how algorithms are developed. 

### Recursion & Divide-and-Conquer

Recursion is not often used in daily life. I think that's because in most cases, we use this kind of method without knowing its name.

> **[Example]** To merge two sorted poker card piles into a single sorted one[1]. 

What should we do? Our common sense might be to choose the smaller card from the top of these two piles, then add the card to the tail of the output pile. Repeat this step for 52 times and we get the output pile, which is also sorted. 

> **[Parent Example]** To sort a card pile.

Inspired by the thought above, we can divide the card pile into two sub-piles, and sort them respectively (which is called *merge sort*). Imagine that we have a basic sort method "basic_sort" that can sort small (say number of cards $<n$) sequence fast. Then we only need another method called "merge" to help us merge piles into a whole one. 

```
# pseudocode
sort(inputpile):
   if (size of inputpile >= n):
     subpile_top = sort(top half of the inputpile)
     subpile_bottom = sort(bottom half of the inputpile)
     return merge(subpile_top, subpile_bottom)
   else:
     return basic_sort(inputpile)
```

This "sort" method we defined will only use "basic_sort" to sort the input pile when its size is smaller than $n$. Otherwise, it will split the pile into halves, and use these two halves as new input for the "sort" function. So the whole pile is **divided** into a number of sort problems within size of $n$, **conquered** respectively and then **combined** together to return a sorted pile.

This is a basic recursion function. This kind of solution is called "Divide and conquer". 

***

Recursion also can be used in many other cases, such as calculating the factorial:


```python
def recur_factorial(n):
    return 1 if n==1 else n*recur_factorial(n-1)

recur_factorial(4)  # 4! = 4 x 3 x 2 x 1 = 24
```
    24



### Induction

Induction is used in many occasions that needs inferences. We may all do sequence homework before like below:

> **[Example]** Prove that $f(n)=1+2+3+\cdots+n=\dfrac{n(n+1)}{2}, n\in N*$.

Although we know that Mr. Gauss solved this problem many years ago, it's still a good example of induction. 

Once you infer a possible form, say $\frac{n(n+1)}{2}$ here, of the summation, you should think about how to prove it. We can easily show it's correct when $n=1, 2, 3$, but we cannot enumerate all the integers. Therefore, an induction method is needed:
1. Show that it's correct in a basic case.  
  > When $n=1$, the left side equals 1, the right side is $\frac{1\times 2}{2}=1$. So it's true when $n=1$.
2. Show that when the previous case is true, then current case is guaranteed to be true.
  > For any given $n$, if $f(n)=\dfrac{n(n+1)}{2}$ is true, then:  
  > $$f(n+1) = \dfrac{n(n+1)}{2} + (n+1) = \dfrac{(n+1)(n+2)}{2}$$ 
  > so it's also true for $n+1$ case.
3. QED. 
  > So it's true for all $n\in N*$.

What a sharp contrast with dive-and-conquer thought. Two totally different thoughts but both are widely applied.

### Reduction\*

Sometimes we may hear "reduction", but it's far from "induction".

Roughly speaking, reduction is a thought to estimate the complexity or find a solution of a new problem. If the new problem is similar to an existing one, it might also have a similar complexity. If there has already been a solution for the existing one, the solution probably also works for the new problem.

## Sorting
    
"Rearranging a sequence of objects so as to put them in some logical order" [2].
    
### Selection Sort

The basic idea of selection sort is: 
1. Find the smallest item, and exchange it with the first entry.
2. Find the smallest item in the remaining list (because the first entry has been done), and exchange it with the second entry.
3. ...

For example, we have a sequence $[1,5,7,4,3,9,8,6,2]$. I write a Python code for selection sorting:


```python
def selection_sort(v):
    n = len(v)
    for i in range(n):
        minidx = i
        j = i + 1
        while j < n and v[j] < v[minidx]:
            minidx = j
            j += 1
        v[i], v[minidx] = v[minidx], v[i]
    return(v)

# Example
a = [1,5,7,4,3,9,8,6,2]
selection_sort(a)
```
    [1, 5, 3, 4, 7, 2, 6, 8, 9]



**Time Complexity of Selection Sort**

There are 1 exchange and $n-i-1$ comparations in each outer loop, so its time complexity for selection sort is:

$$ T \approx \sum_{i=1}^n \left(1 + \sum_{j=i+1}^n 1\right) = \sum_{i=1}^n (n-i) = \frac{n(n-1)}{2} \textrm{ (fixed time)}$$

- **Running time of selection sort is only related to $n$**. Even the list has been already sorted, its running time won't decrease. For example, the selection sort running time of lists $a$ and the corresponding sorted list are respectively $8.35\,\mu\mathrm{s}$ and $8.37\,\mu\mathrm{s}$, nearly the same.

### Insertion sort

Of course, selection sort is an inefficient algorithm. It can not even handle a sorted list in short time. 

Recall the method we use when playing poker. How do we sort cards in our hand? Generally, we would begin from the leftmost to the rightmost, pull it out and insert it into the sorted sequence at its left side.

We use the same list for our Python code:


```python
def insertion_sort(v):
    n = len(v)
    for i in range(1, n):
        j = i
        while j >= 1 and v[j-1] > v[j]:  
            v[j], v[j-1] = v[j-1], v[j]
            j -= 1
        print("i={}, {}".format(i, v))
    return(v)

# Example
a = [1,5,7,4,3,9,8,6,2]
insertion_sort(a)
```

    i=1, [1, 5, 7, 4, 3, 9, 8, 6, 2]
    i=2, [1, 5, 7, 4, 3, 9, 8, 6, 2]
    i=3, [1, 4, 5, 7, 3, 9, 8, 6, 2]
    i=4, [1, 3, 4, 5, 7, 9, 8, 6, 2]
    i=5, [1, 3, 4, 5, 7, 9, 8, 6, 2]
    i=6, [1, 3, 4, 5, 7, 8, 9, 6, 2]
    i=7, [1, 3, 4, 5, 6, 7, 8, 9, 2]
    i=8, [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    [1, 2, 3, 4, 5, 6, 7, 8, 9]



**Time Complexity of Insertion Sort**

In each $i$-loop, there are $i-1$ comparations and $i-1$ exchanges (when worst). The time complexity:

$$
\begin{align*}
T_{\mathrm{worst}} \approx& \sum_{i=1}^n \left(\sum_{j=n}^{i-1} 1+1 \right) = 2\sum_{i=1}^n (i-1) = n(n-1) \\
T_{\mathrm{best}} =& (n-1) + 0 = n-1 \\
T_{\mathrm{average}} =& n(n-1)/2
\end{align*}
$$

So usually it's a $\Theta(n^2)$ sort method. In average cases (when there's no identical sort keys), insertion sort are twice as fast as selection sort.

*__Note: For partially sorted array, insertion sort can be high efficient.__*

An implementation when $n$ is larger, say $10000$. We can use `%lprun` to get a running time report in Jupyter Notebook:
```python
a=list(range(10000))
random.shuffle(a)

# %load_ext line_profiler
%lprun -f insertion_sort insertion_sort(a)
```

Result:
```
Timer unit: 3.95062e-07 s

Total time: 0.0136407 s
File: <ipython-input-4-167f22c9477e>
Function: insertion_sort at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def insertion_sort(v):
     2         1            4      4.0      0.0      n = len(v)
     3     10000         8979      0.9     26.0      for i in range(1, n):
     4      9999         9330      0.9     27.0          j = i
     5      9999        16213      1.6     47.0          while j >= 1 and v[j-1] > v[j]:  
     6                                                       v[j], v[j-1] = v[j-1], v[j]
     7                                                       j -= 1
     8         1            2      2.0      0.0      return(v)
```

*__Note: A good code (14 units) is nearly 4 times faster than an ugly code (65 units) like below! Write better code please.__*

    # UGLY CODE!
    def insertion_sort(v):
        n = len(v)
        for i in range(n):
            j = 1
            for j in reversed(range(i-1)):
                if v[j] < v[j-1]:
                    v[j], v[j-1] = v[j-1], v[j]
                else:
                    break
        return(v)

## Reference

[1] Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein. *Introduction to Algorithms (3rd Edition)*. 2009.  
[2] Robert Sedgewick, Kevin Wayne. *Algorithms (4th Edition)*. 2011. 
