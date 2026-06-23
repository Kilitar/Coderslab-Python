# Series basics

Type: Article

Series are one-dimensional arrays; as an analogy you can imagine them as a column in a spreadsheet or a column known from databases.
The data in a Series must be of one specific type, making them closer to columns known from databases.

> In fact, DataFrames are strongly related to Series, since each column in a DataFrame is actually a Series. You can therefore think of DataFrames as a set of Series.

Series themselves can additionally be decomposed into two components: index and data. Index can be understood (very simplistically) as a row number.

Importantly, the index must be the same length as the data, and is used, among other things, for operations between Series.

## Loading data

As with the introduction to the DataFrame, here we will also use data from the *ceny_towarow.csv* file. To do so, we will use the `read_csv` method that we already discussed.

``` python
import pandas as pd
df_raw = pd.read_csv(
    r'..\01_data\product_prices.csv',  # path to data file
    sep=';',  # column separator
    decimal=','  # character separating the whole and fractional parts of a number
)
```

## DataFrame, or collection of Series

As we mentioned earlier, Series are a component of DataFrame. As a review, let's take a look at the selection of the selected column and use it as an example to introduce basic operations.

> Some basic DataFrame functions such as `head` or `tail` are also available for Series.

``` python
col = df_raw['Value'].head() # we pull the Value column out of the frame - it will be useful for presenting sub-stat operations
type(col) # we check that the column type is actually series
```

Result:

``` 
pandas.core.series.Series
```

## Basic operations on Series

Series as a column allows direct operations on the entire column. Basic arithmetic operators (`+`, `-`, `*`, `/`) are implemented in Pandas.

Also importantly, it is possible to both multiply Series by a number and by another series.

### Operations using numbers

Below are examples showing the basic mathematical operations available in Pandas:

``` python
col # display the contents of Series
```

Result:

``` 
0    21.37
1      NaN
2     3.55
3     6.14
4     5.63
Name: Value, dtype: float64
```

Addition:

``` python
col + 1 # subtract the value from each element
```

Result:

``` 
0    22.37
1      NaN
2     4.55
3     7.14
4     6.63
Name: Value, dtype: float64

Subtraction:
```python
col - 5 # subtract the value from each element
```

Result:

``` 
0    16.37
1      NaN
2    -1.45
3     1.14
4     0.63
Name: Value, dtype: float64
```

Multiplication

``` python
col * 2.5 # multiply all values
```

Result:

``` 
0    53.425
1       NaN
2     8.875
3    15.350
4    14.075
Name: Value, dtype: float64
```

Division:

``` python
col / 2.5 # we divide each element
```

Result:

``` 
0    8.548
1      NaN
2    1.420
3    2.456
4    2.252
Name: Value, dtype: float64
```

### Arithmetic operations between Series

We can also use mathematical operators to work with two series:

``` python
col + col # we practically multiply the values by 2, but using an alternative operation
```

Result:

``` 
0    42.74
1      NaN
2     7.10
3    12.28
4    11.26
Name: Value, dtype: float64
```

For the purposes of the next example, we will create a new dummy Series object:

``` python
col_example = pd.Series(
    range(len(col))
)
col_example # we check that what has been created looks as expected
```

Result:

``` 
0    0
1    1
2    2
3    3
4    4
dtype: int64
```

> In the example above, we saw how to create a Series manually. This is not the only way to generate this object - you can also use lists or dictionaries. You can find out more about creating Series in the [documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html).

Adding Series:

``` python
col + col_example
```

Result:

``` 
0    21.37
1      NaN
2     5.55
3     9.14
4     9.63
dtype: float64
```

To do an operation across different series (`col` and `col_example` in our case) Pandas uses indexes. The process can be understood as follows: e.g. before adding `col` to `col_example` series are connected using indexes (0 to 0 etc.), and only later adding elements is executed.

Operations on series are technically allowed, in such case the result is the longer series – but with missing elements (`NaN`).

Let's create another Series object:

``` python
# we create a series that has one less row to force a NaN to be created at the next operation
col_example2 = pd.Series(
    range(len(col)-1)
)
col_example2  # checking Series generation
```

Result:

``` 
0    0
1    1
2    2
3    3
dtype: int64
```

Let's see what happens if we add this series to the previous one:

``` python
col + col_example2
```

Result:

``` 
0    21.37
1      NaN
2     5.55
3     9.14
4      NaN
dtype: float64
```

## `unique` method

In data analysis, we often want to know what values appear in a column in order to find, for example, errors, outliers or just a record we are interested in. This type of task can be performed using `unique`.

In the following example, we will see what provinces (column **Name**) are available in the analyzed dataset.

View what provinces are available in the source data:

``` python
df_raw['Name'].unique()
```

Result:

``` 
array(  ['SUBCARPATHIA', 'ŁÓDŹ', 'KUYAVIA-POMERANIA', 'LOWER SILESIA',
        'WARMIA-MASURIA', 'HOLY CROSS', 'WEST POMERANIA',
        'POLAND', 'PODLASKIE', 'GREATER POLAND', 'POMERANIA', 'LESSER POLAND',
        'SILESIA', 'MASOVIA', 'LUBLIN', 'LUBUSZ', 'OPOLE'],
        dtype=object)
```
