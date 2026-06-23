# Exercise 2

Type: Exercise

# Exercise 2

Fill out the PostgreSQL connection data in the code. Run a few queries and find out some information about the client **Muscle Machine Inc**.

To do it, first you need to know the `customerNumber` of the **Muscle Machine Inc** customer - this part of code is ready.

Then check (each point is a separate query and display of the results):

- name and surname of the customer's contact person (edit the query that reads `customerNumber`)
- what is the name of the salesperson taking care of this customer (again, edit the query to learn the employee ID - and with another query read the information about this employee)
- identification numbers, statuses, and their order comments (that is all data from the `orders` table where the `customerNumber` column has the same value as the identification number of **Muscle Machine Inc** customer)
- the check numbers and the amounts this customer paid.

Remember that queries are simple strings - you can embed variables into them in several different ways, including the f-string syntax:

``` python
cursor.execute(f"SELECT orderNumber, status FROM orders WHERE customerNumber = {customerNumber}")
```
