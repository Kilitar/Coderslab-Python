# Dataframe basics

Type: Article

Using the example of data on average food prices, we will present the most basic methods to get familiar with the dataset offered by Pandas.

## Loading data

We will read the data from **product_prices_cleaned.csv** file. To do so, we will use the `read_csv` method that we already discussed.

``` python
import pandas as pd # library import

df_raw = pd.read_csv(
    r'..\01_data\product_prices.csv',  # path to data file
    sep=';',  # column separator
    decimal=','  # character separating the whole and fractional parts of a number
)
```

## Getting familiar with the structure of the data

Loading the data without an interpreter error does not yet mean that the process has been entirely correct. For example, if you make a mistake with the separator, the data will be loaded without error, but when you start further work it may turn out that the representation in the structure is not what you expect - for example, all the data can appear in one column.

### `shape` method

The `shape` method gives us general information about our dataset. It returns a tuple representing the dimensions of the DataFrame: (number_of_rows, number_of_columns).

It returns a tuple with information about the number of rows and columns:

``` python
df_raw.shape
```

Result:

``` 
(149940, 7)
```

Number of rows in Dataframe:

``` python
df_raw.shape[0]
```

Result:

``` 
149940
```

Number of DataFrame columns:

``` python
df_raw.shape[1]
```

Result:

``` 
7
```

### `head`method

Basic method to display and check if the data has the expected shape and format. It returns the DataFrame view.

Parameters:

- `n` - number of rows to display (default: 5)

``` python
df_raw.head(5) # displays the first 5 rows of the table
```

Result:

| # | Name | Types of goods | Measurement unit | Group ID | Types of products | Value | Date |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | SUBCARPATHIA | NaN | PLN | 2 | pork ham cooked - per 1kg | 21.37 | 2013-3 |
| 1 | ŁÓDŹ | NaN | PLN | 4 | bread - per 1kg | NaN | 2018-2 |
| 2 | KUYAVIA-POMERANIA | NaN | PLN | 2 | barley groats sausage - per 1kg | 3.55 | 2019-12 |
| 3 | DOLNOŚLĄSKIE | NaN | PLN | 2 | dressed chickens - per 1kg | 6.14 | 2019-2 |
| 4 | WARMIA-MASURIA | NaN | PLN | 2 | Italian head cheese - per 1kg | 5.63 | 2002-3 |

### `tail` method

It is the equivalent of `head()` – the difference is that instead of returning *n* first rows, it returns *n* last rows.

Parameters:

- `n` - number of rows to display (default: 5)

``` python
df_raw.tail(10)
```

Result:

| # | Name | Type of goods | Measurement unit | Group ID | Types of products | Value | Date |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 149930 | WARMIA-MASURIA | NaN | PLN | 4 | Poznan wheat flour, bagged - per 1kg | 0.99 | 2010-10 |
| 149931 | POMERANIA | NaN | PLN | 2 | pork belly cooked - per 1kg | 14.48 | 1999-10 |
| 149932 | MASOVIA | NaN | PLN | 2 | salted herring, non-dressed - per 1kg | 0.00 | 2001-3 |
| 149933 | SILESIA | NaN | PLN | 2 | smoked bacon with ribs - per 1kg | 15.95 | 2015-9 |
| 149934 | SILESIA | NaN | PLN | 2 | barley groats sausage - per 1kg | 4.50 | 2004-8 |
| 149935 | KUYAVIA-POMERANIA | NaN | PLN | 2 | pork  meat (raw bacon)) - per 1kg | 12.15 | 2016-11 |
| 149936 | ŁÓDŹ | beet sugar white, bagged - ... | PLN | 3 | NaN | 0.00 | 2012-5 |
| 149937 | LESSER POLAND | NaN | PLN | 4 | plain mixed bread (wheat-rye) - per 1kg | 3.05 | 2008-6 |
| 149938 | WARMIA-MASURIA | NaN | PLN | 2 | boneless beef (sirloin) - per 1kg | 11.87 | 2000-11 |
| 149939 | MASOVIA | NaN | PLN | 4 | Masurian barley groats - per 1kg | 0.16 | 2005-10 |

### `info` method

Displays a concise summary of information about the DataFrame structure, that is, the list, the type of columns and the number of rows containing non-empty values in each column.
Additionally, displays information about memory usage for the entire DataFrame.

``` python
df_raw.info()
```

Result:

