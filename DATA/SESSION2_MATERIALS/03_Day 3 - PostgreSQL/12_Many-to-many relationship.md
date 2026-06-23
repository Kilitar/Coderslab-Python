# Many-to-many relationship

Type: Exercise

## Many-to-many relationship

Many-to-many relationships are the most difficult types of relationships - they require connecting 3 tables. In the `clasicmodels` database `the best example of such relationship is that between the `orders`and`products` tables.

Let's describe this relationship:

1. There can be many products in one order.
2. One product can be in multiple orders.

Since "pure" many-to-many relationships are not possible to implement in SQL, we solve this problem by using a junction table that is in a one-to-many relationship with our original tables. In our case, it looks like this:

1. A new table `orderdetail` was introduced.
2. The table is in a one-to-many relationship with the `orders` and `products` tables.

Let's try to write an SQL query that will return the following information from the database:

- order id (`orders` table),
- order status (`orders` table),
- code of the ordered product (`orderdetails` table),
- number of items of the ordered product (`orderdetails` table),
- name of the ordered product (`products` table).

To get this:

1. Write a SQL query that loads the order id and status from the `orders` table.
2. Modify the query so that a join with the `orderdetails` is made (we are only interested in the code of the particular order).
3. Modify the query so that a join with the `orderdetails` is made (and add the data we are interested in).
