# Aggregation

Type: Exercise

## Aggregation

Using data from file **product_prices_cleaned.csv**, aggregate the data for each product by month and determine the statistics: `min, max, median, mean, std` for prices (**value** column):

1. skip the national data in the analysis,
2. directly on the object from `groupby`,
3. write a loop that will calculate these values for individual provinces.

Use the `agg` method, and aggregate the data with `'product', 'date'` column to complete the exercise.
