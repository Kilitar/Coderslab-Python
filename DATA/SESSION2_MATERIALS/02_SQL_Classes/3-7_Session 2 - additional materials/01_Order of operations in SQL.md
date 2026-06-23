# Order of operations in SQL

Type: Article

We have learned all the components of the query. To sum up, we can write the general syntax as follows:

``` 
SELECT [DISTINCT]
    column_names,
    AGG_FUNC(column or expression),
FROM
        tab1 as t1
    [LEFT|RIGHT|INNER] JOIN
        tab2 as t2 ON condition
WHERE row_filter_expression
GROUP BY column_names
HAVING group_filter_expression
ORDER BY column [ASC|DESC]
```

However, the order of operations is not the same as the one of reading the query (from top to bottom). It looks like this:

1. `FROM` and `JOIN` - it is from them that the entire execution of the query begins in order to determine the set that will be passed on.
2. `WHERE` - after the working set is built on the basis of `1.`, the conditions from the `WHERE` clause are checked.
3. `GROUP BY` - after filtering out individual rows, the data is further grouped.
4. `HAVING` - if defined, after the aggregation of the data another filtering occurs, this time already at the level of aggregated data.
5. `WINDOW_FUNCTIONS` - if defined, after aggregation of data, values for window functions are determined.
6. `SELECT` - columns from `SELECT` are determined, and new names are given to the columns.
7. `ORDER BY` - only at the very end the data is sorted according to the given pattern.
