# SQL basics

Type: Article

In this article we will get to know the most basic `SQL` commands , including:

- `SELECT` - used to display table columns,
- `WHERE` - used to filter rows,
- `ORDER BY` - used to sort the output data,
- `DISTINCT` - used to display the **unique** rows.

Before we go any further, however, we can't do without the classic *Hello world*. In the case of `SQL` it looks like this:

``` 
SELECT 'Hello world'
```

It is also worth mentioning that `SELECT` is going to start every query aiming to retrieve information from a table.

## `SELECT`

As we have already said, `SELECT` is the absolute foundation: it is mostly used to retrieve information from a table. The most primitive command call on a table is the following example, which we will analyze in a moment:

``` 
SELECT * FROM sakila.inventory
```

> Remember to adjust the query according to your database user. For an explanation, see **Course preparation > Connecting to the CodersLab database > Executing SQL queries on the server**.

Query result;

![select * from](/presentations/DTL/en/4.9/W/M_02_S_02/0b2aba6b-486d-43bb-a0b9-bcc5d2658671/student_content/a4e4baca-8916-42a0-8a04-4c77bcf8801a/./images/select.png)

##### (result fragment)

The query results in are all the columns and rows from the `sakila.inventory` table.

The above query reads as follows:

1. `SELECT` - informing the database engine that we want to display some data,
2. `*` - asterisk symbol means **all columns in the table** (more details soon),
3. `FROM sakila.inventory` - we specify which table we want to take the data from.

So the basic syntax of `SELECT` is this:

``` 
SELECT * FROM table_name
```

Of course, selecting all columns is not always required. When we are only interested in a range, we can use the following syntax:

``` 
SELECT
    col_name_1,
    col_name_2
FROM table_name
```

Where `col_name_1`, and `col_name_2` mean the column names present in the `table_name` table.

> We start all the table queries from the `SELECT` clause!

## `WHERE`

As we have said before, `WHERE` clause is used to select only those results we are interested in at the moment. For example, the query:

``` 
SELECT * FROM sakila.actor
WHERE first_name = 'PENELOPE'
```

is going to return all data from `sakila.actor` for rows where `first_name` is *PENELOPE*.

Query result;
![select * from](/presentations/DTL/en/4.9/W/M_02_S_02/0b2aba6b-486d-43bb-a0b9-bcc5d2658671/student_content/a4e4baca-8916-42a0-8a04-4c77bcf8801a/./images/where.png)

In general, the `WHERE` syntax is:

``` 
SELECT 
    col_name_1,
    col_name_2
FROM table_name
WHERE col_name_1 = <searching_value>
```

> In the `WHERE` clause it is not necessary to use the columns, which are already defined in the  `SELECT` clause.

