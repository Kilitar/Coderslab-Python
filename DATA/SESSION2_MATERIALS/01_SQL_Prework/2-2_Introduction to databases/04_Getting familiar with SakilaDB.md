# Getting familiar with SakilaDB

Type: Article

## Short history of `Sakila DB`

`Sakila DB` is a successor of *world sample DB*, that was shared by Oracle. Work on it began in 2005, and the first official version was released in March 2006.

## Description

`Sakila DB` is a sample database model for an online DVD rental store.

The database includes information on: movies, actors, payments and customers, and more. The business model is now outdated, but the base and its structure is very good to start learning `SQL`.

## Contents of `Sakila DB`

Below is the UML schema of the `Sakila` database. In order to increase the clarity of the diagram, column information has been removed, and only the connections between tables have been retained.

In the diagram, `views` have been marked in yellow. At this point, we just need to identify them with tables.
![sakila](/presentations/DTL/en/4.9/W/M_02_S_02/0b2aba6b-486d-43bb-a0b9-bcc5d2658671/student_content/d861ca97-9628-472d-a472-8a8adf7b1ddc/./images/sakila-diagram-clean-coders-lab.png)

Diagram source: [link](https://database.guide/what-is-a-database-schema/).

Names of columns and tables are really descriptive but additional information on particular tables are available in the [documentation](https://dev.mysql.com/doc/sakila/en/sakila-structure-tables.html), where the contents of database elements were described in detail.

## Other bases (schemas)

As mentioned earlier, we will mainly use the `Sakila` schema in the course, but on the server there also are:

- `examples` - this is where sample tables are,
- `financial` - this is where the tables created for the workshop are,
- `tasks` - here are the tables we are going to use when doing the exercises (if the tables from `Sakila` do not meet some requirements),
- `employees` - here are the tables that we will use to implement the course summary in the form of a workshop,
- there are also other technical materials available, but we will only use them in exceptional cases and discuss them as needed.

## Summary

This article presented the logical structure of the server along with the available databases, in particular `Sakila`. The architecture of this database will come in handy during classes and exercises; we will refer to it very often, especially since we will learn about relationships and how to connect tables.
