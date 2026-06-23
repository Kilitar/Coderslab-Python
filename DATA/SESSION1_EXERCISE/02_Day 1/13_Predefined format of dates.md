# Predefined format of dates

Type: Exercise

## Predefined format of dates

Get familiar with the `GET_FORMAT()` method: documentation [link](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_get-format), which has predefined formats of selected date display standards. Format the `payment_date` column from the `sakila.payment` table according to the US standard.

Call the created column: `payment_date_usa_formatted`.

> **Hint:**
> 
> Use the method like this - `GET_FORMAT(DATE, FORMAT_NAME)`.