> **Note:**
>  All strings that must be treated literally by`SQL` need to be surrounded with single quotes (apostrophe character ').

### Relational operators

Below we list basic logical operators for the `WHERE` clause:

| Operator | Description | Example |
| --- | --- | --- |
| = | Equal | SELECT * sakila.actor WHERE first_name = 'NICK'; |
| <> | Not equal  (new versions can also use !=) | SELECT * FROM sakila.actor WHERE first_name <> 'NICK'; |
| > | Greater than | SELECT * FROM sakila.payment WHERE amount > 5; |
| >= | Greater or equal | SELECT * FROM sakila.payment WHERE amount >= 5; |
| < | Less than | SELECT * FROM sakila.payment WHERE amount < 100; |
| <= | Less or equal | SELECT * FROM sakila.payment WHERE amount <= 100; |
| BETWEEN a AND b | In the specified range (including the limit) | SELECT * FROM sakila.payment WHERE amount BETWEEN 5 and 100; |
| IS NULL | equal to NULL | SELECT * FROM sakila.actor WHERE first_name IS NULL; |
| IN(a, b, c) | Found among the variables given in parentheses | SELECT * FROM sakila.actor WHERE first_name IN ('NICK', 'JOHNNY'); |
| NOT IN(a, b, c) | Not found among the variables given in parentheses | SELECT * FROM sakila.actor  WHERE first_name NOT IN ('NICK', 'JOHNNY'); |
| LIKE | Searches for the specified pattern (strings only, e.g. name: NICK) |  |
|  | 'De%' – column value starting from 'De' | SELECT * FROM sakila.actor WHERE first_name LIKE 'De%'; |
|  | '%ter' – column value ending with 'ter' | SELECT * FROM sakila.actor WHERE first_name LIKE '%ter'; |
|  | '%exte%' – column value includes 'exte' | SELECT * FROM sakila.actor  WHERE first_name LIKE '%exte%'; |

Additionally there are `AND`, `OR` and `NOT`, operators but we are going to discuss them in detail in the next article.

## `ORDER BY`

The `ORDER BY` clause is used to sort results according to one or more columns. For example, if we want to sort the table with actors by first name and last name we will write:

``` 
SELECT * 
FROM sakila.actor
ORDER BY first_name, last_name
```

Query result;

![order by](/presentations/DTL/en/4.9/W/M_02_S_02/0b2aba6b-486d-43bb-a0b9-bcc5d2658671/student_content/a4e4baca-8916-42a0-8a04-4c77bcf8801a/./images/order_by.png)

##### (result fragment)

> Default `ORDER BY` sorting is ascending (`ASC`). If we want to sort in the descending order, we need to add `DESC` after the column name.

In general the `ORDER BY` syntax is:

``` 
SELECT 
    col_name_1,
    col_name_2
FROM table_name
ORDER BY
col_name_1 ASC, col_name_2 DESC, col_name_3
```

In `MySQL` it is also allowed to use column number instead of its name:

``` 
SELECT * 
FROM sakila.actor
ORDER BY 2 ASC, 3 -- alternatively for first_name, last_name
```

> `--` is a comment in `SQL`

## `DISTINCT`

The `DISTINCT` clause is used to retrieve the unique rows from the table and is written directly after `SELECT`. Wanting to get all unique names of actors, we should write:

``` 
SELECT DISTINCT first_name
FROM sakila.actor
```

Query result;
![distinct](/presentations/DTL/en/4.9/W/M_02_S_02/0b2aba6b-486d-43bb-a0b9-bcc5d2658671/student_content/a4e4baca-8916-42a0-8a04-4c77bcf8801a/./images/distinct.png)

##### (result fragment)

If we wanted to get a unique list of first names and last names:

``` 
SELECT DISTINCT 
    first_name,
    last_name
FROM sakila.actor
```

Query result;

![distinct2](/presentations/DTL/en/4.9/W/M_02_S_02/0b2aba6b-486d-43bb-a0b9-bcc5d2658671/student_content/a4e4baca-8916-42a0-8a04-4c77bcf8801a/./images/distinct2.png)

##### (result fragment)

In general:

``` 
SELECT DISTINCT
    col_name_1,
    col_name_2,
FROM table_name
```

## `LIMIT`

Sometimes we want to limit the result of the query and only preview the contents of the result. If we do not want to display all data, which sometimes can take more time than the query itself, we can use the `LIMIT` clause that returns the first `n` rows.

Example:

``` 
SELECT DISTINCT first_name
FROM sakila.actor
LIMIT 5 -- displays only first 5 rows
```

## Comments

`SQL` allows two comment formats:

``` 
-- single-line comment

/*
multi-line comment
*/
```

## Joining all clauses into one query

We already know the most basic `SQL` clauses. Now we can deal with the basic queries. But how does it all come together if we want to use them all at once?

**Exercise:**

Find all names of the clients of the `sakila` database, who are active; sort the results alphabetically in descending order.

**Solution:**

``` 
SELECT DISTINCT first_name
FROM sakila.customer
WHERE active = 1
ORDER BY first_name DESC
-- LIMIT 10 -- if we wanted to limit the query results
```

Let's pay attention to the order of the given clauses:

1. `SELECT`,
2. `DISTINCT`,
3. `WHERE`,
4. `ORDER BY`,
5. `LIMIT`.

> **Note:** 
>  Specifying clauses in an order other than the above will cause syntax errors.

## Summary

In this article we learned basic `SQL` syntax. We know how to display the contents of the entire table or filter them out as needed.

We wrote the first query! It is composed of all the elements we learned and displays a unique list of names of active customers from our database.
