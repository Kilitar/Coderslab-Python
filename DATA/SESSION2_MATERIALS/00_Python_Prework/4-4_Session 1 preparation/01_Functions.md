# Functions

Type: Article

From this article you will learn why you should create functions and how they improve the quality of your code.

## Introduction

Some problems/tasks are always solved the same way. An example of this is checking the correctness of the Polish national id number: PESEL - it doesn't matter whether you do it in a web application form or in a data validation script in an Excel sheet. The pattern is identical: you add PESEL to the appropriate function, and the function returns `True` or `False`. At the same time, you don't need to know how such a function works; even if you are the author of the function, the moment it is finished and works properly, you can stop bothering with its technical details.

Another advantage is the improvement of code readability. A well-named function will allow us to read the code and immediately understand what is going on in it. Look at the example below:

``` python
# Calculates the cost of office floor in a building
cost = 3*3*4*2900 + 2*5*8*2900 + 15*5*2900 + 24*2*1800
```

We can only guess that the "small" numbers are meters, and the "big" numbers are the price per square meter. But why are three small numbers multiplied? Is it about cubic meters?

``` python
cost = (
    3 * office_cost(3, 4)
    + 2 * office_cost(5, 8)
    + office_cost(15, 5)
    + hall_cost(24, 2)
)
```

A code like this much better explains to the reader what's going on here: three offices measuring 3x4m, two offices measuring 5x8m, one measuring 15x5m, and a corridor 24m long and 2m wide. Two different functions are used to calculate the cost of the office and corridor, and this tells us that the office and corridor have different rates per square meter - and each function knows its own.

## Syntax

Shown above is the sample use of functions, in other words: **call** with **arguments**. In order for that code to work, the corresponding functions must have already been created. You will learn more about creating functions during classes with the lecturer. For now , just see how such functions would have to be defined:

``` python
def office_cost(width, length):
    return width * length * 2900

def hall_cost(width, length):
    return width * length * 1800
```

## Summary

As you can see, it doesn't look complicated - a function is simply a piece of code that you can jump to for a moment (taking the necessary data with you), calculate what you need, and then take the result and use it in the place that the function was called from.
