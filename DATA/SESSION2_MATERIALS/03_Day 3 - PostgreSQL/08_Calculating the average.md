# Calculating the average

Type: Exercise

## Calculating the average

Using Python calculate the average purchase price (`buyPrice`) of a product.

To do so:

1. Create a database connection object.
2. Query the database for all products (the query can be narrowed down to the purchase price).
3. In a loop, iterate all the results and sum them up.
4. After summing up all the results, divide them by the number of rows returned.

> **Hint:**
> 
> 
> 
> 
> To get the number of returned rows you can use the `cursor` object called `rowcount`.
> 
> 
> 
> ``` 
> rows_count = my_coursor.rowcount
> ```
