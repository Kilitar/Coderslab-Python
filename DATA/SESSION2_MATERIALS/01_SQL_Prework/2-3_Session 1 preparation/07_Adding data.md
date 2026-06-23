# Adding data

Type: Article

## `INSERT INTO`

Data is added to the table using the `INSERT INTO` query:

``` sql
INSERT INTO table_name (col_name_1, col_name_2, col_name_3, ...)
VALUES (value1, value2, value3, ...);
```

Where:

- `table_name` - is the name of the table,
- `col_name_1, col_name_2, ...` - names of columns,
- `value1, value2, ...` - values,

If we do not specify column names after the table name, the data will be written to the subsequent columns of the table (according to its definition):

``` sql
INSERT INTO table_name VALUES (value1, value2, value3, ...);
```

Later on we are going to use the `examples.students` table, with the following columns:

1. `id` - student's id,
2. `name` - student's first name,
3. `surname` - student's family name,
4. `email`,
5. `class_id` - id of student's class.

``` 
SELECT * FROM examples.students
```

At this stage, the table should be empty:

``` 
+----+------+-------+----------------+--------+
|id  |name  |surname|email           |class_id|
+----+------+-------+----------------+--------+
```

#### Example 1:

``` sql
INSERT INTO students VALUES (10, 'Jack', 'Koval', 'jack@gmail.com', 1);
```

Checking table contents:

``` 
+--+-----+--------+---------------+--------+
|id|name |surname |email          |class_id|
+--+-----+--------+---------------+--------+
|10|Jack |Koval   |jack@gmail.com |1       |
+--+-----+--------+---------------+--------+
```

#### Example 2:

``` sql
INSERT INTO students VALUES ('Walter', 'walter@gmail.com');
```

In this case we will get an error:

``` text
ERROR:  invalid input syntax for integer: 'Walter'
LINE 1: INSERT INTO students VALUES ('Walter', 'walter@gmail.com');
```

The error is caused by the fact that the number of columns (5) is not equal to the number of passed data (2).

> You can find more information on `INSERT INTO` in the [official documentation](https://dev.mysql.com/doc/refman/8.0/en/insert.html).

#### Example 2 - corrected

To correct example 2, specify the names of the columns to be completed:

``` 
INSERT INTO students (name, email) VALUES('Walter', 'walter@gmail.com');
```

Checking table contents:

``` 
+----+------+--------+----------------+--------+
|id  |name  |surname |email           |class_id|
+----+------+--------+----------------+--------+
|10  |Jack  |Koval   |jack@gmail.com  |1       |
|NULL|Walter|NULL    |walter@gmail.com|NULL    |
+----+------+--------+----------------+--------+
```

## Adding multiple rows at once

If we have a whole list of rows to load at once, we can do it with the command:

``` 
INSERT INTO table_name (column_list)
VALUES
    (value_list_1),
    (value_list_2),
    ...
    (value_list_n);
```

#### Example:

``` sql
INSERT INTO students VALUES 
   (11, 'Marianne', 'Koval', 'funkykoval@gmail.com', 1),
   (12, 'Jerry', 'Newman', 'jn@gmail.com', 2);
```

``` 
SELECT * FROM students;
+----+---------+--------+--------------------+--------+
|id  |name     |surname |email               |class_id|
+----+---------+--------+--------------------+--------+
|10  |Jack     |Koval   |jack@gmail.com      |1       |
|NULL|Walter   |NULL    |walter@gmail.com    |NULL    |
|11  |Marianne |Koval   |funkykoval@gmail.com|1       |
|12  |Jerry    |Newman  |jn@gmail.com        |2       |
+----+---------+--------+--------------------+--------+
```

For very large amounts of data, the limit may be important:

``` 
SHOW VARIABLES LIKE 'max_allowed_packet'; -- 16GB on my computer
```

Which we change with the command:

``` 
SET GLOBAL max_allowed_packet=size;
```

## Creating rows based on the search result

To save the result of a query to a table, we can use the command:

``` 
INSERT INTO table_name(column_list)
SELECT
   select_list
FROM
   another_table
WHERE
   condition;
```

#### Example:

``` 
INSERT INTO examples.students(name, surname, email)
SELECT 
   first_name, 
   last_name, 
   email 
FROM sakila.customer 
LIMIT 5
```
