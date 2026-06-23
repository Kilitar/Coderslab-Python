# Loan status

Type: Article

## Loan status

On the database site, we can find information that there are a total of 682 granted loans in the database, of which 606 have been repaid and 76 have not.

Let's assume that we don't have information about which status corresponds to a repaid loan and which does not. In this situation, we need to infer this information from the data.

To do this, write a query to help you answer the question of which statuses represent repaid loans and which represent unpaid loans.

## Solution:

### Verifying the correctness of the information in the documentation.

Before we move on to the core part of the exercise, we will check whether the documentation is true.

To do this exercise, we need to use the `loan` table. The check can be done by counting the number of its rows, e.g. with `COUNT`:

``` 
SELECT count(*) FROM financial.loan -- 682
```

### Actual solution

We already know that the contents of the table match the documentation. According to the requirements, we need to check whether based on the `status` column we can group the loans into paid and unpaid ones.

We are going to use a query written earlier and modify it to group the data according to `status`:

``` 
SELECT 
    status, 
    count(status) 
FROM financial.loan
GROUP BY 1
ORDER BY 1
```

Now the `loan` table is grouped according to loan status, together with the quantity information.

The result of our query is this table:

| status | count(status) |
| --- | --- |
| A | 203 |
| B | 31 |
| C | 403 |
| D | 45 |

From which we can deduce that:

- Paid loans have the `A, C` status; 203 (A) + 403 (C) = 606,
- Unpaid loans have the `B, D` status; 31 (A) + 45 (C) = 76.
