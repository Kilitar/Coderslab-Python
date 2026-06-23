# Client analysis - part 3

Type: Article

## Client analysis - part 3

Use the query created in the previous task and modify it to determine the percentage of each district in the total amount of loans granted.

Sample result:

| district_id | customer_amount | loans_given_amount | loans_given_count | amount_share |
| --- | --- | --- | --- | --- |
| 1 | 73 | 100 | 2 | 0.6666 |
| 74 | 17 | 50 | 5 | 0.3333 |

> In other words, the task is to determine the distribution of granted loans by region.

## Solution:

Of course there are many ways to do this exercise.

We will present a sample approach using a window function - then you just need to add the query from the previous part of the exercise in the form of a subquery, and then apply a window function that determines the total amount of granted loans:

### Query from the previous exercise:

``` 
SELECT
    d2.district_id,

    count(distinct c.client_id) as customer_amount,
    sum(l.amount) as loans_given_amount,
    count(l.amount) as loans_given_count
FROM
        financial.loan as l
    INNER JOIN
        financial.account a using (account_id)
    INNER JOIN
        financial.disp as d using (account_id)
    INNER JOIN
        financial.client as c using (client_id)
    INNER JOIN
        financial.district as d2 on
            c.district_id = d2.district_id
WHERE True 
    AND l.status IN ('A', 'C')
    AND d.type = 'OWNER'
GROUP BY d2.district_id
;
```

### Subquery

At this point we will define a CTE and use it in the query:

``` 
WITH cte AS (
    SELECT
        d2.district_id,

        count(distinct c.client_id) as customer_amount,
        sum(l.amount) as loans_given_amount,
        count(l.amount) as loans_given_count
    FROM
            financial.loan as l
        INNER JOIN
            financial.account a using (account_id)
        INNER JOIN
            financial.disp as d using (account_id)
        INNER JOIN
            financial.client as c using (client_id)
        INNER JOIN
            financial.district as d2 on
                c.district_id = d2.district_id
    WHERE True 
        AND l.status IN ('A', 'C')
        AND d.type = 'OWNER'
    GROUP BY d2.district_id
    ;
)
SELECT *
FROM cte
```

At this point we will use the window function, because we want to determine the distribution we will sum the total amount of loans with:

- `SUM(loans_given_amount) OVER ()` - which returns the total amount of given loans.

In the end we get:

``` 
WITH cte AS (
    SELECT d2.district_id,

           count(distinct c.client_id) as customer_amount,
           sum(l.amount)               as loans_given_amount,
           count(l.amount)             as loans_given_count
    FROM 
            financial.loan as l
        INNER JOIN
            financial.account a using (account_id)
        INNER JOIN
            financial.disp as d using (account_id)
        INNER JOIN
            financial.client as c using (client_id)
        INNER JOIN
            financial.district as d2 on
                c.district_id = d2.district_id
    WHERE True
      AND l.status IN ('A', 'C')
      AND d.type = 'OWNER'
    GROUP BY d2.district_id
)
SELECT
    *,
    loans_given_amount / SUM(loans_given_amount) OVER () AS share
FROM cte
ORDER BY share DESC
```

Preview the result (first 5 rows):

| district_id | customer_amount | loans_given_amount | loans_given_count | share |
| --- | --- | --- | --- | --- |
| 1 | 73 | 10502628 | 73 | 0.1198 |
| 74 | 17 | 2906652 | 17 | 0.0332 |
| 54 | 18 | 2784744 | 18 | 0.0318 |
| 64 | 15 | 2671872 | 15 | 0.0305 |
| 70 | 22 | 2354520 | 22 | 0.0269 |
