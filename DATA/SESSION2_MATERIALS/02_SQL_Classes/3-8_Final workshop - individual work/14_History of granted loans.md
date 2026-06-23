# History of granted loans

Type: Article

## History of granted loans

Write a query that prepares a summary of the granted loans in the following dimensions:

- year, quarter, month,
- year, quarter,
- year,
- total.

Display the following information as the result of the summary:

- total amount of loans,
- average loan amount,
- total number of given loans.

## Solution:

In the exercise, the main thing is to use the `EXTRACT` function with the appropriate parameters, followed by `GROUP BY WITH ROLLUP`. This will give us all the summaries we are interested in with a single query:

### Preparing the grouping set

We will start by preparing a template of the query:

``` 
SELECT *
FROM financial.loan
```

The next step will be to use the `EXTRACT` function to get the information we are interested in from the `date` column:

``` 
SELECT
    -- first we extract what we need from the date column
    extract(YEAR FROM date) as loan_year,
    extract(QUARTER FROM date) as loan_quarter,
    extract(MONTH FROM date) as loan_month,
FROM financial.loan
```

In this way, we have prepared the appropriate columns with which to perform further aggregation.

``` 
SELECT
    -- first we extract what we need from the date column
    extract(YEAR FROM date) as loan_year,
    extract(QUARTER FROM date) as loan_quarter,
    extract(MONTH FROM date) as loan_month,
FROM financial.loan
GROUP BY 1, 2, 3
```

At this point we have grouped the data by year, quarter and month. To finish this step and generate additional grouping sets, we need to use `ROLL UP`:

``` 
SELECT
    -- first we extract what we need from the date column
    extract(YEAR FROM date) as loan_year,
    extract(QUARTER FROM date) as loan_quarter,
    extract(MONTH FROM date) as loan_month,
FROM financial.loan
GROUP BY 1, 2, 3 WITH ROLLUP
```

### Generating numeric values

The final step of the task is to generate statistics for the granted loans. The following should be used here:

- `SUM` - to count the total amount of loans granted,
- `AVG` - to determine the average loan amount,
- `COUNT` - to determine the number of loans granted.

Because we have already used `WITH ROLLUP`, the remaining grouping sets will be automatically generated.

``` 
SELECT
    -- first we extract what we need from the date column
    extract(YEAR FROM date) as loan_year,
    extract(QUARTER FROM date) as loan_quarter,
    extract(MONTH FROM date) as loan_month,

    -- summaries
    sum(amount) as loans_total,
    avg(amount) as loans_avg,
    count(amount) as loans_count
FROM financial.loan
GROUP BY 1, 2, 3 WITH ROLLUP
ORDER BY 1, 2, 3
```
