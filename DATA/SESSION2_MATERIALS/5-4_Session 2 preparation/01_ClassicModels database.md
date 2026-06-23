# ClassicModels database

Type: Article

During the first day of class, we will be using the ClassicModels database. This is a database often used during the course - it contains 8 tables with a total of 59 columns and just under 4,000 rows. It contains data typical for a company dealing with commerce - the tables are about products, customers, orders, etc.

You will find the file with the database schema in the `Session 2 Exercise files.zip` archive. Importing the database from a file has already been described in Prework, in the article "Preparing the database". Remember that first you have to create an empty database – call it `classicmodels`.

## ClassicModels database tables

![ClassicModels base view](/presentations/DTL/en/4.9/W/M_05_S_04/276c7692-18ba-433f-a09d-1972d712f029/student_content/d2a3b12c-918f-42e5-bd3c-6a3515c01633/./images/classicmodels.svg)

Below you will find a list of the tables available in the database - along with a listing of the tables the foreign keys lead to:

- `customers`: information about clients; with a reference to the client advisor (from the `employees` table)
- `products`: information about particular products on offer, with their stocks and indication which of the `productlines` they belong to,
- `productlines`: product categories,
- `orders`: the orders made by the `customers`,
- `orderdetails`: particular items from `orders` indicating the ordered `products`,
- `payments`: information about payments made by particular `customers`,
- `employees`: information about employees along with who the supervisor is (rows in this table reference other rows in the same table), and in which of the `offices` each employee works,
- `offices`: contains the addresses of the particular company offices.
