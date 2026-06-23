# Code style

Type: Article

![Code style](/presentations/DTL/en/4.9/W/M_04_S_02/27fb0f51-63a0-48fd-9722-5944eeb8ada5/student_content/4c26b2b3-242c-46df-a56a-62d666c00e58/images/styl_kodu.jpg)

## Introduction

It is not hard to write a piece of code that works. What distinguishes the best programmers from the mediocre ones, is their code style.
The best ones obviously write code that works. Moreover, it is readable and well optimized.
In short, there is certain elegance to it.

In this article, we will discuss the basic principles of writing nice code in Python.

---

## PEP 8

**PEP 8** is just a set of rules on how to write code in Python. Without following these rules, your code may work, but it certainly won't be consistent nor elegant.
You can find the entire PEP 8 documentation here
[https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/).

It is quite extensive. Fortunately, there are a many tools that can help you maintain high quality code.
These are different types of linters, such as Pylint or Flake8.

Now let's discuss some basics rules of writing elegant code.

---

## Indentations

Blocks of code written in Python should be "indented" with 4 spaces. Most editors by default, replace a tab with four spaces, or at least have the option to be configured that way.

---

## Defining lists

When defining a list, you should remember that separating elements, apart from the obligatory comma, there should also be a **space**.

##### Good:

``` python
members = ["Mike", "Ike", "Spike"]
```

##### Bad:

``` python
members = ["Mike","Ike","Spike"]
```

If you want to define a very long list, it is good to split it The closing parenthesis should be placed on a new line.
It is good if it has the same indentation as the variable to which you assign the list.

##### Example:

``` python
numbers = [
    1, 2, 3,
    4, 5, 6,
]
```

---

## Maximum line length

According to PEP 8 convention, the maximum line length is 79 characters. However, modern monitors have much higher resolution and allow more code to be displayed.
Therefore this rule is often bent, assuming as the maximum line length of 120 characters.

## Operators

Operators, should be surrounded by a space character on both sides: this provides better code readability.

##### Good:

``` python
result = 2 + 2 * 2
```

##### Bad:

``` python
result=2+2*2
```

---

## Summary

Keeping in mind the fact that the most commonly mentioned advantage of Python is its readability it is a good idea to keep the high quality of code - at least by following the `PEP 8` convention.
Fortunately, there is a number of tools available that will make it easier for you.

When you have the time, we recommend reading a detailed description of PEP 8, which you can find here:
[https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/).

And in this article you will find some other rules that help to keep the code quality high:
[https://docs.python-guide.org/writing/style/](https://docs.python-guide.org/writing/style/).
