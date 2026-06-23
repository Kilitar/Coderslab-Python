# Modification of column names

Type: Exercise

## Modification of column names

Read the file **product_prices.csv** into a DataFrame. Modify the names of columns so that they match those in the **product_prices_renamed.csv** file. Complete two variants of the exercise:

1. Using the `rename` method,
2. Overwriting all column names using `columns`.

To unify the naming and reduce the risk of a **typo**, you can use the dictionary below:

``` 
{'Name': 'province',
 'Types of goods': 'product_types',
 'Measurement unit': 'currency',
 'id': 'id',
 'Types of products': 'product_line',
 'Value': 'value',
 'Date': 'date'}
```

> The `columns` method overwrites the columns directly on the object (does not return a new DataFrame), so if you do step 2 first, the hint will be useless (the columns get overwritten).
