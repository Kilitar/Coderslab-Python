# Automation for analysts

Type: Exercise

## Automation for the analyst

A team of analysts prepares the monthly report on the prices of the product selected by the Board. Because they are aware you know Python, they asked you to automate the process. Talking to the team, you have set the following business conditions that enable process automation:

Three report parameters are available:

- **product_group_id**,
- **product**,
- **date**.

Assumptions for each parameter:

1. A parameter may have at most one value,
2. If the parameter is empty we return all records from the group,
3. We assume that the file is always prepared correctly (we want to practice report automation, not error handling).

Based on the above requirements:

1. Load the  **config.xlsx** file using `openpyxl`,
2. Prepare appropriate conditions to filter data from **product_cleaned.csv**,
3. Based on the conditions filter the frame,
4. Aggregate the data using a **pivot_table**:
  
  1. index - product, province,
  2. columns - dates,
  3. value - average product price,
  4. remember to remove 0,
5. Save the file to the spreadsheet any way you want.

Hints:

1. You can save individual filtering conditions to variables and then use them all to filter `DataFrame`: the same as writing them all as before i.e. `df.loc[var1 & var2]`
2. If you decide to write with Pandas, be careful with the parameters passed to the function (what happens if you set `index=False`?). Link to the [documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html).
