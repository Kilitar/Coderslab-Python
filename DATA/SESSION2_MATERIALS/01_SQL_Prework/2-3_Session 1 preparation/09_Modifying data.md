# Modifying data

Type: Article

## Updating / modifying data in a table

## `UPDATE`

We modify the data in the table using `UPDATE`:

``` 
UPDATE [LOW_PRIORITY] [IGNORE] table_name
SET
col_name_1 = value1,
col_name_2 = value2,
...
WHERE col_name_3 = some_value;
```

> We always use `UPDATE` with a `WHERE` clause (otherwise all the data in the table will be changed).

- `LOW_PRIORITY` - enables postponing the update until nobody is reading data from the table,
- `IGNORE` - works the same here as with inserts, a single error does not stop the operation.

### Example:

Let's assume a mistake was made while adding students to the system, and the student with `id=10` got an incorrect name. This can be solved using the `UPDATE` clause, that modifies the particular row.

### Data before update

``` 
SELECT * 
FROM examples.students
WHERE id = 10
```

| id | name | surname | email | class_id |
| --- | --- | --- | --- | --- |
| 10 | Jack | Koval | jack@gmail.com | 1 |

### Updating data

Now we are going to use the `UPDATE` clause to change Jack to Jake:

``` 
UPDATE examples.students 
SET name="Jake" 
WHERE id=10;
```

### Data after update

``` 
SELECT * 
FROM examples.students
WHERE id = 10
```

| id | name | surname | email | class_id |
| --- | --- | --- | --- | --- |
| 10 | Jake | Koval | jacek@gmail.com | 1 |
