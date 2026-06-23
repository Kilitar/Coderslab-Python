# Relational database

Type: Article

In this article you will find out what exactly relationships are and how to join together the data from multiple tables to extract more interconnected information.

## Relationships

Relationships is another name for tables. Every relationship (table) consists of a header that contains the information on which attributes (columns) are included in it and the contents – collection of tuples (rows).

**Relationships**, **attributes** and **tuples** are very formal names. In practice, it is more common to use the names: **table**, **column** and **row**; we'll use these names from now until the end of the course.

## Primary key

It is a column that unambiguously identifies the row within the table. Referring to a value from this column guarantees us that at most one row will be matched - it follows that the values in a column labeled as a primary key are always unique.

The primary key is not a mandatory part of the table, but it is, in practice, essential to work with tables conveniently, precisely because it guarantees pointing to exactly one row.

By convention the primary key is the column called `id`, and its values are numbers: `1`, `2`, `3`, etc. You can deviate from this rule if the table contains a column that meets the assumptions of the primary key. It can be the `PESEL` column in the table of the citizen of Poland – by definition, each citizen has their own unique PESEL number, that identifies them. But it cannot be the `PESEL` column in the table of clients of a private company – foreigners don't have the number; a common practice is to enter the first six digits of the birth date, followed with five zeros, and this can result in duplicates.

## Foreign key

A foreign key is a column whose contents are the primary keys of other tables. In this way, a row in a table can indicate the rows associated with it. Example:

**customer** table:

| id | name | surname | pesel |
| --- | --- | --- | --- |
| 1 | Marian | Kowalski | 90123112345 |
| 2 | Anna | Nowak | 89112223456 |
| 3 | Kamil | Ślimak | 67020355441 |
| 4 | Rafał | Koń | 79050800123 |

**credit_card** table:

| id | client_id | credit_card_number | expires |
| --- | --- | --- | --- |
| 1 | 4 | 4778 7983 8407 4994 | 7/2023 |
| 2 | 4 | 4989 3409 7677 3421 | 3/2022 |
| 3 | 4 | 4821 3128 6582 3791 | 1/2022 |
| 4 | 2 | 4759 4724 9044 0456 | 4/2021 |

In the example above, both tables have their own keys as the `id` column. The values in the two `id` columns do not depend on each other in any way.

But there is a relationship between the `customer.id` and `credit_card.client_id`. The value from the `client_id` column points to the rows with remaining data about the owner of the credit card data. In this example, we can see that Rafał Koń has 3 credit cards, Anna Nowak has one, and the other customers have not yet provided their card data.

## Combining tables in practice

When we join the results from two tables we will talk about **left** and **right** – the labels will mean which of the tables was referenced before, and which one after the word `JOIN` in the `SELECT` query.

Sample query that returns data about customers who have provided their card data:

``` sql
SELECT name, surname, credit_card_number FROM customer JOIN credit_card ON customer.id = credit_card.client_id;
```

``` 
|        name           |       surname         |   credit_card_number     |
| from "customer" table | from "customer" table | from "credit_card" table |
|----------------------:|----------------------:|-------------------------:|
|                  Anna |                 Nowak |   4989 3409 7677 3421    |
|                 Rafał |                   Koń |   4759 4724 9044 0456    |
|                 Rafał |                   Koń |   4759 4724 9044 0456    |
|                 Rafał |                   Koń |   4759 4724 9044 0456    |
```

The `JOIN` keyword makes it possible to point to the next table we want to take data from.

There are 4 possible ways to join tables:

- `LEFT JOIN` - returns all rows from the **left** table, and adds data from the **right** one – wherever data is missing, the `NULL` value will be used,
- `RIGHT JOIN` - works similarly to `LEFT JOIN`, but returns all rows from the **right** table, adding data from the **left** one,
- `INNER JOIN` or just `JOIN` – returns only those rows that could be matched in both tables,
- `OUTER JOIN` - returns all rows from both tables, joined wherever possible, filled with `NULL` values where the data was missing in the other table.

### `LEFT JOIN` query example:

Below is an example of a `LEFT JOIN` query. As you can see, it is used practically in the same way as the `JOIN` query from the example above. You will learn the other types, and how to combine more than 2 tables soon, in a class with the lecturer.

``` sql
SELECT name, surname, credit_card_number FROM customer LEFT JOIN credit_card ON customer.id = credit_card.client_id;
```

``` 
|          name         |       surname         |    credit_card_number    |
| from "customer" table | from "customer" table | from "credit_card" table |
|----------------------:|----------------------:|-------------------------:|
|                Marian |              Kowalski |                    NULL  |
|                  Anna |                 Nowak |     4989 3409 7677 3421  |
|                 Kamil |                Ślimak |                    NULL  |
|                 Rafał |                   Koń |     4759 4724 9044 0456  |
|                 Rafał |                   Koń |     4759 4724 9044 0456  |
|                 Rafał |                   Koń |     4759 4724 9044 0456  |
```
