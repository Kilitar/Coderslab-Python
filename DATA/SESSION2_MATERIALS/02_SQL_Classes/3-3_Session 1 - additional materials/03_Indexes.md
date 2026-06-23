# Indexes

Type: Article

## What is an index?

Indexes are special search tables that speed up searching in a table against one of its columns.

We should use them when many `WHERE` clauses depend on this column.

Too many indexes can slow down the performance of the database - that's why you need to be careful about them and add them after a thorough analysis of the database.

The effect of indexes is most evident in the speed of query execution if the index is added to a column with a numeric type.

## B-Tree (Balanced Tree)

![b-tree](/presentations/DTL/en/4.9/W/M_03_S_03/c614a99c-65ee-477e-8c70-b90d8e79db20/student_content/3ceb3558-b9fb-4146-aa12-7c7864094984/./images/B-tree.png)

A good analogy of indexes from real life is the way the phone book is organized.

Indexes can be applied to individual columns or groups of columns.

`PRIMARY KEY` and `UNIQUE KEY` cause automatic assignment of indexes.

## What are indexes for?

From a data analyst's point of view, an index has one most important task - to speed up the performance of a query, and this is what they are mainly used for. As mentioned earlier, we need to be aware that too many of them can work the opposite of the intended purpose, i.e. queries will execute more slowly.

Most often, indexes are created by a team of database administrators or architects, but an analyst can also create an index if necessary. Indexes can be set up not only in physical tables, but also in temporary tables, but keep in mind that setting up an index also takes time (sometimes it is not a fast operation at all).

Other side effects of indexes are:

- use of additional disk space of the database,
- indexes should be refreshed from time to time, otherwise they will slow down,
- any modification of the database can be more time-consuming, because it will require refreshing the index.

## Creating an index

As mentioned earlier, using the `PRIMARY KEY` keyword, causes automatic creation of index. Because index is most effective with numbers, the `id` column is most often just the row number.

Nevertheless, the index itself can be added when creating a table:

``` 
CREATE TABLE index_example(
   c1 INT PRIMARY KEY,
   c2 INT NOT NULL,
   c3 INT NOT NULL,
   c4 VARCHAR(10),
   INDEX (c1)
);
```

or when you want to modify an existing one, just write:

``` 
CREATE INDEX index_name ON table_name (column_list)
```

It is worth to note: more than one index can be created on a single table.

## Using index

The DB engine will use the index itself when it determines that it can.
For example, using the `index_example` table, the query:

``` 
SELECT * FROM index_example WHERE c1 = 1
```

Is going to use the index, but

``` 
SELECT * FROM index_example WHERE c2 = 1
```

isn't going to use it.

In other words, in order to consciously use an index, you need to know its structure (columns).

## Removing an index

When we find that the index is not needed, it can be removed with:

``` 
DROP INDEX index_name ON table_name
```

We can display the list of indexes with the command:

``` 
SHOW INDEXES FROM table_name;
```
