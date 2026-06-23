# Prework revision

Type: Article

In this article you will find a summary of the most commonly used queries and SQL language constructs for selecting data.

## Selecting data

To pick data from the database, use the `SELECT` command:

``` sql
SELECT
  columns separated by commas, or * to retrieve all
FROM
  table name
;
```

Examples:

``` sql
SELECT customerName, phone FROM customers;
```

``` sql
SELECT * FROM customers
```

The above queries are simple and do not require a more detailed indication of columns. This will not always be the case; sometimes you'll need to indicate which table a column comes from - a dot character can then be used to separate the table name from the column name:

``` sql
SELECT customers.customerName, customers.phone FROM customers;
```

We can extend the `SELECT` queries with conditions that rows need to meet to be qualified as search results:

``` sql
SELECT
  which columns or use * to take all
FROM
  table name
WHERE
  condition, or more conditions combined using AND or OR
;
```

Examples:

``` sql
SELECT * FROM customers WHERE city = 'Singapore';
```

``` sql
SELECT * FROM customers WHERE city = 'Singapore' AND creditlimit > 50000;
```

The results selected with the `SELECT` command can be sorted:

``` sql
SELECT
  which columns or use * to take all
FROM
  table name
WHERE
  conditions
ORDER BY
  The column by which the results are to be sorted
ASC or DESC
;
```

Examples:

``` sql
SELECT * FROM customers ORDER BY creditlimit;
```

``` sql
SELECT * FROM customers ORDER BY creditlimit ASC;
```

``` sql
SELECT * FROM customers WHERE city = 'Singapore' ORDER BY creditlimit DESC;
```

If any of the queries shown here are not clear, read the SQL prework again.
