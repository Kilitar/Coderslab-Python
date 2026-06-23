# Creating tables

Type: Article

> **Note:**
> 
> To create a table in your database, we need to be given the appropriate permissions (this does not apply to temporary tables that we will talk about later).

## Creating a table

The database we are working with has more than a dozen predefined tables. However, there are situations when we want to save the results of a query somewhere, or at the testing stage we create auxiliary tables to save intermediate steps.

To create a table we use the notation:

``` 
CREATE TABLE [IF NOT EXISTS] table_name(
   column_1_name column_1_type,
   column_2_name column_2_type,
   ...
);
```

Where:

- `column_1_name` means the name of table,
- `column_1_type` means the type of table, e.g. bigint,
- `IF NOT EXISTS` only creates the table if it does not exist (optional clause). If we do not add it, and the table exists, an error is generated.

For example:

``` 
CREATE TABLE my_first_table(
    first_col text,
    second_col datetime
)
```

After executing the above query, we can query the table: `SELECT * FROM my_first_table`. At this point, the table is empty.

### Creating tables based on query results

Let's imagine that we create a report, we have a query for it and we want to save the results somewhere in the database so that they do not disappear. Using the basic way of creating tables means that you must first define the columns, their types, and only then feed them.

This approach doesn't make much sense when our output table has a dozen or even tens of dozens of columns. We can make it easier for ourselves by using the following syntax:

``` 
CREATE TABLE [IF NOT EXISTS] table_from_query AS
QUERY
```

> **Note:**
> 
> In the documentation, often the optional parameters of a query are written in curly brackets - as in the `IF NOT EXISTS` example above.

As a `QUERY` we understand any `SQL` expression, such as:

``` 
CREATE TABLE IF NOT EXISTS actor_nick AS
SELECT *
FROM sakila.actor
WHERE first_name = 'NICK'
```

> **Note:**
> 
> Creating tables requires giving special permissions to the user, and we will not be able to create tables in every database.

## Temporary tables

> The rights to create regular tables are not needed in the case of creating temporary ones.

`Temporary tables` are by nature very similar to *normal* tables, but they have one crucial difference - **they only exist while the session is open; once the session is closed they are deleted**.

They are an extremely useful tool in the work of an analyst, when it is often necessary to simultaneously prepare some queries and their results, and combine them later. Thanks to the temporary tables, we can save these results, use them and then use them again, and when the work is finished, the tables will be automatically deleted.

And just like earlier, we can create a temporary table either by defining and feeding it or by using `CREATE .. AS` and directly following `CREATE` with `TEMPORARY`:

Example:

``` 
CREATE TEMPORARY TABLE IF NOT EXISTS tmp_actor_nick AS
SELECT *
FROM sakila.actor
WHERE first_name = 'NICK'
```

At this point we can query our table with a command:

``` 
SELECT *
FROM tmp_actor_nick
```

A good practice when creating temporary tables is prefixing their names with `tmp_`. This approach increases the readability of the code.

In order to streamline your work while creating a solution, you can modify the query as follows:

``` 
DROP TABLE IF EXISTS tmp_actor_nick;
CREATE TEMPORARY TABLE tmp_actor_nick AS
SELECT *
FROM sakila.actor
WHERE first_name = 'NICK'
```

Thanks to `DROP TABLE` the temporary table `tmp_actor_nick` will be deleted and created once again.
