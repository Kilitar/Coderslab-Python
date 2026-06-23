# Views

Type: Article

## What is the view for?

Before we explain what view is, let's analyze an example. Suppose we want to create the following query:

``` 
SELECT 
    a.first_name as actor_name,
    a.last_name as actor_last_name,
    f.title as film_title,
    f.description as film_description
FROM
        actor as a
    INNER JOIN
        film_actor fa on a.actor_id = fa.actor_id
    INNER JOIN
        film f on fa.film_id = f.film_id
```

which returns information about the actor and the movies they played in.
If we wanted to use this query, it would often have to be saved somewhere and each time copied, pasted, saved....

In other words, such a process is very inefficient, because every time someone asks us to refresh such a listing, we have about 5-10 minutes of additional work.

This is exactly the reason why `views` are useful.

## What is a view?

You can say that a view is a query stored directly on the database server - just like that. It is used in the same way as tables (we have already used views in the course).

The syntax for creating a view is as follows:

``` 
CREATE VIEW actor_film AS
SELECT 
    a.first_name as actor_name,
    a.last_name as actor_last_name,
    f.title as film_title,
    f.description as film_description
FROM
       actor as a
    INNER JOIN
        film_actor fa on a.actor_id = fa.actor_id
    INNER JOIN
        film f on fa.film_id = f.film_id
```

Note that the syntax is close to the one we used when creating a table based on a query. What is the difference between a view and a table?

> The view recalculates the query each time and returns the form of a table; the table, on the other hand, has the data stored on disk, and as long as we don't change it ourselves, the data stays as it was originally stored.

In the example given at the beginning, you could, e.g., make the view available to someone from the outside. Then, when they need it, they retrieve the data for themselves, and we don't have to worry about it, we just need to pass the following syntax to such a person:

``` 
SELECT * FROM actor_film;
```

## Materialized views – PostgreSQL and Oracle

We already know the concept of a view. But what if the data (mostly) refreshes in our database once a day, and the view is used by 20 people? In such a situation, the view will **recalculate the same data 20 times**.  In `PostgreSQL` and `Oracle` **materialized views** come to the rescue - this is the concept of views that are created based on queries just like regular views, but remember the result of their last execution.

Thanks to this, their repeated use does not cause processor load by executing the queries that build the view. On the other hand views of this type are stored in memory or dumped to the disk. So they increase the use of other resources.

> **Note:**
> **Materialized views do not exist in MySQL!**

`MySQL` does not support materialized views. We mention them because in `PostgreSQL` or `Oracle` databases they are important topics. In `MySQL` if we want to have an analogous functionality, we create temporary tables using syntax like:

``` 
CREATE TABLE XYZ AS SELECT …
```

Later we have to remember about updating the data in this table ourselves. To do it we can use, for example, procedures or job_scheduler... more on that later.

## A view does not have to refer to other tables...

``` 
CREATE VIEW daysofweek (day) AS
    SELECT 'Mon'
    UNION
    SELECT 'Tue'
    UNION
    SELECT 'Web'
    UNION
    SELECT 'Thu'
    UNION
    SELECT 'Fri'
    UNION
    SELECT 'Sat'
    UNION
    SELECT 'Sun';
```

In general, a view can become any query where we earlier add a clause:

``` 
CREATE VIEW view_name AS ...
```

## Advantages of using views

- Simplifying complex queries - the business recipient gets only what they need, and does not worry about how it was created.
- Hiding complex relationships between tables - the recipient does not have to remember how to connect one table to another as long as it has already been done and checked once.
- Adding an extra layer of security - the user gets access only to selected data, not to the whole database.
- Making it easier to maintain backward compatibility.

![view-concept](/presentations/DTL/en/4.9/W/M_03_S_04/c7fde7ac-87f0-43c5-bebe-c446b356926d/student_content/8496ca99-5b56-4dc3-a0f2-86e7d412a735/./images/view-concept.jpg)

## Dropping a view

If you want to remove a view, just use the following syntax:

``` 
DROP VIEW view_name
```

## Modifying a view

If we want to modify a view, we have two options:

- either first use `DROP VIEW` and then again `CREATE VIEW`,
- or use the query dedicated for this: `CREATE OR REPLACE VIEW view_name AS ...`.
