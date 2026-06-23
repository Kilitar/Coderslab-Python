# Analytical functions

Type: Article

Analytic functions are a useful tool when working with data. They allow you to process data **without aggregation**, which means you can extract information about a group without losing information about its components.

The most basic methods are:

- **row number** (`cumcount`) –  this is the most basic function to determine the position of an element within a group - for example, having test scores, we can rank students from best to worst,
- **cumulative sum** (`cumsum`) – useful when we want to determine e.g. feature distribution in percent,
- **cumulative minimum** (`cummin`) – showing how the minimum changes over time,
- **cumulative maximum** (`cummax`) – analogous to minimum – how the maximum changes over time.

Determining the function in Pandas is done in two steps:

1. First, we sort the set by the feature (or features) we are interested in,
2. We group `DataFrame` by some criterion and determine the statistics.

> **Note:**
> 
> These functions are not implemented for `DataFrame`, that is why step (1) is necessary even if we work on the entire dataset. Then you can create yourself a column, e.g. **dummy**, which will contain only one value and will be used for trivial grouping of elements.

For the presentation of methods, we will use the collection about product prices, which was processed in lectures. For the sake of clarity, we will only deal with the product **barley porridge - per 1kg** for data from Poland.

## Loading and preliminary processing of data

``` python
import pandas as pd

df = pd.read_csv(
    r'..\01_data\processed\product_prices_cleaned.csv',
    sep=';'
)
df.head()  # making sure that the data was read correctly
```

Result:

| # | province | product_types | currency | product_group_id | product_line | value | date | product |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | SUBCARPATHIA | NaN | PLN | 2 | pork ham cooked - per 1kg | 21.37 | 2013-3 | pork ham cooked - per 1kg |
| 1 | ŁÓDŹ | NaN | PLN | 4 | bread - per 1kg | NaN | 2018-2 | bread - per 1kg |
| 2 | KUYAVIA-POMERANIA | NaN | PLN | 2 | barley groats sausage - per 1kg | 3.55 | 2019-12 | barley groats sausage - per 1kg |
| 3 | LOWER SILESIA | NaN | PLN | 2 | dressed chickens - per 1kg | 6.14 | 2019-2 | dressed chickens - per 1kg |
| 4 | WARMIA-MASURIA | NaN | PLN | 2 | Italian head cheese - per 1kg | 5.63 | 2002-3 | Italian head cheese - per 1kg |

Next we filter data:

``` python
df = df.loc[
    (df['product'] == 'barley groats sausage - per 1kg') &
    (df['province'] == 'POLAND')
]
df.head()  # reviewing filtering correctness
```

Result:

| # | province | product_types | currency | product_group_id | product_line | value | date | product |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 888 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 4.34 | 2002-6 | barley groats sausage - per 1kg |
| 3257 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 7.63 | 2012-3 | barley groats sausage - per 1kg |
| 4384 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 7.24 | 2011-8 | barley groats sausage - per 1kg |
| 4846 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 5.76 | 2008-8 | barley groats sausage - per 1kg |
| 6033 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 3.70 | 2019-2 | barley groats sausage - per 1kg |

Next, we convert the corresponding column to a date:

``` python
df['date'] = pd.to_datetime(df['date'], format='%Y-%m')
```

## Row number

As we mentioned, row number is used to number the rows according to a certain order. For example, we will determine the ranking, based on the price of the product over time (descending).

Let's start by sorting the frame according to the value:

``` python
df_sorted = df.sort_values(by=['value'], ascending=False)
df_sorted['rn'] = df_sorted.groupby(by=['product']).cumcount()
```

> **Note:**
> 
> DataFrame does not implement `cumcount` – this method can only be used after grouping data (even trivially like here).

The `cumcount` returns a `Series` type object. If we want to save the results to our output `DataFrame`, they need to be added as a new column.

Note that `cumcount` function returns values from 0 to n - 1:

``` python
df_sorted.head()
```

Result:

| # | province | product_types | currency | product_group_id | product_line | value | date | product | rn |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 58430 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 9.41 | 2019-01-01 | barley groats sausage - per 1kg | 0 |
| 95878 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 9.40 | 2018-08-01 | barley groats sausage - per 1kg | 1 |
| 27810 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 9.33 | 2018-10-01 | barley groats sausage - per 1kg | 2 |
| 17846 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 9.24 | 2019-10-01 | barley groats sausage - per 1kg | 3 |
| 44600 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 9.17 | 2018-06-01 | barley groats sausage - per 1kg | 4 |

Now we can, for example, select the top months with price:

``` python
df_sorted.query("rn < 10")
```

Result:

