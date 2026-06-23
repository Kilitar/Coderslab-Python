# DELETE CASCADE

Type: Exercise

## DELETE CASCADE

In the `sakila` database delete cascade was not set. For this exercise, get familar with the model of the `tasks` database presented on the schema:

![schema](/presentations/DTL/en/4.9/W/M_03_S_02/e13ef7e2-fdf7-430c-9147-eaa0bc36a70c/exercises/e7f3ab8b-4b3e-4e01-a97c-517bc3f8ef46/./images/tasks-diagram.png)

Based on your analysis of the table, answer the following questions:

- What is the type of relationship between each pair of tables?
- What happens if you delete a record from the `child` table; does this operation affect other tables? Which ones?
- What happens if you delete a record from the `class` table; does this operation affect other tables? Which ones?
- What happens if you delete a record from the `school` table; does this operation affect other tables? Which ones?
- Write a query to delete one of the schools. What happened in other tables?
- Using the query from the class, determine cascading relationships between the tables.

### Code from class:

``` 
USE information_schema; 
 
SELECT
    UNIQUE_CONSTRAINT_SCHEMA,
    TABLE_NAME, 
    REFERENCED_TABLE_NAME 
FROM
    referential_constraints 
WHERE delete_rule = 'CASCADE'
```
