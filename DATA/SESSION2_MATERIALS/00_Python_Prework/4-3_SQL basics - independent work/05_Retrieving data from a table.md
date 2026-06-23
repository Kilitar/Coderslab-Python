# Retrieving data from a table

Type: Article

## Loading table elements

We retrieve data from the table using a SELECT query:

``` 
SELECT col_name_1, col_name_2
FROM table_name;
```

Where in the place of `col_name_*` we enter the names of columns whose data we want
to load and in the place of `table_name` the name of the table we want to load the data from.

**Example:**

``` 
SELECT class_id, name
FROM classes;
```

To select all columns, we can use the * symbol. Note that if
it is not necessary, let's not retrieve all columns from the table.

``` 
SELECT *
FROM table_name;
```

**Example:**

``` 
SELECT *
FROM classes;
```

## WHERE clause

We can narrow down the search results by adding a WHERE clause to our SELECT query:

``` 
SELECT col_name_1, col_name_2
FROM table_name
WHERE col_name_1 = <searching_value>;
```

**Example:**

``` 
SELECT *
FROM students
WHERE name = 'Walter';
```

*Note:* All strings we want SQL to take literally (like the name in the example above) must be surrounded by single apostrophes (`'` character).

## Relational operators

| Operator | Description | Example |
| --- | --- | --- |
| = | Equal | SELECT * FROM students WHERE name = 'Dexter'; |
| <> | Not equal (new versions can also use !=) | SELECT * FROM students WHERE name <> 'Dexter'; |
| > | Greater than | SELECT * FROM teachers WHERE pay > 139; |
| >= | Greater or equal | SELECT * FROM teachers WHERE pay >= 139; |
| < | Less than | SELECT * FROM teachers WHERE pay < 100; |
| <= | Less or equal | SELECT * FROM teachers WHERE pay <= 100; |
| BETWEEN a AND b | In the specified range (including the limit) | SELECT * FROM marks WHERE mark BETWEEN 3 and 5; |
| IS NULL | equal to NULL | SELECT * FROM students WHERE name IS NULL; |
| IN(a, b, c) | Found among the variables given in parentheses | SELECT * FROM students WHERE name IN ('Dexter', 'Stephen'); |
| NOT IN(a, b, c) | Not found among the variables given in parentheses | SELECT * FROM students WHERE name NOT IN ('Dexter', 'Stephen'); |
| OR | Logical operators connecting individual conditions | SELECT * FROM students WHERE name = 'Dexter' OR name = 'Stephen'; |
| AND |  | SELECT * FROM students WHERE name = 'Dexter' AND class_id = 11; |
| LIKE | Searches for the specified pattern (strings only, e.g. name: Dexter) |  |
|  | 'De%' – column value starting from 'De' | SELECT * FROM students WHERE name LIKE 'De%'; |
|  | '%ter' – column value ending with 'ter' | SELECT * FROM students WHERE name LIKE '%ter'; |
|  | '%exte%' – column value includes 'exte' | SELECT * FROM students WHERE name LIKE '%exte%'; |
| NOT | Can precede other operations | SELECT * FROM students WHERE name NOT LIKE 'De%'; |
|  |  | SELECT * FROM marks WHERE mark NOT BETWEEN 3 and 5; |

## AND clause - combining several queries

We can add several conditions in one SQL query. For example, if we want to find all persons in the class with id=3 whose name is Brandon - we can do it using the logical operator AND.

It causes our query to search for such rows in which data satisfies both requirements.

**Example:**

``` 
SELECT * FROM students
WHERE name = 'Brandon' AND class_id = 3;
```

## OR clause - combining several questions.

What about the case where we don't want to combine queries using "and" but with "or"? \

That is, for example, we want to find all the marks in our system that are issued for a student with id=5 **or** for a student with id=6.
We can achieve this using the OR keyword.

**Example:**

``` 
SELECT * FROM marks WHERE
student_id = 5 OR student_id = 6;
```

## ORDER BY clause

We can sort the found results against one column (or more).
The ORDER BY clause is used for this. Sorting is done according to the order of
columns listed in the query.

``` 
SELECT col_name_1, col_name_2
FROM table_name
ORDER BY col_name_1 ASC|DESC,
col_name_2 ASC|DESC;
```

Pick one of the options: ASC – ascending, DESC – descending

**Example:**

``` 
SELECT * FROM marks
ORDER BY mark DESC;
```