| # | province | product_types | currency | product_group_id | product_line | value | date | product | rn |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 58430 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 9.41 | 2019-01-01 | barley groats sausage - per 1kg | 0 |
| 95878 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 9.40 | 2018-08-01 | barley groats sausage - per 1kg | 1 |
| 27810 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 9.33 | 2018-10-01 | barley groats sausage - per 1kg | 2 |
| 17846 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 9.24 | 2019-10-01 | barley groats sausage - per 1kg | 3 |
| 44600 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 9.17 | 2018-06-01 | barley groats sausage - per 1kg | 4 |
| 26335 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 9.14 | 2019-09-01 | barley groats sausage - per 1kg | 5 |
| 83383 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 9.12 | 2017-11-01 | barley groats sausage - per 1kg | 6 |
| 46104 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 9.11 | 2018-02-01 | barley groats sausage - per 1kg | 7 |
| 99474 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 8.98 | 2019-07-01 | barley groats sausage - per 1kg | 8 |
| 79836 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 8.90 | 2018-12-01 | barley groats sausage - per 1kg | 9 |

## Cumulative sum

Let's determine the cumulative price - we will do this only for the purpose of presenting the method (this information in this case has no significant value, but in combination with the row number it allows to determine the cumulative average).

Let's start by sorting the frame according to the value:

``` python
df_sorted = df_sorted.sort_values(by=['value'], ascending=False)
```

As with `cumcount`, the `cumsum` function is not implemented for the DataFrame.

> **Note:**
> 
> If there is more than one number column in the frame, a new DataFrame will be returned.

``` python
df_sorted['cs'] = df_sorted.groupby(by=['product'])['value'].cumsum()
df_sorted.head()
```

Result:

| # | province | product_types | currency | product_group_id | product_line | value | date | product | rn | cs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 58430 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 9.41 | 2019-01-01 | barley groats sausage - per 1kg | 0 | 9.41 |
| 95878 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 9.40 | 2018-08-01 | barley groats sausage - per 1kg | 1 | 18.81 |
| 27810 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 9.33 | 2018-10-01 | barley groats sausage - per 1kg | 2 | 28.14 |
| 17846 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 9.24 | 2019-10-01 | barley groats sausage - per 1kg | 3 | 37.38 |
| 44600 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 9.17 | 2018-06-01 | barley groats sausage - per 1kg | 4 | 46.55 |

## Cumulative minimum (`cummin`)

Next, we will calculate the ascending minimum. Let's start by sorting the frame by date:

``` python
df_sorted = df_sorted.sort_values(by=['date'], ascending=True)
```

As with the previous functions, `cummin` is not implemented for DataFrame.

> **Note:**
> 
> If there is more than one number column in the frame, a new DataFrame will be returned.

``` python
df_sorted['cummin'] = df_sorted.groupby(by=['product'])['value'].cummin()
df_sorted.head()
```

Result:

| # | province | product_types | currency | product_group_id | product_line | value | date | product | rn | cs | cummin |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 109105 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 3.40 | 1999-01-01 | barley groats sausage - per 1kg | 247 | 1506.40 | 3.40 |
| 63584 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 3.59 | 1999-02-01 | barley groats sausage - per 1kg | 237 | 1471.56 | 3.40 |
| 98733 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 3.25 | 1999-03-01 | barley groats sausage - per 1kg | 249 | 1512.94 | 3.25 |
| 34091 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 3.41 | 1999-04-01 | barley groats sausage - per 1kg | 245 | 1499.60 | 3.25 |
| 104713 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 3.50 | 1999-05-01 | barley groats sausage - per 1kg | 243 | 1492.72 | 3.25 |

## Cumulative maximum (`cummax`)

Finally, we will calculate the ascending maximum. Using the `cummax` function is analogous to `cummin`:

``` python
df_sorted = df_sorted.sort_values(by=['date'], ascending=True)
df_sorted['cummax'] = df_sorted.groupby(by=['product'])['value'].cummax()

df_sorted.head()
```

Result:

| # | province | product_types | currency | product_group_id | product_line | value | date | product | rn | cs | cummin | cummax |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 109105 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 3.40 | 1999-01-01 | barley groats sausage - per 1kg | 247 | 1506.40 | 3.40 | 3.40 |
| 63584 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 3.59 | 1999-02-01 | barley groats sausage - per 1kg | 237 | 1471.56 | 3.40 | 3.59 |
| 98733 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 3.25 | 1999-03-01 | barley groats sausage - per 1kg | 249 | 1512.94 | 3.25 | 3.59 |
| 34091 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 3.41 | 1999-04-01 | barley groats sausage - per 1kg | 245 | 1499.60 | 3.25 | 3.59 |
| 104713 | POLAND | NaN | PLN | 2 | barley groats sausage - per 1kg | 3.50 | 1999-05-01 | barley groats sausage - per 1kg | 243 | 1492.72 | 3.25 | 3.59 |
