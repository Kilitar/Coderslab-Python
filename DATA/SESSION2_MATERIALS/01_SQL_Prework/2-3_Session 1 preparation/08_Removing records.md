# Removing records

Type: Article

## `DELETE`

We remove data from the table using the `DELETE` clause:

``` 
DELETE FROM table_name
WHERE some_column = some_value;
```

> `DELETE` is used together with the `WHERE`clause (otherwise all the records from the table would be deleted).

### Example

Let's assume all of the students with the first name Marianne quit school. You can remove them from the table as follows:

``` 
-- Removing all Mariannes from the database
DELETE FROM example.students
WHERE name = "Marianne"
```

We can also sort the elements or limit the amount of deleted data before deleting (we don't have to combine this):

``` 
-- Removing from the database only the first 2 students without a given id
DELETE FROM example.students
WHERE id IS NULL -- deleting students with no ID assigned
ORDER BY name -- setting order of record deletions
LIMIT 2  -- setting limit of deletions
```

## `TRUNCATE`

An alternative to `DELETE` is `TRUNCATE`. Not unlike `DELETE`, it deletes data from the table but in this case **all table content is cleared** without exception.

Use:

``` 
TRUNCATE table_name
```

It is equivalent to the command:

``` 
DELETE FROM table_name 
WHERE True
```

From the point of view of a data analyst the key difference between `TRUNCATE` and `DELETE` is that `TRUNCATE` clears the entire table, which makes it much faster than deleting *row by row* as in the case of `DELETE`.
