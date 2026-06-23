# Selection - part 1

Type: Article

## Client selection

Check the database for the clients who meet the following results:

- their account balance is above 1000,
- they have more than five loans,
- they were born after 1990.

And we assume that the account balance is `loan amount` - `payments`.

## Solution:

Again, we can use the query that was developed earlier, in this case it is about the appropriate use of `HAVING` and the appropriate group selection.

### Query from previous exercises

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

### Domain modification

Having the query, we can proceed to the next part, which is the selection of the appropriate domain. We know from the exercise conditions that we are concerned with clients who were born after 1990.

Of course, the earlier analyses were done at the district level; now we will modify the query to analyze the client:

``` 
SELECT
    c.client_id,

    sum(amount - payments) as client_balance,
    count(loan_id) as loans_amount
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
    AND EXTRACT(YEAR FROM c.birth_date) > 1990
GROUP BY c.client_id
;
```

### Filtering groups

With the domain established, we can write the appropriate group filtering conditions using `HAVING`:

``` 
SELECT
    c.client_id,

    sum(amount - payments) as client_balance,
    count(loan_id) as loans_amount
FROM loan as l
         INNER JOIN
     account a using (account_id)
         INNER JOIN
     disp as d using (account_id)
         INNER JOIN
     client as c using (client_id)
WHERE True
  AND l.status IN ('A', 'C')
  AND d.type = 'OWNER'
GROUP BY c.client_id
HAVING
    SUM(amount - payments) > 1000
    AND COUNT(loan_id) > 5
```

After execution, we will find that the result set is empty, that is, the criteria have been ill-defined. The analysis of this problem is the subject of the next exercise.
