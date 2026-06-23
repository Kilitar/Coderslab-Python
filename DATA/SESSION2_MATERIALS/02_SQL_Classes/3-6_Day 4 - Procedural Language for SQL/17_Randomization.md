# Randomization

Type: Exercise

## Randomization

Write a procedure that first creates a table called `randomizer`, and then fills it with random values (a part of the procedure should be to specify how many values should be in the table). For example:

``` 
CALL fill_randomizer(10)
```

should populate the `randomizer` table with 10 random values from the `0-1` range.

> **Hint**:
> 
> 
> 
> 
> To generate a random value from the `0-1` range, you can take a hint from the example below:
> 
> 
> 
> ``` 
> SELECT rand() -- randomizing from the range of 0-1
> ```

In addition, you can use the following structure code to create a table:

``` 
DROP TABLE IF EXISTS randomizer;
CREATE TABLE randomizer (
    id INT,
    value FLOAT
)
```
