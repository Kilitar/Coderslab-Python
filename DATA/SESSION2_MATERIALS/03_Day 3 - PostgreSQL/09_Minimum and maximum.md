# Minimum and maximum

Type: Exercise

## Min and max

Using Python and SQL, find out what the most expensive and cheapest product (based on the column `MRSP` - Manufacturers Suggested Retail Price) sold by the company.

To do so:

1. Create a database connection object.
2. Create variables for the highest and lowest price. Assign them values of `0` (for highest price) and `math.inf` (for lowest price). Remember to import the `math` library
3. Query the database for all products (the query may be narrowed down to just one column).
4. In a loop, iterate through all the results and:
  
  1. If the product price is lower than the variable storing the lowest price, assign it to that variable;
  2. If the price of the product is greater than the variable with the highest price, then assign that value to that variable.

At the end of the script, display information about these prices.
