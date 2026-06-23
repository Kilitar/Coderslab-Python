# Rental report

Type: Exercise

## Rental report

Using the queries and the joining method from the previous tasks, write a query that returns the following information about the rental:

- rental id,
- film id,
- film title,
- film description,
- film rating,
- rental rating,
- rental date,
- payment date,
- payment amount.

Name the columns so that a person who opens the report for the first time has no problem understanding the meaning and does not need to guess what a name such as `title` refers to.

> **Hint:**
> 
> The syntax for joining multiple tables is similar to joining two. You just need to add another join, e.g.:
> 
> 
> 
> ``` 
> SELECT 
>   t1.col_name,
>   t2.col_name2,
>   t3.col_name3
> FROM
>        tab1 AS t1
>    [INNER|LEFT|RIGHT] JOIN 
>        tab2 AS t2 ON t1.key1 = t2.key1
>    [INNER|LEFT|RIGHT] JOIN
>        tab3 AS t3 ON t2.key2 = t3.key3
> ```
