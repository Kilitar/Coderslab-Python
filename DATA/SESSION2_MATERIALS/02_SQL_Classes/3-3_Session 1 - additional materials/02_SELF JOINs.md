# SELF JOINs

Type: Article

## Other types of `JOIN`

## `CROSS JOIN`

One may wonder what would happen if we didn't write on which columns we perform joins. This case has a special place in set theory, but in practice it is avoided.

Mathematics calls such joins the **Cartesian product**.

### Example

``` 
SELECT
    actor_id,
    film_id
FROM
        sakila.actor
    CROSS JOIN
        sakila.film
```

(result fragment)

| actor_id | film_id |
| --- | --- |
| 186 | 1 |
| 111 | 1 |
| 85 | 1 |
| 63 | 1 |
| 156 | 1 |

Both notation and theory are very simple here. It can be compared to the situation where the rows of table A are arranged in a line, and the rows of table B in a perpendicular line. The result contains all possible pairs, just like coordinate pairs on the Cartesian plane.

Unfortunately, the order of magnitude of the result is the sum of the orders of magnitude of the input tables, making it easy to fall outside the range of available operating memory resources when working with even a small amount of data if this combination is used carelessly.

With two tables A and B with the number of rows (respectively) 1,000 and 2,000, the result of `CROSS JOIN` will be a table with `2,000,000` (two million!) rows.

**It is not recommended to use `CROSS JOIN` if we are not sure that they are the only way to get the desired result.**

## `SELF JOIN`

We speak of `SELF JOIN` when the same table appears on the left and on the right side of the join.

In this type of join, it is necessary to use aliases. The general syntax is as follows:

``` 
SELECT c1, c2, c3, ...    -- columns we want to show
FROM t AS t1 JOIN t AS t2 -- the same table (here "t") named in one case (t1) and (t2) in the other
USING (c)                 -- we specify the columns to join
WHERE condition           -- general condition based on standard aliases
```

For example, a condition could be:

``` 
t1.c1 != t2.c1;           -- filtering repeating values
```

### Joining can be performed on a single table.

These types of joins allow us to have an elaborate insight into the relationships between the elements of one table. For example:

- co-occurrence of given values in rows,
- comparing rows with each other,
- preparing a table for complex grouping.

### Example

We most often use `SELF JOIN` when we are dealing with a hierarchy of elements. These can be categories in a store (then we have a case where categories are nested). We can also show this with the example of a company where there is a supervisor-subordinate relationship.

In our database, we will have the following assumptions:

- Each employee has only one direct supervisor.
- All employees are stored in the same table.

The structure of the table could look like this:

| id | name | report_to |
| --- | --- | --- |
| 1 | Liz | NULL |
| 2 | Bart | 1 |
| 3 | Monica | 1 |
| 4 | Tom | 3 |

Based on this, we can understand, that:

- Liz has no supervisor (she is the boss). Bart and Monica are her direct subordinates
- Additionally, Monica is Tom's superior.
- Neither Tom nor Bart have any subordinates.

We can create the previously presented table using the following query:

``` 
CREATE TABLE employees (
    id INT auto_increment primary key,
    name VARCHAR(255),
    report_to INT, -- by default nullable (can be NULL)
    FOREIGN KEY (report_to) REFERENCES employees (id)
);
```

Then let's fill the table with data:

``` 
INSERT INTO employees (id, name, report_to) VALUES
    (1, 'Liz', NULL), (2, 'Bart', 1), (3, 'Monica', 1), (4, 'Tom', 3);
```

Now, we can easily find out who is whose supervisor:

``` 
SELECT 
    e1.name AS superior, 
    e2.name AS subordinate -- list of all relations
FROM 
        employees AS e1 -- table employees on the left
    JOIN 
        employees AS e2 -- and right side of JOIN means SELF JOIN
            ON e2.report_to = e1.id;
```

Querying a list of dependencies between employees requires specifying the same table twice on both sides of the JOIN. To make this possible we use `AS` aliasing.

| superior | subordinate |
| --- | --- |
| Liz | Bart |
| Liz | Monica |
| Monica | Tom |
