# Pivot table

Type: Exercise

## Pivot table

Using the data from the  **product_prices_cleaned.csv** file do the following:

1. Create a pivot table so that the rows hold years, and columns have names of goods. Use the average price of the product as the value.
2. Using `lambda` and `pivot_table`, recreate the view of the data discussed during the lecture. Analyse the result of the recreation. What can you say about what was passed to the function?
3. Using `pivot_table`, see how the mean and median prices in the product groups were shaped across years (many functions can be passed as a list).

> **Subsection 2 hint:**
> 
> 
> 
> 
> Code from the lecture:
> 
> 
> 
> ``` 
> pd.pivot(data=df, index=['province', 'product'], columns=['date'], values=['value'])
> ```
