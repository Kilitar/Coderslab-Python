# Fully paid loans

Type: Article

## Fully paid loans

Find out the balance of repaid loans, divided by client gender.

Additionally, use a method of your choice to check whether the query is correct.

## Solution:

The exercise looks inconspicuous, but to get the answer to this question, you need to make several `JOIN`s, starting from `loan`, and to get the gender information, you need to go through `account` -> `disp` -> `client`.

### Query domain selection.

Since in the exercise conditions we have the information that we are interested only in repaid loans, at the very beginning we will start by selecting only those rows that we're interested in.

From the solution of the exercise about the statuses of loans, we know that the repaid loans are those marked with statuses `('A', 'C')`:

``` 
SELECT *
FROM financial.loan as l
WHERE l.status IN ('A', 'C')
```

### Going through the database schema

In the first part, we will only deal with writing the appropriate join conditions.

Joining `loan` and `account` - here there is no big problem, it can be done directly using the `account_id` column:

``` 
SELECT *
FROM
        financial.loan as l
    INNER JOIN
        financial.account as a USING (account_id)
WHERE l.status IN ('A', 'C')
```

Then, to attach to the current state, we have the `disp` table. It contains the `client_id` column, which we will use later to join with the `client_id` table.

The join to the current result is done via `account_id`, for this reason we will again use the `USING` clause:

``` 
SELECT *
FROM
        financial.loan as l
    INNER JOIN
        financial.account as a USING (account_id)
    INNER JOIN
        financial.disp as d USING (account_id)
WHERE l.status IN ('A', 'C')
```

To get information about the client's gender, we need the `client` table. Here, the join is done on the `client_id` column, which comes from the `disp` table joined before:

``` 
SELECT
    *
FROM
        financial.loan as l
    INNER JOIN
        financial.account a using (account_id)
    INNER JOIN
        financial.disp as d using (account_id)
    INNER JOIN
        financial.client as c using (client_id)
WHERE l.status IN ('A', 'C')
```

### Grouping

At this point we have everything we need, we just need to group by the `gender` column and sum the `amount` column accordingly:

``` 
SELECT
    c.gender,
    sum(l.amount) as amount
FROM
        financial.loan as l
    INNER JOIN
        financial.account a using (account_id)
    INNER JOIN
        financial.disp as d using (account_id)
    INNER JOIN
        financial.client as c using (client_id)
WHERE l.status IN ('A', 'C')
GROUP BY c.gender
```

### Verification

Let's save the results to a temporary table to validate the correctness of the solution:

``` 
DROP TABLE IF EXISTS tmp_results;
CREATE TEMPORARY TABLE tmp_results AS
SELECT
    c.gender,
    sum(l.amount) as amount
FROM
        financial.loan as l
    INNER JOIN
        financial.account a using (account_id)
    INNER JOIN
        financial.disp as d using (account_id)
    INNER JOIN
        financial.client as c using (client_id)
WHERE l.status IN ('A', 'C')
GROUP BY c.gender
```

We can now check if the totals between the tables agree:

``` 
WITH cte as (
    SELECT sum(amount) as amount
    FROM financial.loan as l
    WHERE l.status IN ('A', 'C')    
)
SELECT (SELECT SUM(amount) FROM tmp_results) - (SELECT amount FROM cte)
```

Performing the above query, we will notice that the difference is not equal 0, and consequently, the amount of loans granted was *duplicated*, so there is an error.

The trap lies in the join between `account` and `disp`, where for one `account_id` there can be multiple customers (owner and disponent). To correct this, modify the query, for example:

``` 
DROP TABLE IF EXISTS tmp_results;
CREATE TEMPORARY TABLE tmp_results AS
SELECT
    c.gender,
    sum(l.amount) as amount
FROM
        financial.loan as l
    INNER JOIN
        financial.account a using (account_id)
    INNER JOIN
        financial.disp as d using (account_id)
    INNER JOIN
        financial.client as c using (client_id)
WHERE True
    AND l.status IN ('A', 'C')
    AND d.type = 'OWNER'
GROUP BY c.gender
```

Now for the verification: you can check if something on the way *hasn't escaped* or appeared:

``` 
WITH cte as (
    SELECT sum(amount) as amount
    FROM financial.loan as l
    WHERE l.status IN ('A', 'C')    
)
SELECT (SELECT SUM(amount) FROM tmp_results) - (SELECT amount FROM cte)
```

With which we verify that the exercise was done correctly.
