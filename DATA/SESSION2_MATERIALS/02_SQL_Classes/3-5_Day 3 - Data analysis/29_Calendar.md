# Calendar

Type: Exercise

# Calendar

Using `ROW_NUMBER` and appropriate date values create a `calendar` table in the database, that:

- will start from '2000-01-01',
- will end on '2030-12-31'.

The calendar table should have the following columns:

- date (`date`),
- year (`date_year`),
- month (`date_month`),
- day (`date_day`),
- number of day of week (`day_of_week`),
- number of week in the year (`week_of_year`),
- date of generating the calendar (`last_update`).

Preview of the table result:

``` 
+----------+---------+----------+--------+-----------+------------+-------------------+
|date      |date_year|date_month|date_day|day_of_week|week_of_year|last_update        |
+----------+---------+----------+--------+-----------+------------+-------------------+
|2000-01-01|2000     |1         |2       |1          |52          |2021-05-11 20:40:12|
|2000-01-02|2000     |1         |3       |2          |1           |2021-05-11 20:40:12|
|2000-01-03|2000     |1         |4       |3          |1           |2021-05-11 20:40:12|
|2000-01-04|2000     |1         |5       |4          |1           |2021-05-11 20:40:12|
|2000-01-05|2000     |1         |6       |5          |1           |2021-05-11 20:40:12|
+----------+---------+----------+--------+-----------+------------+-------------------+
```

> Hint - start by modifying the following code:

``` 
SELECT
    ROW_NUMBER() over () AS rn 
FROM payment
LIMIT 100
```

## Solution schema

1. Check the number of days between '2000-01-01' and '2030-12-31'.
2. In place of the `LIMIT` from the query above, write the value from the previous point.
3. Using the appropriate date functions, write a query that returns a calendar view.