``` 
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 149940 entries, 0 to 149939
Data columns (total 7 columns):
 #   Column             Non-Null Count   Dtype
---  ------             --------------   -----
 0   Name               149940 non-null  object
 1   Rodzaje towarów    34272 non-null   object
 2   Jednostka miary    149940 non-null  object
 3   ID grupy           149940 non-null  int64
 4   Rodzaje produktów  115668 non-null  object
 5   Wartość            137088 non-null  float64
 6   Data               149940 non-null  object
dtypes: float64(1), int64(1), object(5)
memory usage: 8.0+ MB
```

### `columns` method

The `columns` method returns the names of all columns in a given DataFrame.

``` python
df_raw.columns
```

Result:

``` 
Index(['Name', 'Types of goods', 'Measurement unit', 'Group ID', 'Types of products', 'Value', 'Date'],
      dtype='object')
```

This method can also be used if you want to change the names of **all** columns in the DataFrame; just write:

``` 
df_raw.columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g']  # overwriting column names
```

However, note that in this case the number of passed new column names must be equal to the number of the columns in the frame.

## Basic DataFrame operations

### Choosing a column

One common task is to select only the columns of interest from the output set. There is an easy way to do it: with the standard indexing operator `df[column_name]`. For example:

``` python
df_raw['Name']  # displays only the 'Name' column from the DataFrame'
```

Result:

``` 
0                SUBCARPATHIA
1                        ŁÓDŹ
2           KUYAVIA-POMERANIA
3               LOWER SILESIA
4              WARMIA-MASURIA
             ...
149935      KUYAVIA-POMERANIA
149936                   ŁÓDŹ
149937          LESSER POLAND
149938         WARMIA-MASURIA
149939                MASOVIA
Name: Name, Length: 149940, dtype: object
```

A single column from the DataFrame will be returned at this point, but it will be a different structure - Series (we will discuss it later).

> An acceptable form of column selection is still df_raw.column_name.

### Selecting columns

When you want to display more than one column, you need to pass a list of names, for example:

``` python
df_raw[['Name', 'Value', 'Date']]  # displays the columns 'Name', 'Value', 'Date' from the DataFrame
```

Result:

| # | Name | Value | Date |
| --- | --- | --- | --- |
| 0 | SUBCARPATHIA | 21.37 | 2013-3 |
| 1 | ŁÓDŹ | NaN | 2018-2 |
| 2 | KUYAVIA-POMERANIA | 3.55 | 2019-12 |
| 3 | LOWER SILESIA | 6.14 | 2019-2 |
| 4 | WARMIA-MASURIA | 5.63 | 2002-3 |
| ... | ... | ... | ... |
| 149935 | KUYAVIA-POMERANIA | 12.15 | 2016-11 |
| 149936 | ŁÓDŹ | 0.00 | 2012-5 |
| 149937 | LESSER POLAND | 3.05 | 2008-6 |
| 149938 | WARMIA-MASURIA | 11.87 | 2000-11 |
| 149939 | MASOVIA | 0.16 | 2005-10 |

149940 rows × 3 columns

With this type of operation, a DataFrame object is also returned, so we can use all the methods we learned earlier.

> If by some reasons we want to select one column from a DataFrame and force Pandas to return it as a DataFrame, it is enough to pass the column as a list, e.g. `df_raw[['Name']]`.

#### `loc` method

An alternative to the column selection methods given earlier is the `loc` method. It is going to be discussed in more detail by the lecturer.

``` python
df_raw.loc[:, 'Value']
```

Result:

``` 
0         21.37
1           NaN
2          3.55
3          6.14
4          5.63
          ...
149935    12.15
149936     0.00
149937     3.05
149938    11.87
149939     0.16
Name: Value, Length: 149940, dtype: float64
```

``` python
df_raw.loc[:, ['Value', 'Name']]
```

Result:

| # | Value | Name |
| --- | --- | --- |
| 0 | 21.37 | SUBCARPATHIA |
| 1 | NaN | ŁÓDŹ |
| 2 | 3.55 | KUYAVIA-POMERANIA |
| 3 | 6.14 | LOWER SILESIA |
| 4 | 5.63 | WARMIA-MASURIA |
| ... | ... | ... |
| 149935 | 12.15 | KUYAVIA-POMERANIA |
| 149936 | 0.00 | ŁÓDŹ |
| 149937 | 3.05 | LESSER POLAND |
| 149938 | 11.87 | WARMIA-MASURIA |
| 149939 | 0.16 | MASOVIA |

149940 rows × 2 columns.

> The `loc` method has a very wide range of uses. In addition to its trivial use in the form of column selection, it is more often used as a way to filter the DataFrame or modify the data. These aspects will be discussed in the lectures.
