# Introduction to numpy

Type: Article

## Pandas and Numpy

As we mentioned, Pandas is a library designed to make working with data easier by providing high-level tools for data processing and analysis.

In fact at the heart of Pandas is `NumPy` (Numeric Python), that makes it possible to work with large, multidimensional datasets. It is from NumPy that the assumption that each column in Pandas has one specific type comes from, and allows operations on columns through basic arithmetic operations.

Full description and library documentation is available at the [link](https://numpy.org/doc/stable/reference/generated/numpy.array.html).

NumPy itself in data analysis and processing can be used as an advanced alternative to Pandas if our code is executing too slowly. However, it is more often found in tasks related to Data Science - that is, modeling and analysis of multidimensional data.

In this article we are going to present only the most basic elements of `NumPy`: arrays and array operations.

## `array`

The basic type of data in `NumPy` is an `array` – using it is similar to using a list, but there are a few significant differences:

- The data it contains has a single, predetermined type,
- takes up less space,
- is definitely faster.

> `Series` in Pandas is in fact a Numpy `array`!

In situations where processing millions of records is crucial, using NumPy is invaluable.

Example – `array` and list:

``` python
import numpy as np

lst = [1, 2, 3]
arr = np.array(lst) # list can be converted to array
```

Indexing:

``` python
print(lst[1])
print(arr[1])
```

Result:

``` 
2
2
```

Slicing:

``` python
print(arr[1:])
print(lst[1:])
```

Result:

``` 
[2 3]
[2, 3]
```

Another difference arises when you want to perform a certain operation on all the data. In NumPy, multiplying an array by a number is trivial:

Example:

``` python
arr*5
```

Result:

``` 
array([ 5, 10, 15])
```

Performing the same operation on a list will *extend* it five times: to multiply each element, you have to write something like a loop (we leave it as an exercise).

## `ndarray`

It is a multidimensional version of `array` with the same properties: i.e. having one, defined data type. In other words, it is a multidimensional matrix.

`ndarray` object can be created by passing a list to an `array`.

> Notice that in this case Pandas `DataFrame` cannot be fully equaled with an `ndarray` because each of its columns can give a different data type. In this case `DataFrame`, has a similar structure as multiple `Series`.

[Link](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html) to the object documentation.

Example – creating a 2x2 array:

``` python
x = np.array([
    [1, 2, 3],
    [4, 5, 6]])
x
```

Result:

``` 
array([[1, 2, 3],
       [4, 5, 6]])
```

And type of the `x` variable:

``` python
type(x)
```

Result:

``` 
numpy.ndarray
```

Example - displaying an element from the first column, first row:

``` python
x[0,0]
```

Result:

``` 
1
```

Example - displaying only the first column:

``` python
x[:,0]
```

Result:

``` 
array([1, 4])
```

Example - multiplying the array by a constant:

``` python
x*2
```

Result:

``` 
array([[ 2,  4,  6],
       [ 8, 10, 12]])
```

Example - adding an array to an array:

``` python
x + x
```

Result:

``` 
array([[ 2,  4,  6],
       [ 8, 10, 12]])
```
