# Group by

Type: Exercise

## Group by

Run the following SQL query on your database:

``` sql
select * from products GROUP by productline
```

Do you understand what error was returned by the database?

Now try running the following SQL query on your database:

``` sql
select count(*) from products GROUP by productline;
```

Does the query now work properly? Why? What information can be extracted from it? What other columns would be useful for the query to give us more information?
