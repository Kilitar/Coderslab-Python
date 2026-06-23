# Filtering data

Type: Exercise

## Filtering data

While generating the `product_prices_renamed.csv` file the following processing errors occurred and they need to be found:

1. In the **date** column, data from 1888 appeared - '1888-0',
2. Check the **date** column for similar errors but with future values.
3. In the **value** column, too high value was introduced – find it and locate the row where it is (use `query`),
4. There was a spelling error in the **product_types** column for one of the products. Find it and the corresponding rows. How many such rows are there?

You do not need to assign the results to the variable: it is enough if you display them.

> Later, based on the solution of this task, we will correct all errors in the data.

Hints:

Subsection 2:

1. There is only one such value.
2. Use `loc` or `query` with the condition `date > '2020-1'`.

Subsection 3:

1. There is only one such value.
2. Do the following:
  
  1. use `describe()`, to view percentiles,
  2. use `loc` or `query` to find erroneous entries,

Subsection 4:

You can do it in the following way:

1. Use `unique()` method to find all available values,
2. Use `loc` or `query` to find erroneous entries,
3. The number of rows can be checked with the `shape` method.
