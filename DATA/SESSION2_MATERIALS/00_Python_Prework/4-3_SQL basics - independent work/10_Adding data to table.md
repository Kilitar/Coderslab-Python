# Adding data to table

Type: Article

## Adding elements to a table

We add data to the table using the **INSERT INTO** query:

``` sql
INSERT INTO table_name(col_name_1, col_name_2, col_name_3, ...)
VALUES (value1, value2, value3, ...);
```

Where:

- `table_name` – is how we refer to the table,
- `col_name_1, col_name_2, ...` – are names of columns,
- `value1, value2, ...` – are individual values,

If we do not specify column names after the table name, the data will be written to the next columns of the table (according to its definition):

``` sql
INSERT INTO table_name VALUES (value1, value2, value3, ...);
```

**Example 1:**

``` sql
INSERT INTO students VALUES (10, 'Jack', 'Koval', 'jack@gmail.com', 1);
```

After running this example, the database will return the following information:

``` text
INSERT 0 1
```

It means that one record (1) has been added to the database. 0 is the table object identifier (OID). By default, the OID for the table is not set - that's why the value is 0. During the course, we will not go into into topics related to the operation of data engines, so the topic of OID will not be discussed.

You can find more information in the documentation: [https://www.postgresql.org/docs/8.1/datatype-oid.html](https://www.postgresql.org/docs/8.1/datatype-oid.html)

**Example 2:**

``` sql
INSERT INTO students VALUES ('Walter', 'walter@gmail.com');
```

In this case we will get an error:

``` text
ERROR:  invalid input syntax for integer: 'Walter'
LINE 1: INSERT INTO users VALUES('Walter', 'walter@gmail.com');
```

The error is caused by the fact that the number of columns (5) is not equal to the number of the passed data (2).

**Example 3:**

``` sql
INSERT INTO students(name, surname, email, class_id) VALUES('Walter', 'Adamson', 'walter@gmail.com', 2);
```

We can also specify the columns in which the data will be populated.
In the above example, we bypass the primary key - so the database itself will generate it for us.
