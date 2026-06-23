# UML basics

Type: Article

`UML`: `Unified Modeling Language`, is a method of graphical representation of informatics systems. For our purposes, we will focus only on the elements that are used in the case of databases to represent their contents, namely the individual tables and the relationships between them.

A well-documented database should also include its `UML` diagram, so that the analyst does not have to *guess* the relationships, but has them graphically presented.

> As a rule, data analyst's duties do not include the creation or development of the database model, most often they are simply a database user. Therefore, in this section we will focus only on reading the diagram.

## `UML` components in the context of databases

- **Classes** - or simply **tables**, an example representation:

![table](/presentations/DTL/en/4.9/W/M_02_S_02/0b2aba6b-486d-43bb-a0b9-bcc5d2658671/student_content/15277c60-4dbe-4d01-bf82-42fe60bd7c36/./images/table.png)

The first line contains the name of the table, below it is the information about the names of individual columns and their types (we will discuss types in `SQL` in detail during the second session).

- **Relationships** - define relationships between tables. In `UML`, a relationship is customarily defined simply by arrows connecting two tables.

The example below illustrates the connection (relationship) between the `payment` and `rental` tables: in this case it was defined for the `rental_id` column:

![relation](/presentations/DTL/en/4.9/W/M_02_S_02/0b2aba6b-486d-43bb-a0b9-bcc5d2658671/student_content/15277c60-4dbe-4d01-bf82-42fe60bd7c36/./images/relation.png)

> We skip the types of relationships for the moment, they will be discussed in detail during the first session, on the second day.

- **Key** - in short: a key (identifier) uniquely identifies a row; in other words: within a column that is a key, there **cannot** be the same value twice.

In a `UML` database, a column used as a unique identifier has a key symbol to the left, for example:

![key](/presentations/DTL/en/4.9/W/M_02_S_02/0b2aba6b-486d-43bb-a0b9-bcc5d2658671/student_content/15277c60-4dbe-4d01-bf82-42fe60bd7c36/./images/key.png)

In the `film_text` table, the key (identifier) is the `film_id` column, which was marked with the black rectangle.

# Summary

In this article we have learned about the basic components of `UML`, which can help you present and conveniently read the structure of the database.

Using the knowledge from this article, we will see how the `Sakila` database, used as the basis for developing this course, was built.
