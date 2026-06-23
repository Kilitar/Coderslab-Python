# Rollup and having

Type: Exercise

## `ROLLUP` and `HAVING`

Based on the `payment` table write a query that:

- determines the sum of payments divided by client and by employee,
- determines the sum of payments per client,
- determines the sum of payments.

Do two versions of the exercise:

1. Using only `ROLLUP`,
2. Adding the `HAVING` clause to the `GROUP BY` for payments above 70.

How are the results of the queries different? To make it easier to notice the difference, do the exercise only for the first 3 customers (`customer_id` < 4).

### Expected result (sample)

``` 
+-----------+--------+-----------+
|customer_id|staff_id|payments   |
+-----------+--------+-----------+
|1          |1       |64.83      |
|1          |2       |53.85      |
|NULL       |NULL    |383.15     |
+-----------+--------+-----------+
```
