# Film rentals 2

Type: Exercise

## Film rentals 2

Write a procedure `film_rental_store` that tests if it is possible to rent the film at the given store (`stock_part_2` table).

If possible (the film is available), the procedure should:

- return the information, about the stock after renting the film
- and the information that the film is available to rent.

Otherwise, the procedure should:

- return the information that the film is out of stock in the store,
- return the information whether the film can be rented from another store. If so, make a reservation there, that is: reduce the stock.

What parameters does the procedure need to take to be executed?

> You may use [this](https://dev.mysql.com/doc/refman/8.0/en/delete.html). Additionally, offer a different solution.

> **Hint**:
> 
> 
> 
> 
> The stock is updated by removing the appropriate record from the table; remember to start a transaction before `DELETE`.
