# Payments and rentals

Type: Exercise

## Payments and rentals

Write a join for `rental` and `payment` tables. Display only the following columns:

- payment_id,
- rental_id,
- amount,
- rental_date,
- payment_date.

Use `INNER JOIN` in this exercise.

> Remember to use **aliases** for the tables in the query.

> This and the next 2 exercise will be the components for our first rental report.

> **Note:**
> 
> If two tables have the same column names, `SQL` will need to know which table we want to display the column from (we can use aliases), for example:
> 
> 
> 
> ``` 
> SELECT 
>     t.col_name
> FROM tab as t
> ```
