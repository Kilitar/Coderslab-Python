# Aggregate functions

Type: Exercise

## Aggregate functions in SQL

Find out the following from the database:

1. What is the size of each order (by size, we mean the number of pieces of all products in that order)?
2. What is the total amount of each order?
3. How many products are there for each product line?
4. What is the average suggested retail price (`MSRP`) for each product line?
5. How many customers are from each country?
6. What is the smallest and largest credit limit for a company per country?

> ## Hint:
> 
> 
> 
> 1. In point 2 we can calculate the amount for the order using `sum(quantityordered * priceEach)`. Such code is going to multiply `quantityordered` and `priceEach` for each row, and then sum them up.
