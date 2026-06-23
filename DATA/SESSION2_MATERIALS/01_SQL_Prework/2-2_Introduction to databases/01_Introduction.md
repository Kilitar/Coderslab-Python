# Introduction

Type: Article

## Databases and database systems

According to official definitions:

> **Database** - a collection of data stored according to certain rules.

> **Database Management System** (DBMS) - a software or information system used to manage a database.

The database application is responsible for:

- maintaining relationships between files
- their security under conditions of multi-access and malfunctions
- interpreting queries and generating reports

In practice, the term - database - is often used to refer to a database system.

## Why do we use databases?

We use databases when we have a large number of related data in our project. Storing the data in a dedicated database management system will allow us to quickly manage such a collection and easily share it with other programs.

Databases are also helpful in the following:

- collecting and storing huge datasets,
- quick searching and sorting of datasets,
- creating relationships between data.

## What is a relational database?

The theory of relational databases is very extensive and is definitely beyond the scope of this course, moreover, in practice, it is enough for us to learn the most important concepts of relational database theory needed for our daily work as a data analyst.

Relational database system consists of the following hierarchical elements:

- **tables** - as a structure for storing data,
- **tuples** - in other words, the rows (records) of a given table,
- **keys** - a way to uniquely identify a given row in a table,
- **relationships** - as connections between individual tables (will be discussed in detail later),
- **constraints** - in short — rules controlling the content of a row in the table.

### Tables

In shape and structure they resemble those known from `Excel` - they are built of rows and columns, but they have some important differences:

- in a worksheet column data types can be mixed, in a database the type of data in a column is predetermined (e.g. `float` - 10.00),
- far more data can be loaded into a database table.

### Tuples

As mentioned earlier, tuples are simply rows of a table. Importantly, they all have the same attributes - **columns** and there is no exception to this rule (at most, a field can be empty: represented by `NULL` value).

![table_anatomy](/presentations/DTL/en/4.9/W/M_02_S_02/0b2aba6b-486d-43bb-a0b9-bcc5d2658671/student_content/3214cdb2-8941-4607-b0fc-8f6e578da395/./images/table_anatomy_en.png)

### Keys

The key is defined for a given table. Without going into the theoretical details of a key, we can say that it uniquely designates a row in the table (most often it will simply be a column named `id`).

Interestingly, there are many types of keys with different theoretical properties (e.g. primary key, super key, etc.), but for our applications this is unnecessary.

### Relationships

Practically speaking, relationships answer the question of how table A can be connected to table B. The topic is broad and also important, so we will discuss it together in class.

### Constraints

In practice **constraints** impose certain restrictions on the quality of data in the table. They can relate to one column, for example, a person's height cannot be negative, or several - the price of a product after discount cannot be higher than before it.

## Summary

In this article we learned the basics and the structure of relational databases, along with the purpose of using them. We also know that the central element are the tables where data is stored. Pairs of tables can be connected by relationships.
