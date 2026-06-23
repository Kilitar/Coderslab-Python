# Removing errors

Type: Exercise

## Removing errors

Using the solutions from the previous class and the **product_prices_renamed.csv** file, modify `loc` so that it corrects the errors present in the dataset:

1. In the **date** column, data from 1888 appeared - '1888-0', change the value to 1999-1,
2. In the **date** column, data from 2099 appeared - '2099-13', change the value to 2019-1,
3. There is a spelling error in the **product_types** column - correct it. Number of pieces should be '10pcs.`. Check whether the task was done correctly.
4. Use `loc` to convert the values given in `EUR` to `PLN` with 4.15 exchange rate.
  
  Instead of writing `loc` twice, first query the data for rows where **currency** = `EUR` and save it to a variable.
5. Filter from the set those rows where the price for the product is 3000.

> Remember that `loc` modifies data irrevocably.
