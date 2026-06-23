# Client analysis - part 2

Type: Article

## Client analysis - part 2

Make analyses that answer the questions:

- which area has the most clients,
- in which area the highest number of loans was paid,
- in which area the highest amount of loans was paid,

Select only **owners** of accounts as clients.

## Solution:

> Note: if you use the results of the previous exercise, you need to be careful with `JOIN`, because `district_id` occurs in two tables.

Solution from previous exercises:

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

Here we don't exactly need either gender or age, so we can skip them right away:

``` 
SELECT
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
;
```

Of course, the result of the above query makes little sense, given the requirements of the exercise. At this point, we only get information about the amount of repaid loans and their number.

Now we will add a `district_id` column to meet the requirements. It is in the `district` table; because `district_id` is in the `district`, `account` `client` table we cannot take advantage of the `USING` clause:

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

We can answer the exercise question in many ways. Here we will only give one example. To do so, we are first going to create a temporary table:

``` 
DROP TABLE IF EXISTS tmp_district_analytics;
CREATE TEMPORARY TABLE tmp_district_analytics AS
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

And now we will query to find the results one by one:

- The district with the most customers:
  
  
  
  ``` 
  SELECT *
  FROM tmp_district_analytics
  ORDER BY customer_amount DESC
  LIMIT 1
  ```
- The district with the highest repaid loan amount:
  
  
  
  ``` 
  SELECT *
  FROM tmp_district_analytics
  ORDER BY loans_given_amount DESC
  LIMIT 1
  ```
- The district with the highest number of repaid loans:
  
  
  
  ``` 
  SELECT *
  FROM tmp_district_analytics
  ORDER BY loans_given_count DESC
  LIMIT 1
  ```
