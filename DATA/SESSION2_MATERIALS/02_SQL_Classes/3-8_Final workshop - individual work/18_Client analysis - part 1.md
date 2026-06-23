# Client analysis - part 1

Type: Article

## Client analysis - part 1

Modifying the queries from the exercise on paid loans, answer the following questions:

- Who has more repaid loans - women or men?
- What is the average age of the borrower divided by gender?

> **Hints:**
> 
> 
> 
> - Save the result of the previously written and then modified query, for example, to a temporary table, and conduct the analysis on it.
> - You can calculate the age as the difference: 2021 - the year of birth of the borrower.

## Solution:

Because later we will still want to analyze the number of loans, we need to add a column that is going to allow us to do so, such as `loans_count`:

Query from the previous exercise:

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
WHERE True
    AND l.status IN ('A', 'C')
    AND d.type = 'OWNER'
GROUP BY c.gender
```

Using the `EXTRACT` clause, we will determine the age of the borrower based on the `birth_date` column:

``` 
SELECT
    c.gender,
    2024 - extract(year from birth_date) as age,
   
    -- aggregates
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
GROUP BY c.gender, 2
```

We add another aggregate, i.e. the number of taken loans:

``` 
SELECT
    c.gender,
    2024 - extract(year from birth_date) as age,

    -- aggregates
    sum(l.amount) as loans_amount,
    count(l.amount) as loans_count -- needed later
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
GROUP BY c.gender, 2
;
```

The last thing left is to wrap the query in a temporary table:

``` 
DROP TABLE IF EXISTS tmp_analysis;
CREATE TEMPORARY TABLE tmp_analysis AS
SELECT
    c.gender,
    2024 - extract(year from birth_date) as age,

    -- aggregates
    sum(l.amount) as loans_amount,
    count(l.amount) as loans_count -- needed later
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
GROUP BY c.gender, 2
;
```

To be sure, let's check if everything is correct:

``` 
-- check that the number of loans is correct (606)
SELECT SUM(loans_count) FROM tmp_analysis  
;
```

Now we are able to answer the first question - it comes down to summarizing the earlier table and summing up the `loans_count` column:

``` 
SELECT
    gender,
    SUM(loans_count) as loans_count
FROM tmp_analysis
GROUP BY gender
;
```

Similarly, the part about the age of the borrower:

``` 
SELECT
    gender,
    avg(age) as avg_age
FROM tmp_analysis
GROUP BY gender
;
```
