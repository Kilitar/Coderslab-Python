# Unpaid rentals

Type: Exercise

## Unpaid rentals

Using `tasks.payment` and `sakila.rental` tables find unpaid rentals (those with no payment).

What type of `JOIN` should be used here? Can you find more than one solution of this exercise?

> **Hint:**
> 
> After performing a `JOIN`, you can confidently filter the rows created **after the join**, for example:
> 
> 
> 
> ``` 
> SELECT *
> FROM
>        tabl1 as t1
>    RIGHT JOIN
>        tabl2 as t2 USING (key)
> WHERE t1.col_name > 0
> ```
