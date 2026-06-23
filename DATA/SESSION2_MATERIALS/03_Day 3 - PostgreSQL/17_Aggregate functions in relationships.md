# Aggregate functions in relationships

Type: Exercise

## Aggregate functions in relationships

Aggregate functions can also be used together with relationships. For example, if we want to find out the number of items ordered from each production line, we can write the following SQL query:

``` sql
SELECT productlines.productLine, sum(quantityOrdered) from productlines
JOIN products ON products.productline = productlines.productline
JOIN orderdetails ON orderdetails.productcode = products.productcode
GROUP BY productlines.productline
```

Based on this query, find out:

1. What is the total amount of orders for each of the product lines (`sum(quantityordered * priceEach)`)?
2. What is the total of payments made by each company (the query should also return the name of that company)?
3. How many total items did each company order?
