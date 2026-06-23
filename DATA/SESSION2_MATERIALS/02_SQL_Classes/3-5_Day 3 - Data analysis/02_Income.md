# Income

Type: Exercise

## Income

Aggregate the`payment ` table according to the following rules:

1. determine the total amount of rental shop's income,
2. determine the total amount of rental shop's income divided by customers (for now don't use `JOIN`, only `customer_id`),
3. determine the total amount of rented films per employee,
4. using `date_format` function, do subpoints 2 and 3. split by months and sort the results by the keys: `client_id/staff_id` ascending, `amount` - descending.

> **Hint:**
> Documentation for `date_format` is [here](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html).
