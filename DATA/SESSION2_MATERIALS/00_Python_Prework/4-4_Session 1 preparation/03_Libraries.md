# Libraries

Type: Article

From this article you will learn what libraries are and how to install and use them.

## What is a library?

A library is simply a set of tools (functions, constants, classes, etc.) related to some issue, and providing solutions to common tasks. As a programmer, you can import such a library, and then reach for anything that its creators have prepared.

## Embedded libraries

We are going to use the `csv` library as an example here – it is a collection of tools to work with **.csv** files (they can be created with e.g. Microsoft Excel):

``` python
import csv

with open('eggs.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
```

The imported `csv` module provided the `csv.reader` function; in turn, the function made it possible for us to read the sheet in a loop: row by row.

Knowing the library has saved us from writing all the code that reads **.csv** files by ourselves.

## Additional libraries

We are not limited to Python's built-in libraries. The open source community has created plenty of other useful libraries - and there are tools to install them easily.

This time we will use the `openpyxl` library as an example.

### Installing libraries using terminal

The command used to install libraries is `pip`. Using it in the console looks like this:
```bash
$ pip install openpyxl
```
Once the installation succeeds the library is ready to use:

```bash
$ python
Python 3.9.1 (default, Jan 20 2021, 00:00:00)
[GCC 10.2.1 20201125 (Red Hat 10.2.1-9)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> import openpyxl
```

### Installing libraries from within Jupyter

We can use the same command from the Jupyter editor. Just remember that `pip` is not a Python keyword but a separate program – to run it put the `!` character at the beginning of the line:

``` python
!pip install openpyxl
```

> **Pro tip**
> 
> This code can sometimes cause an error. If somewhere in the body of the error there is a line `PermissionError: [Errno 13] Permission denied:`, the error is caused by no access to our disk from the level of Jupyter. The easiest solution to this problem is to run Jupyter Notebook as an administrator.

In the next line we can check if the library has installed correctly:

``` python
import openpyxl
```

In a notebook, the whole process looks like this:

![library_installation](/presentations/DTL/en/4.9/W/M_04_S_04/ed19ad35-577e-46e1-a7ea-7b3689faa10d/student_content/2ba06edc-0518-48da-a596-61159bcd2408/images/instalacja_biblioteki_en.png)

## Summary

Installing libraries is easy, and knowing them greatly speeds up writing programs - you don't have to solve problems already solved by someone else. Sometimes the biggest problem will be... choosing the library - the open source community has really made an effort to make sure there are plenty to choose from!
