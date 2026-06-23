# Grouping data across sheets

Type: Exercise

## Grouping data across sheets

Modify the previous exercise so that each product group is in a separate worksheet together with the corresponding `product_group_id`. For example
`product_group_id` 1 should go to the sheet named `1`.

Use the method to create a new workbook:

``` 
wb.create_sheet(name, index)
```

Where:

- `name` - is the name of the workbook, where we want to save the data (should be a string),
- `index` - is the worksheet position in the workbook.
