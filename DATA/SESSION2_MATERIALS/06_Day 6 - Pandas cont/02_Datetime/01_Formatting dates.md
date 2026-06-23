# Formatting dates

Type: Exercise

## Formatting dates

Load the file **product_prices_cleaned.csv**. The *date* column contains information about the months of value reporting.

1. What date format is it?
2. Change the column format to `datetime64`.
3. Add a new column – *month* to the DataFrame as a way to isolate the information about the month from the *date* column.
4. Add a new column – *quarter* to the DataFrame as a way to isolate the information about the year from the *date* column.
5. Add a new column – *year* to the DataFrame as a way to isolate the information about the quarter from the *date* column.
6. Using the `dt.strfime` method ([link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.strftime.html) to the documentation), convert the  *date* column to the *YYYY-MM-01* format and overwrite its value; e.g.:
  
  ``` 
  df['date'] = col.dt.strftime('format')
  ```
7. Overwrite the *product_prices_cleaned.csv* file. It will be used in the following sections to analyze the collection.
