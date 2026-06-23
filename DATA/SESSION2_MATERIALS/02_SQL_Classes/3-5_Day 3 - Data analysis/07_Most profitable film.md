# Most profitable film

Type: Exercise

## Most profitable film (summary)

Prepare a report that displays the top 10 most rented films. Make the following business assumptions to prepare the report:

- film title,
- number of actors who played in it,
- the amount of revenue of the film,
- number of film rentals.

Additionally, make sure that the amount you get for all films is correct (before you limit the results).

> **Hint**:
> This task is quite complex and requires several joins. You can make your work easier by using queries from previous tasks.

## `LIMIT`

To restrict the results of the query you can use the `LIMIT` clause that returns the first `n` rows; for example:

``` 
SELECT * FROM payments LIMIT 10 -- returns the first 10 rows
```
