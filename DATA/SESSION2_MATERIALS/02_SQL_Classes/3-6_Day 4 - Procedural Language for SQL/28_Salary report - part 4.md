# Salary report - part 4

Type: Exercise

## Salary report - part 4

Write a procedure: `generate_salary_report` that as a parameter takes the day to generate the report for and then writes the results to the `employees.salary_report` table.

Additionally assume that the report has to be available **at the end** of the given month.

**For example:**

``` 
-- generating the report in the current view (a kind of exception)
CALL employees.generate_salary_report(NOW());

-- generating the report for '2021-01-31'
CALL employees.generate_salary_report('2021-01-31');

-- the below call should also generate the report for  '2021-01-31'
CALL employees.generate_salary_report('2021-01-05');
```

### Table structure

``` 
SELECT * FROM employees.salary_report;
```

| gender | dept_name | avg_salary | amount | diff | report_date | report_generation_date |
| --- | --- | --- | --- | --- | --- | --- |
| F | Customer Service | 67409.4939 | 7007 | 0.99693363 | 2021-07-31 | 2021-07-21 15:29:21 |
| M | Customer Service | 67202.7916 | 10562 | NULL | 2021-07-31 | 2021-07-21 15:29:21 |
| F | Development | 67575.8459 | 24533 | 1.00202306 | 2021-07-31 | 2021-07-21 15:29:21 |
| M | Development | 67712.5559 | 36853 | NULL | 2021-07-31 | 2021-07-21 15:29:21 |
| F | Finance | 78747.4166 | 5014 | 0.99601109 | 2021-07-31 | 2021-07-21 15:29:21 |

Where:

- `report_date` - date that report was generated for,
- `report_generation_date` - date of generating the report on the server/ date of calling the procedure.

> **Hints:**
> 
> 
> 
> - The function [LAST_DAY()](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_last-day) can prove useful.
> - Remember to delete the appropriate rows before adding them to the database.
> - You can use temporary tables to save interim results.
