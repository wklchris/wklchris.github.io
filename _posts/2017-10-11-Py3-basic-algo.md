---
layout: post
title: Basic Algorithms written in Python
categories: Algorithm
update: 2017-10-12
tags: Py-compute
---


This article introduces basic algorithms and their Python 3 implementation.

<!-- more -->

*__K. Wu, Oct 2017__*

## Introduction

The basic algorithms, in general, include following topics:
1. Sorting
  - Selection Sort
  - Insertion Sort
2. Searching
3. Graph Algos
4. String Algos

Let's get started. 


```python
# Import some necessary modules
import random
```

## Sorting

    
"Rearranging a sequence of objects so as to put them in some logical order" [1].
    
### Selection Sort

The basic idea of selection sort is: 
1. Find the smallest item, and exchange it with the first entry.
2. Find the smallest item in the remaining list (because the first entry has been done), and exchange it with the second entry.
3. ...

For example, we have a sequence $[1,5,7,4,3,9,8,6,2]$. I write a Python code for selection sorting:


```python
def selection_sort2(v):
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
    [1, 2, 3, 4, 5, 6, 7, 8, 9]



#### Time Complexity of Selection Sort

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
    for i in range(n):
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

    i=0, [1, 5, 7, 4, 3, 9, 8, 6, 2]
    i=1, [1, 5, 7, 4, 3, 9, 8, 6, 2]
    i=2, [1, 5, 7, 4, 3, 9, 8, 6, 2]
    i=3, [1, 4, 5, 7, 3, 9, 8, 6, 2]
    i=4, [1, 3, 4, 5, 7, 9, 8, 6, 2]
    i=5, [1, 3, 4, 5, 7, 9, 8, 6, 2]
    i=6, [1, 3, 4, 5, 7, 8, 9, 6, 2]
    i=7, [1, 3, 4, 5, 6, 7, 8, 9, 2]
    i=8, [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    [1, 2, 3, 4, 5, 6, 7, 8, 9]



#### Time Complexity of Insertion Sort

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

#### Improvement of Insertion Sort

- Shortening its inner loop to move the larger entry to the right one position (instead of doing full exchanges) will cut the number of array access in half.[1] I also write a code for it:


```python
def insertion_sort2(v):
    n = len(v)
    for i in range(n):
        t = v[i]  # temp variable
        j = i
        while j >= 1 and v[j-1] > t:  
            v[j] = v[j-1]
            j -= 1
        v[j] = t
    return(v)

# Example
a = [1,5,7,4,3,9,8,6,2]
insertion_sort2(a)
```
    [1, 2, 3, 4, 5, 6, 7, 8, 9]



An implementation when $n$ is larger, say $10000$. The first function uses $1.6\,\mu\mathrm{s}$, while the second one uses $2.2\,\mu\mathrm{s}$. 

*__Note: The improved code is nearly 4 times faster that an ugly code ($6.5\,\mu\mathrm{s}$) like below! Write better code please.__*

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

[1] Robert Sedgewick, Kevin Wayne. *Algorithms (4th Edition)*. 2011
