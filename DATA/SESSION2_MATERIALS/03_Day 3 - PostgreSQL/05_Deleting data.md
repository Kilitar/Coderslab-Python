# Deleting data

Type: Exercise

## Deleting data

Our firm is ending the cooperation with `Tokyo Collectables, Ltd`. To do so:

1. Try to delete the data from the `customers` table in the company called `Tokyo Collectables, Ltd`. Think about the message you received. What could it mean?

We already know that we can't delete data that occurs in a relationship. This would result in a data inconsistency (we would have orders for a non-existent company in the system).
In this case `Tokyo Collectables, Ltd` has existing orders in the system. We have to delete them before the database will allow us to delete that company. To do so:

1. Find `customernumber` for `Tokyo Collectables, Ltd`.
2. Delete all orders assigned to this company.

Deleting the orders will also fail - for the same reason. First we have to delete all the details of these orders. To do so:

1. See which numbers `ordernumber` the orders for `Tokyo Collectables, Ltd` have.
2. Delete all details (`orderdetails` table) for these orders. Try to do it with just one query (use the `AND` keyword or the `IN` operator).
3. Delete all orders.
4. Try to delete the company from the database.

The company still fails to be deleted. We still need to discard all payments that are assigned to it in the system. This will be done analogously to deleting order details.

Deleting data from the database is not that simple. The process is designed specifically - to reduce the possibility of accidental deletion of data.
