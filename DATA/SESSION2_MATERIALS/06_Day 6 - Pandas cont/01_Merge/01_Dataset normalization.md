# Dataset normalization

Type: Exercise

## Dataset normalization

In the sheets of the **dims.xlsx** file there are dictionaries for the data from the **product_prices_cleaned.csv** file. Use `merge` to normalize the data following the steps:

1. Read the contents of the **dims.xlsx** file sheets to separate `DataFrames`.
  For readability base names of frames on the names of sheets.
2. Read the data from **product_prices_cleaned.csv** file to the `df` variable.
3. Based on the **d_province** workbook, use the `id` column to add the `province_id` column to the `df` frame.
4. Based on the  **d_product** workbook, add the `product_id` column to the `df` frame.
5. From the table, extract only the columns that refer to other tables, e.g.. **product_id** and the columns **value**, **date**. Do you think this is more readable? What are potential benefits of this approach?

> We will tell you how to read many workbooks at once when we discuss `openpyxl`.

You can find more about database normalization at the [link](https://www.sqlshack.com/what-is-database-normalization-in-sql-server/).
