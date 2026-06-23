# Multiple grouping

Type: Exercise

## Multiple grouping

It is also possible to group by multiple columns. The result will always be grouped in the order in which the columns are entered (from left to right).

For example, if you want to find out how many orders in each status are assigned to each company, you can create a SQL query:

``` sql
SELECT customerName, status, count(status) FROM customers
JOIN orders ON orders.customernumber = customers.customernumber
GROUP BY customername, status
ORDER BY customername;
```

Based on this query, find out, how many employees with a particular `jobtitle` are in each office.
