# Introduction to databases

Type: Article

## What are databases?

Databases are organized collections of information whose purpose is
storing, processing and returning data.

A database should allow:

- data definition,
- adding, deleting and modifying data,
- managing data access.

## Why do we use databases?

We use databases when we have a large number of related data in our project.

Storing data in a dedicated database, allows us  to quickly manage such a collection and easily share it with other programs.

Databases are also helpful in the following:

- collecting and storing huge datasets,
- quick searching and sorting of datasets,
- creating relationships between data.

## Types of databases

- **Hierarchical** - are obsolete. Hierarchical databases are said to be hierarchical if there is a parent-child relationship between the data stored in such a system.
  
  
  
  
  Hierarchical type of databases was created by IBM in 1968 and is no longer used.
- **Relational** - databases that focus on the relationships between data. Data in such databases are represented as two-dimensional tables, where each column is an attribute and a row is data.
- **Object-oriented** - databases created based on the idea of object-oriented programming. Objects corresponding to particular classes are held in memory.
  
  
  
  
  They are used when the processed and stored data are hierarchically complex structures and have numerous and intensive relationships (e.g. images, animations, multidimensional data).

They are not very popular due to the high cost of maintenance.

- **Non-relational** - the latest approach to databases. We store data as key-value pairs, where values have no unified structure.
  Easily scalable and fast with large data sets.

## Most popular databases

- **PostgreSQL** - relational database using SQL. Released under an **open source** license.
- **Oracle** - relational database slightly extending SQL. Tends to be used by large companies.
- **MySQL** - a relational database based on SQL language. Popular with small and medium-sized companies.
- **MongoDB** - non-relational database based on holding entire documents, placed in so-called collections.

## How do we communicate with a database?

We already know what a database is and how data is kept in it.
We are left with one more important question: 

**How do we communicate with it?

There are languages specially created for the purpose of "talking" to a database. We are going to learn the most popular one: **SQL** (Structured Query Language).

This language is based on queries. We will send instructions (in the form of queries) saying what we want to achieve, and the database will respond accordingly.

Each of our queries will cause one (though sometimes very complex) reaction in the database.

These reactions can be different: it can be the return of some set of data, modification of existing data, or the creation of a completely new piece of information in the database.

## Relational databases

Behind the relational model is the idea of linking data by means of interrelationships between them.
But let's start by explaining how information is stored in a database.

We will be working on a database (very simplified) that holds information for a virtual student record at school.

In our theoretical database, which we will rely on in this article, we hold the following information:

- **each student's data**, e.g, name, surname and email of a parent,
- **each teacher's data**, e.g, name, surname and salary,
- **each class data**, e.g, name, form teacher, list of students,
- **each mark data**: mark with information which teacher gave it and to which student.

## Database tables

A relational database has tables in its structure.

A table in a database is a subset that stores data related to each other. If our database represents a store, for example, it may have the following tables:

- table with shop employees' data,
- table with shop orders,
- table with shop products,
- table with current promotions.

Each table consists of columns and rows. A column stores the data associated with a record, this data is of the appropriate
type, such as:

- for a user: 
  
  first name, last name, email, IP address, login, password;
- for an order: 
  
  number, amount, date placed, date paid, date shipped.

A row is a single record stored in a table.

## What data is stored in a database?

In a relational database, each of the data types (sometimes also known as entity) is kept in a separate table.
Database tables are similar to Excel tables, where we have all the fields that can be stored in columns.

Some of these columns will be required - without them the database will not accept the new information.

In each row one entry is kept, each representing a one-item set of information (e.g. data of one student).

Below is an example of a database table storing information about students:

| student_id | name | surname | email |
| --- | --- | --- | --- |
| 1 | Vlad | Steppen | vlad.steppen@yahoo.com |
| 2 | Angela | Yallow | a.yallow@gmail.com |
| 3 | Simon | Neckenzie | simon.neckenzie@hotmail.com |
| 4 | Olga | Sokolov | sokolov.olga@gmail.com |

## Data uniqueness – primary key

We mentioned earlier that each entry in our database must be unique.
This is achieved through the use of a **primary key**.
This is one of the columns in our table (customarily, it is the first column) that holds an automatically generated number unique to this table.

This number becomes the identifying number (**id**) for the row.
The value of the primary key in the vast majority of cases is automatically assigned by the database and we should not interfere with it.

Let's take another look at our table with students - the primary key is the column named student_id.

| student_id | name | surname | email |
| --- | --- | --- | --- |
| 1 | Vlad | Steppen | vlad.steppen@yahoo.com |
| 2 | Angela | Yallow | a.yallow@gmail.com |
| 3 | Simon | Neckenzie | simon.neckenzie@hotmail.com |
| 4 | Olga | Sokolov | sokolov.olga@gmail.com |

## Database schema

Below you can see a simplified schema of the tables in the database on which we will work.
This schema is not complete - it lacks relationships between tables and their associated columns and additional tables (so-called junction tables).

![](/presentations/DTL/en/4.9/W/M_04_S_03/eb66c298-e4ee-445b-91be-f3445cec6ba5/student_content/3979f008-0409-47c1-8b3c-153f15d88e24/images/ex_database.png)

Relationships are links between individual database tables. Let's take a look at them.

## Types of relationships

In relational databases there are three relationships between tables:

- one-to-one,
- one-to-many,
- many-to-many.

### One-to-one relationship

A relationship in which one element from a table can be connected to only one element from another table.

**Example:**

- A teacher can be the educator of only one class.
- A class can have only one educator.

### One-to-many relationship

A relationship in which one element from a table can be connected to multiple elements from another table.

**Example:**

- A student can belong to only one class, and multiple students can be assigned to one class.

### Many-to-many relationship

A relationship in which many elements from a given table can be combined with multiple elements from another table.

**Example:**

- A class can be taught by multiple teachers.
- One teacher can teach multiple classes.

In our sample database, we will also use relationships.
Let's list below what kind of relationships are present in it:

- **student belongs to one class** - there are many students in one class,
- **a supervising teacher can be responsible for one class** - there is one supervising teacher in one class,
- **a student can have multiple marks** - a mark is given to one student,
- **a teacher can give multiple marks** - a mark is given by one teacher,

You will learn about how relationships are created during classes.

### Database schema with relationships

Below you can see a simplified schema of the tables in the database on which we will work.
The relationships and necessary columns are already added.

![](/presentations/DTL/en/4.9/W/M_04_S_03/eb66c298-e4ee-445b-91be-f3445cec6ba5/student_content/3979f008-0409-47c1-8b3c-153f15d88e24/images/ex_rel_database.png)
