# Multiplication

Type: Exercise

## Multiplication

Create a database procedure with a name of your choice that for the parameters: `base` and `number_of_elements` returns the multiple of base equal to the number of elements.

For example:

``` 
-- calling a procedure with base 2 and number of elements 10
CALL proc_name(@p_base:=2, @p_number:=10)

-- Result:
-- 2,4,6,8,10,12,14,16,18,20
```

> **Note:**
> 
> 
> 
> 
> In order to combine a string and a numeric type, you can take a hint from the following code snippet:
> 
> 
> 
> ``` 
> SELECT CONCAT('I am ', cast(5 as CHAR(10)), ' years old')
> ```
