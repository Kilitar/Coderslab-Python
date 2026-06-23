# Film rental

Type: Exercise

## Film rental

Based on the analogy with a bank transaction, write a `film_rental` procedure that uses the table `trigger_exercise.stock_part_1` to check whether a given `film_id` can be rented - if so, reduce the stock by one and return 1, otherwise return 0.

Example of use:

``` 
CALL film_rental(1)
```

Take advantage of the transaction mechanism here by following the steps below:

1. First write a query that finds the film and reduces its stock by 1,
2. If the film is found and its count is sufficient to be rented, approve the transaction.
3. Otherwise, cancel it.
