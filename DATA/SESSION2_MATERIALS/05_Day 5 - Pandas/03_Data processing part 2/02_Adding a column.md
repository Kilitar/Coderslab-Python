# Adding a column

Type: Exercise

## Adding a column

Following on the solution of the previous exercise, create a new column: **product** using **product_types** and **product_line**:

1. Check that the **product_types** and **product_line** columns are complementary (an empty value in one column entails a non-empty value in the other).
2. Create a new column: **product** using the values from the **product_types** column e.g. `df['product'] = df['product_types']`.
3. Find non-empty values in the **product_line** column and enter them into the **product** column,
4. Use a method of your choice to check if all values in the **product** column are non-empty.
5. Remove duplicates from the table.
6. Using the `to_csv` method save the data (we will be using them later in the course), set separator=';' and `index=False`.
  
  Save the file as `product_prices_cleaned.csv`.

The `to_csv` method is one of many that can be used to save a `DataFrame` as a **csv** file. Within the scope of this exercise we are interested in the following parameters.

- `sep` - row separator (',' by default),
- `index` - should table index (row number, by default) also be saved (default: `True`).

Sample call:

``` 
df.to_csv(
    'filepath', # path to file
    sep=';', # separator setting
    index=False
)
```
