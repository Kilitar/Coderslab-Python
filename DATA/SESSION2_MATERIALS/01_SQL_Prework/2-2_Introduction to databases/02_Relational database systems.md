# Relational database systems

Type: Article

## What is RDBMS? (Relational database management system)

RDBMS: Relational database management system It is simply a program/engine that manages a database based on a relational model. Importantly, most RDBMS engines are based on the `SQL` standard, so most commands written for one database will work correctly with another (although there may be subtle syntactic differences).

To learn `SQL` in the course we will be using `MySQL`; but as we have indicated, this is not the only implementation available, and depending on their needs, each company (or even a team or project) can use the one that suits them best at the time.

## Database popularity ranking

The chart below illustrates database popularity ranking in 2023-06.

![popularity chart](/presentations/DTL/en/4.9/W/M_02_S_02/0b2aba6b-486d-43bb-a0b9-bcc5d2658671/student_content/1beea46e-341c-46c7-b195-46c926ee4ec1/./images/db_engines.png)

Source: [click](https://db-engines.com/en/ranking_trend)

### Oracle database

![oracle](/presentations/DTL/en/4.9/W/M_02_S_02/0b2aba6b-486d-43bb-a0b9-bcc5d2658671/student_content/1beea46e-341c-46c7-b195-46c926ee4ec1/./images/oracle.png)

Relational database based on SQL language (extended a little). It is used by large companies; only paid versions exist.

Although Oracle is not a cheap solution, by far the more important factors in choosing a system are: performance, scalability and security — and in these areas Oracle dominates.

### MySQL

![oracle](/presentations/DTL/en/4.9/W/M_02_S_02/0b2aba6b-486d-43bb-a0b9-bcc5d2658671/student_content/1beea46e-341c-46c7-b195-46c926ee4ec1/./images/mysql.png)

Currently, the most popular and widely used database management system.

`MySQL` began as a niche system for developers, but has grown into a major player in the enterprise database market. Sold to Sun Microsystems in 2008, `MySQL` eventually became part of Oracle's powerhouse following the Sun Microsystems acquisition in 2009. Now being much more than a niche database, `MySQL` powers commercial websites and countless internal applications used in large enterprises.

### Microsoft SQL Server

![MS Server](/presentations/DTL/en/4.9/W/M_02_S_02/0b2aba6b-486d-43bb-a0b9-bcc5d2658671/student_content/1beea46e-341c-46c7-b195-46c926ee4ec1/./images/sql_server.jpg)

However, if you're using Microsoft Server, you're probably running SQL Server on top of it as well.

Its ease of use, accessibility and tight integration with the Windows operating system make SQL Server the obvious choice for those who use Microsoft-branded products in their businesses. Microsoft is now promoting SQL Server as the platform to use for both on-premise and cloud-based databases and business intelligence solutions.

### PostgreSQL

![Postgres](/presentations/DTL/en/4.9/W/M_02_S_02/0b2aba6b-486d-43bb-a0b9-bcc5d2658671/student_content/1beea46e-341c-46c7-b195-46c926ee4ec1/./images/postgresql.png)

PostgreSQL, or simply Postgres, is an open-source object-relational database management system (ORDBMS).

Its uses include online gaming applications, data center automation options and domain registration.

### SQLite

![SQLite](/presentations/DTL/en/4.9/W/M_02_S_02/0b2aba6b-486d-43bb-a0b9-bcc5d2658671/student_content/1beea46e-341c-46c7-b195-46c926ee4ec1/./images/sqlite.png)

SQLite is a library that implements an independent, serverless and configuration-free database engine.

SQLite is also an embedded database engine. Unlike most SQL databases, SQLite does not use a separate server process running in the background. What sets it apart is its simplicity.

### MariaDB

![MariaDB](/presentations/DTL/en/4.9/W/M_02_S_02/0b2aba6b-486d-43bb-a0b9-bcc5d2658671/student_content/1beea46e-341c-46c7-b195-46c926ee4ec1/./images/maria_db.png)

This database was created by a group of former MySQL AB employees.

The main goal of the project is to cooperate with the free software community and make it available under the GPL license, in contrast to the uncertain status of the MySQL license, which now depends on Oracle.

## Other types of databases

In addition to relational databases, there are other, so-called `NoSQL` databases. These include:

- **graph databases** - Linked data is represented using a graph built from nodes (records) and edges, which define the relationships between data. Importantly, unlike in a relational database, in a graph database the relationship is defined at the node level, not the table level. Sample graph databases - [Neo4J](https://neo4j.com/), [Apache TinkerPop](https://tinkerpop.apache.org/),
- **document database** - e.g. [MongoDB](https://www.mongodb.com/), where data is stored as documents - in this case as `JSON` files; another example of a document database is [CouchDB](https://couchdb.apache.org/),
- **time series database** - databases optimized for working with time series or data with unique timestamp. The most popular database of this type is [InfluxData](https://www.influxdata.com/).

You can find more information about types of databases and their evolution at this [link](https://www.prisma.io/dataguide/intro/comparing-database-types#other-database-types).

## Summary

In this article we have looked at the most popular varieties of relational databases, such as `MySQL` and `Postgres`. Keep in mind that these systems are largely similar, but there are some differences between them.

Also, now we know that relational databases are not the only way to store data; it can also be done in the so-called `NoSQL` databases.
