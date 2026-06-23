# Actors ranking

Type: Exercise

## Actors ranking

Write a query that will create a ranking of actors based on the average rating from the movies they played in.
To do the exercise assume the following:

- use the `actor_analytics` view,
- use the `ROW_NUMBER()` function to create the ranking.

Sort the actors from the best to the worst, e.g.: 1 - highest rating.

Additionally, review the table and see how rows that have the same values are treated.

> **Hints**:
> 
> 
> 
> 1. The `ROW_NUMBER()` function returns the number of the row in a partition,
> 2. You can omit `PARTITION BY` in `OVER()`,
> 3. Example of using `ROW_NUMBER()`:
> 
> 
> ``` 
> SELECT *, ROW_NUMBER() OVER (ORDER BY amount DESC)
> FROM payment
> ```
