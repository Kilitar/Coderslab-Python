# Cumulative sum

Type: Exercise

## Cumulative sum

Cumulative sum (often shortened to cumsum), as the name suggests, refers to the cumulative amount; window functions let us count according to a specified order: this is done using the `ORDER BY` clause.

In a sense `ROW_NUMBER()` was already an example of a cumsum regarding the count of elements in a partition.
In statistics this approach can be used to determine e.g. a [cumulative distribution function](https://sheetaki.com/how-to-plot-a-cdf-in-excel/)

Our task is going to be to write a clause that determines the following accumulating values.

- `MIN` for `avg_film_rate`,
- `SUM` for `actor_payload`,
- `MAX` for `longest_movie_duration`.

Use `actor_id` as a sorting key - ascending.

> **Hint:**
> Appropriately modify the code below:
> 
> 
> 
> ``` 
> SELECT 
>     *
>     , ROW_NUMBER() OVER (ORDER BY actor_id) 
> FROM sakila.actor_analytics
> ```
