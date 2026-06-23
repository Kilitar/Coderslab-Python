# NULL

Type: Article

> Remember to edit the queries according to your database user. For an explanation, see **Course preparation > Connecting to the CodersLab database > Executing SQL queries on the server**

`NULL` is an empty value.

At first glance, `NULL` is inconspicuous, but in practice it causes a great many problems, especially when in a table `NULL` goes unnoticed.

![joke](/presentations/DTL/en/4.9/W/M_02_S_03/dc58a073-2282-4a01-ae8d-bdcc9f890d64/student_content/e7dfd1dd-c2d2-4f68-805c-0c26a8b8c060/./images/joke.jpg)

Why?

To understand this, let's go back to the operators `AND` and `OR` - we initially mentioned that they can return two values - 0/1, but at this point we need to add `NULL` to it.

## `NULL` in `DataGrip`

`NULL` in `DataGrip` is displayed by default as shown below:

![null](/presentations/DTL/en/4.9/W/M_02_S_03/dc58a073-2282-4a01-ae8d-bdcc9f890d64/student_content/e7dfd1dd-c2d2-4f68-805c-0c26a8b8c060/./images/null.png)

##### (fragment of the `original_language_id` column from `sakila.film` table)

This means only that the value has not been filled (does not have any data).

## `AND`

Below is the `AND` logical table extended with `NULL`:

| condition A | condition B | AND |
| --- | --- | --- |
| 1 | 1 | 1 |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 0 | 0 | 0 |
| 1 | NULL | NULL |
| 0 | NULL | 0 |
| NULL | 1 | NULL |
| NULL | 0 | 0 |
| NULL | NULL | NULL |

## `OR`

Below is the `OR` logical table extended with `NULL`:

| condition A | condition B | OR |
| --- | --- | --- |
| 1 | 1 | 1 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 0 | 0 | 0 |
| 1 | NULL | 1 |
| 0 | NULL | NULL |
| NULL | 1 | 1 |
| NULL | 0 | NULL |
| NULL | NULL | NULL |

## `NOT`

Below is the `NOT` logical table extended with `NULL`:

| condition A | NOT |
| --- | --- |
| 1 | 0 |
| 0 | 1 |
| NULL | NULL |

> **Note:**
> We can say that if the logical connective returns `NULL` when filtering rows, it is treated as 0 (`False`). Consequently, it will not be returned.

## Special functions

Because `NULL` is a very important part of `SQL`, in order to effectively filter data including `NULL`, two operators were implemented:

- `IS NULL` - returns 1 (`True`), when the value is `NULL`; otherwise: 0 (`False`),
- `IS NOT NULL` - returns 1 (`True`), when the value is **not** `NULL`; otherwise: 0 (`False`) .

For example, finding empty optional addresses in the `sakila.address` table:

``` 
SELECT *
FROM sakila.address
WHERE address2 IS NULL
```

Query result;
![null query](/presentations/DTL/en/4.9/W/M_02_S_03/dc58a073-2282-4a01-ae8d-bdcc9f890d64/student_content/e7dfd1dd-c2d2-4f68-805c-0c26a8b8c060/./images/null_query.png)

> **Note:**
> 
> if we wrote a query: `SELECT * FROM sakila.address WHERE address2 = NULL`, the set of results would be empty.

Analogously, finding non-empty optional addresses in the `sakila.address` table:

``` 
SELECT *
FROM sakila.address
WHERE address2 IS NOT NULL
```

Query result;

![not null query](/presentations/DTL/en/4.9/W/M_02_S_03/dc58a073-2282-4a01-ae8d-bdcc9f890d64/student_content/e7dfd1dd-c2d2-4f68-805c-0c26a8b8c060/./images/not_null_query.png)

> Note that in the example we don't have `NULL`, but (empty string) as values of the column `address2`.
