# Cleaning and processing data - exercise

Type: Exercise

1. Remove the remaining columns that will not be needed in the context of our analysis.
2. In the pivot table (`null_values` sheet) that checks iif the data is filled in the particular columns, mark the remaining variables and check whether they are complete.
  If the data is not complete, assign default values here, for example, if there is no average number of reviews per month, enter 0. For text values, you can assign the value "Undefined." In the columns where the data type in date, you can assign a remote date value from the past, e.g., "01-01-1970".
3. Create an additional variable: `price_range`, based on the `price` variable, that is going to specify the price range of each offer.
  Implement a three-step scale ("Cheap", "Normal", "Expensive"). Assume that the cost of renting a property:

- is low if the price is less than the median of all bids,
- is average in price, when the price is less than or equal to the 85th percentile
- is high if the price is greater than the 85th percentile

*Hint: You can count median value with MEDIAN(), and 85th percentile with the PERCENTILE() formula.*

### Good luck!
