# Selection - part 2

Type: Article

## Selection part 2

From the previous exercise you probably already know that there are no customers who meet the requirements. Make an analysis to determine which condition caused the empty results.

## Solution:

> TL;DR - maximum number of loans per client is 1

The easiest way to do this is to comment out the subsequent components of the query and see when the data starts to appear.

In this case, after commenting out the following conditions

``` 
AND EXTRACT(YEAR FROM c.birth_date) > 1990 -- for WHERE
AND count(loan_id) > 5 -- for HAVING
```

Results will appear; and modifying the previous query as follows:

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
--  AND EXTRACT(YEAR FROM c.birth_date) > 1990
GROUP BY c.client_id
HAVING
    sum(amount - payments) > 1000
--    and count(loan_id) > 5
ORDER BY loans_amount DESC -- here we add descending sorting by number of loans
```

will allow us to find that customers have at most one loan.
