# Relationships

Type: Article

## Relationships in `SQL`

Relationships is another name for tables. Each relationship (table) consists of a header, which contains information about what attributes (columns) are contained in it, and content - a set of tuples (rows).

**Relationships, attributes, and tuples** are very formal terms. In practice, one tends to encounter the terms (respectively) **table, column, and row**.

## Primary key

It is a column that unambiguously identifies the row within the table. Referring to a value from this column guarantees that at most one row will be matched - it follows that **the values in a column labeled as a primary key are always unique**.

The primary key is not a mandatory part of the table, but it is, in practice, essential to work with tables conveniently, precisely because it guarantees pointing to exactly one row.

By convention the primary key is the column called `id`, and its values are consecutive integers (starting from 1). You can deviate from this rule if the table contains a column that meets the assumptions of the primary key. It can be the `PESEL` column in the table of the citizens of Poland – by definition, each citizen has their own unique `PESEL` number that identifies them. But it cannot be the `PESEL` column in the table of clients of a private multinational company because foreigners don't have the number. A common practice is to enter the first six digits of the birth date, followed by five zeros: and this can result in duplicates.

> It is worth noting that in the `MySQL` implementation if a column is a primary key then it cannot contain `NULL`.

## Foreign key

A foreign key is a column whose content is the primary key of another table. In this way, you can link data through the relationships contained in it.

Example based on linking the `film` and `language` tables:

![foreign-key](/presentations/DTL/en/4.9/W/M_02_S_03/9ba63916-a8f9-4753-a578-b5d033546874/student_content/849537c2-03c4-423e-87fd-9d769115e91c/./images/foreign_key.png)

In the `film` table we have the following keys:

- primary - as `film_id`, commonly marked with diagrams with a key,
- foreign - we have two here: for `language_id` column, and `original_language_id`, which refer to the `language_id` column in the `language` table.

In the `language` table we have:

- primary - `language_id` column,

> **Note**
> 
> While the `film` table has a foreign key to the `language` table, it does not mean that the opposite is also true, i.e. that the `language` table has a foreign key to the `film` table. In other words, having a foreign key sets a one-way relationship.

## Composite key

So far we have only talked about simple keys based on a single, chosen column. The key can be based on several columns. For example, if we are talking about a film with the following properties:

- film title,
- production date,
- duration,
- rating,
- director,
- boxoffice

we can readily assume that:

- film title,
- production year,
- and director

uniquely identify the film in question so they are its unique identifier.

> In the practice of an analyst, this type of keys is most often encountered when data is received in csv form, where a preliminary analysis of the data structure should be done and potential keys should be selected.

> A table can contain different types of keys, i.e. it can contain both a composite (also called compound) key, a foreign key and a primary key.

## Why bother with relationships?

### Maintaining data integrity

Defining relationships between tables helps to maintain order in the database. If the table contains a foreign key, then we are sure that there are no values in it that are not present in the reference table. For example, to the `film` table we are not going to add a film with a language e.g. Hindi, unless it is earlier added to the `language` table.

What's more, the database engine not only enforces the correctness of the written data; it also makes sure that deletion or modification does not violate the boundaries (constraints) defined, for example, by keys.

Let's imagine a situation where someone wants to remove a company that has already filed some tax returns from the tax return database. We then have the following options:

- Prevent this operation and inform the database user of the error.
- Delete all the returns together with the company.
- Set the company ID to NULL, if it is possible to give it such property.

The default option is to throw an error.

> As you can guess, checking integrity and relationships is not an easy task for the database engine, which is reflected later in the performance of writing to the database.
