# Duplicates

Type: Exercise

## Duplicates

Using the **product_prices_renamed.csv** files:

1. check how many rows are duplicated,
2. using `duplicated` check which rows were doubled.
3. using `drop_duplicates`, remove all duplicates from the output dataset (we assume that a row with a duplicate is an error and needs to be removed) – write the result to a new DataFrame.

> **Hints:**
> 
> 
> 
> 
> #### Subsection 2:
> 
> 
> 
> 
> To determine, the number of duplicate rows use the source data and the results from subsection 1.
> 
> 
> 
> 
> #### Subsection 3:
> 
> 
> 
> 1. first use `duplicated`, to find duplicated rows,
> 2. Use `loc` to separate them from the output set,
> 3. Use `drop_duplicates` to get only those rows that are duplicated.
