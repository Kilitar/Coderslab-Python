# Analysis of accounts

Type: Article

## Analysis of accounts

Write a query that ranks accounts according to the following criteria:

- number of given loans (decreasing),
- amount of given loans (decreasing),
- average loan amount,

Only **fully paid** loans are considered.

## Solution:

Based on the exercise conditions, it is enough to use the `loan` table, but we need to consider two elements:

1. grouping rows by `account_id`,
2. ranking the results of the previous query.

That is, the task must be performed in two steps. For example we can use a subquery, and then add a window function to get the result.

### Subquery

We will start solving the exercise by creating a query for the subquery. As the first step, we will start by properly filtering the rows in the `loan` table:

``` 
SELECT *
FROM financial.loan
WHERE status IN ('A', 'C')  -- only granted loans
;
```

The previous exercise tells us that `('A', 'C')` statuses together define the domain of paid loans. Now we will move on to grouping by account, i.e. `account_id`:

``` 
SELECT 
    account_id
FROM financial.loan
WHERE status IN ('A', 'C')  -- only granted loans
;
```

All that remains is to determine the appropriate statistics for a given account:

- sum of paid loan amounts: `sum(amount)`,
- number of paid loans: `count(amount)`,
- average amount of paid loans: `avg(amount)`.

``` 
SELECT
    account_id,
    sum(amount)   as loans_amount,
    count(amount) as loans_count,
    avg(amount)   as loans_avg
FROM financial.loan
WHERE status IN ('A', 'C')  -- only granted loans
GROUP BY account_id
```

All that is left now is to define a CTE and use it in the query:

``` 
WITH cte as (
    SELECT
        account_id,
        sum(amount)   as loans_amount,
        count(amount) as loans_count,
        avg(amount)   as loans_avg
    FROM financial.loan
    WHERE status IN ('A', 'C')  -- only granted loans
    GROUP BY account_id
)
SELECT *
FROM cte
```

We will use the subquery created this way to denote the ranking.

### Ranking

We move on to ranking the accounts according to the set criteria. For this we will use `ROW_NUMBER` and the previously created subquery to which we will add:

- `ROW_NUMBER() OVER(ORDER BY loans_amount DESC)` - the result of this formula will rank **all** `account_id` based on the loan amount from high to low,
- `ROW_NUMBER() OVER(ORDER BY loans_count DESC)` - the result of this formula will rank **all** `account_id` based on the number of loans from high to low,

Finally, after modifications, we get the following query:

``` 
WITH cte AS (
    -- first step, i.e. aggregating the data to the account_id level
    SELECT
       account_id,
       sum(amount)   as loans_amount,
       count(amount) as loans_count,
       avg(amount)   as loans_avg
    FROM financial.loan
    WHERE status IN ('A', 'C')  -- only granted loans
    GROUP BY account_id
)
SELECT
    *,
    -- ranking
    ROW_NUMBER() over (ORDER BY loans_amount DESC) AS rank_loans_amount,
    ROW_NUMBER() over (ORDER BY loans_count DESC) AS rank_loans_count
FROM cte
```

Of course, you might as well use another rank function, such as `RANK` or `DENSE_RANK`, nevertheless, from a technical point of view, `ROW_NUMBER` also solves the exercise.
