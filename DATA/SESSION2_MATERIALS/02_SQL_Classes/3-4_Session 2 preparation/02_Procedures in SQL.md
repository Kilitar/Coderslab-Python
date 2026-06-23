# Procedures in SQL

Type: Article

## Introduction to procedural `SQL`

`PL/SQL` is an extension of `SQL` allowing, among other things, the creation of loops, procedures or functions.

## Variables

Variables are inherent elements of procedures and functions. In `PL/SQL` it is possible to create your own variables and work with them as needed.

Example:

``` 
SET @name = 'XYZ';  -- defining new variable
SET @surname = 'TMMNB';

SELECT @name; -- returning the content of a single variable
SELECT @name, @surname; -- we can also return multiple variables
```

> **Note:**
> There are two equivalent syntaxes for assigning a value to a variable - `=` or `:=`.

We can also use a query to generate the value of a variable:

``` 
SET @count = (SELECT COUNT(*) FROM payment); -- number of rows in the payment table
SELECT @count;
```

## Procedures

A procedure is, in other words, a stored `SQL` code that we can re-use many times.

Example:

``` 
DELIMITER $$
 
CREATE PROCEDURE sp_name()
BEGIN
  -- SQL code
END $$
 
DELIMITER ;
```

Where:

- `sp_name` is the name of the procedure
- `()` - list of arguments (empty in this case).

Because procedures consist of multiple statements, a special designation must be entered for the end of the procedure. It can be a string of any characters; usually: `//` or `$$` (as in the example below), marked with the `DELIMITER` keyword.

## Arguments

We pass the arguments to the procedure in parentheses. In addition to the types of variables, we can also use additional keywords:

- `IN` - input parameter; its changes inside the procedure are ignored outside,
- `OUT` - output parameter; set inside the procedure; its initial value is ignored,
- `INOUT` - is read from outside and its changes are propagated outside.

Example – a procedure that increases a counter by the given value:

``` 
DELIMITER $$
 
CREATE PROCEDURE set_counter(
    INOUT counter INT,  -- the counter variable will be displayed after modification; variable type INT
    IN inc INT -- input parameter
)
BEGIN
    -- SQL code
    SET counter = counter + inc;
END$$
 
DELIMITER ;
```

## Using a procedure

To run an existing procedure we use: `CALL proc_name(params)`.

If we wanted to execute the `set_counter` procedure we created earlier:

``` 
SET @counter = 1;
CALL set_counter(@counter, 1); -- 2, new value of the @counter variable
CALL set_counter(@counter, 1); -- 3, new value of the @counter variable
CALL set_counter(@counter, 5); -- 8, new value of the @counter variable
SELECT @counter; -- 8
```

## Deleting procedures

To delete a procedure it is enough to use the `DROP PROCEDURE` clause, for example:

``` 
DROP PROCEDURE [IF EXISTS] set_counter;
```

## Advantages and disadvantages

Writing procedures in a database is a debatable topic beyond the scope of this course,  but it is good to be aware of what causes the controversy:

**Advantages**

- **Reduction of network traffic** - data processing is done in the database and we pass on only the result instead of the entire data set,
- **Centralization of business logic in the database** - everything is done in the database, in one place,
- **Increasing the security of the database** - the procedure can be used only by the people with access to the database and with the ability to call it.

**Disadvantages:**

- **Difficult debugging** - one of the major drawbacks. Database-side procedures are very difficult to debug, usually due to not having a debugger, or if there is one, it is usually severely and we can not verify the query during execution,
- **Difficult maintenance** - no less important disadvantage, however, procedures created in the database are hard to version (e.g. in `GIT`) and so testing and deployment is difficult.
