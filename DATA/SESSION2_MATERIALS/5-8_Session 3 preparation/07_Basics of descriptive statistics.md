# Basics of descriptive statistics

Type: Article

Pandas offers many methods for determining basic descriptive statistics such as:

- mean
- median
- standard deviation
- percentiles / quantiles.

In this section, we will recall the interpretations of all these metrics in the context of the dataset we are working on.

> Since the homework assignment is to perform an analogous analysis for the full set of data, here we will use only a subset of them - the transformations.

## Loading the data into the DataFrame

``` python
import pandas as pd

df_raw = pd.read_csv(
    r'..\01_data\raw\preserves.csv',  # path to data file
    sep=';',  # column separator
    decimal=','  # character separating the whole and fractional parts of a number
)
```

### Mean

The most well-known positional statistic, at the same time it is very often abused and vulnerable to data manipulation.

It is calculated simply as the sum of numbers divided by their number.

> After also getting familiar with the median, we recommend reading [this article](https://en.as.com/latest_news/what-is-the-difference-between-median-salary-and-average-salary-n/) as an example of a situation when the arithmetical average does not work well.

Using Pandas, you can determine the mean with `mean()`:

``` python
df_raw['Value'].mean() # determine the average price for the pickups
```

Result:

``` 
2.1737464985994395
```

### Standard deviation

Often, the standard deviation is given next to the mean as a statistic for how the data differs from the mean.

The larger the value of the standard deviation, the more dispersed the data is. In other words, the standard deviation is counted to examine whether units in a population are similar for the characteristic under study.

> Standard deviation is always >= 0

In addition to the standard example on the basis of the data set under consideration, we will present an example of other data with the same mean, but with different variance.

In Pandas standard deviation is determined with `std()`:

``` python
df_raw['Value'].std()
```

Result:

``` 
2.783597750653627
```

Now let's look at a fictional (a little extreme) example of data, where the mean will be the same, but the standard deviations will be different:

``` python
# here we have an example of data with mean = 0
data1 = pd.Series([-1, 0, 1])
data2 = pd.Series([-10, -90, 0, 0, 100])

print("Data 1 mean: {}; std: {}".format(
    data1.mean(),
    data1.std()
))

print("Data 2 mean: {}; std: {}".format(
    data2.mean(),
    data2.std()
))
```

Result:

``` 
Data 1 mean: 0.0; std: 1.0
Data 2 mean: 0.0; std: 67.45368781616021
```

### Median

Another basic statistic is the median, otherwise known as the middle value.
Its value indicates that 50% of the observations are smaller than it, and 50% are larger than it.

In Pandas median is determined with `median()`:

``` python
df_raw['Value'].median()
```

Result:

``` 
1.775
```

That is: between 1999 and 2019, as much as 50% of the prices of processed goods were lower and 50% higher than about 1.78 .

### Percentile

Percentiles are a generalization of the concept of the median to other values. For example, a percentile of 10% will determine the value for which 10% of observations will be lower and 90% will be higher.

> It can also be said that the median is a special case of the 50% percentile.

> Other special cases of percentiles are quantiles, that is, percentiles of 0% (minimum / quantile 0), 25% (1st quantile), 50% (2nd quantile / median), 75% (3rd quantile) and 100% (maximum / 4th quantile).

Quantiles in Pandas are determined with `quantile(q)`, where q is a list of percentiles we want to determine.

``` python
# We determine percentile 0, 10%, 50% (median), 75% and 100% (max)
df_raw['Value'].quantile([0, 0.1, 0.5, 0.75, 1])
```

Result:

``` 
0.00     0.000
0.10     0.000
0.50     1.775
0.75     3.130
1.00    15.590
Name: Value, dtype: float64
```

Where:

1. Minimum value - 0,
2. Percentile 10% - 0 - that is, 10% of the price values for processed goods in 1999-2019 were less than or equal to 0,
3. Median - 1.775 - i.e. between 1999 and 2019, 50% of the prices for processed goods were less than, and 50% were higher than about 1.78
4. Percentile 75% - 3.13 - that is, between 1999 and 2019, 75% of the price of processed goods was lower than 3.13,
5. Max - 15.59 - that is, in 1999-2019 the maximum price in the processed goods group was 15.59

### `describe()` method

All the above statistics do not need to be determined manually each time. Pandas offers a neat function that summarizes Series / DataFrame - `describe(percentiles)`.

The function determines the mean, standard deviation, percentiles and the number of non-NNN observations.

Parameters:

- `percentiles` percentiles we want to determine (analogous to the `quantile` function). Defaults are: 0%, 25%, 50%, 75%, 100%.

Example:

``` python
df_raw['Value'].describe()
```

Result:

``` 
count    1428.000000
mean        2.173746
std         2.783598
min         0.000000
25%         0.000000
50%         1.775000
75%         3.130000
max        15.590000
Name: Value, dtype: float64
```
