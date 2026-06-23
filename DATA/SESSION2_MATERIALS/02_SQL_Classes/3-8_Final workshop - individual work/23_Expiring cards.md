# Expiring cards

Type: Article

## Expiring cards

Write a procedure to refresh the table you created (you can call it e.g. `cards_at_expiration`) containing the following columns:

- client id,
- card id,
- expiration date - assume that the card can be active for 3 years after issue date,
- client address (column `A3` is enough).

> **Note:**
> The `card` table has cards that were issued until the end of 1998.

## Solution:

### Basic query

Let's start by writing a query, which we will later use in the procedure. To get the required data, we need to reach the `district` table from the `card` table via `disp`, `client`:

``` 
SELECT *
FROM
    INNER JOIN
        financial.disp as d using (account_id)
    INNER JOIN
        financial.client as c using (client_id)
    INNER JOIN
        financial.district as d2 on
            c.district_id = d2.district_id
;
```

Assuming that the card from issue is valid for three years, we can now determine its expiration date using `DATE_ADD`:

``` 
SELECT 
    c2.client_id,
    c.card_id,

    -- we calculate the expiration date according to the exercise conditions
    DATE_ADD(c.issued, INTERVAL 3 year) as expiration_date,
    d2.A3 as client_adress
FROM 
        financial.card as c
    INNER JOIN
        financial.disp as d using (disp_id)
    INNER JOIN
        financial.client as c2 using (client_id)
    INNER JOIN
        financial.district as d2 using (district_id)
```

Let's now package it into a sub-query, which we are about to process further:

``` 
WITH cte AS (
    SELECT 
        c2.client_id,
        c.card_id,

        -- we calculate the expiration date according to the exercise conditions
        DATE_ADD(c.issued, interval 3 year) as expiration_date,
        d2.A3 as client_adress
    FROM 
            financial.card as c
        INNER JOIN
            financial.disp as d using (disp_id)
        INNER JOIN
            financial.client as c2 using (client_id)
        INNER JOIN
            financial.district as d2 using (district_id)
)
SELECT * 
FROM cte
```

### Determining the card's expiration date.

> Suppose we have a card issued on `2020-01-01`, its expiration date according to the exercise conditions is `2023-01-01`.
> Because we want to mail new cards a week before the expiration date, then we just need to check the condition `2023-01-01 - 7 days = 2022-12-25 <= DATE <= 2023-01-01`.

With the subquery ready, we can now find those cards that will expire in 7 days from a certain date. As an example, let's take `2000-01-01`:

``` 
WITH cte AS (
    SELECT 
        c2.client_id,
        c.card_id,

        -- we calculate the expiration date according to the exercise conditions
        DATE_ADD(c.issued, interval 3 year) as expiration_date,
        d2.A3 as client_adress
    FROM 
            financial.card as c
        INNER JOIN
            financial.disp as d using (disp_id)
        INNER JOIN
            financial.client as c2 using (client_id)
        INNER JOIN
            financial.district as d2 using (district_id)
)
SELECT * 
FROM cte
-- now from the full list of cards we select only those that are about to expire
WHERE '2000-01-01' BETWEEN DATE_ADD(expiration_date, INTERVAL -7 DAY) AND expiration_date
```

### Creating a table

Now we need to create a table that we will feed with data:

``` 
CREATE TABLE financial.cards_at_expiration
(
    client_id       int                      not null,
    card_id         int default 0            not null,
    expiration_date date                     null,
    A3              varchar(15) charset utf8 not null,
    generated_for_date date                     null
);
```

> We leave doing it on the basis of the query placed above (`CREATE TABLE AS`) as practice.

### Creating the procedure

Before we create the procedure, we need to parameterize our query. Suppose we replace the date `2000-01-01` with the parameter `p_date`:

``` 
WITH cte AS (
    SELECT 
        c2.client_id,
        c.card_id,

        -- we calculate the expiration date according to the exercise conditions
        DATE_ADD(c.issued, interval 3 year) as expiration_date,
        d2.A3 as client_adress
    FROM 
            financial.card as c
        INNER JOIN
            financial.disp as d using (disp_id)
        INNER JOIN
            financial.client as c2 using (client_id)
        INNER JOIN
            financial.district as d2 using (district_id)
)
SELECT * 
FROM cte
-- now from the full list of cards we select only those that are about to expire
WHERE p_date BETWEEN DATE_ADD(expiration_date, INTERVAL -7 DAY) AND expiration_date
```

> Note: The above query will not calculate at this point!

Now all we need to do is create the template of the procedure, which we will supplement with additional queries in a moment:

``` 
DELIMITER $$
DROP PROCEDURE IF EXISTS financial.generate_cards_at_expiration_report; 
CREATE PROCEDURE financial.generate_cards_at_expiration_report(p_date DATE)
BEGIN
END;
DELIMITER ;
```

To make the procedure fully functional, we need to add the following elements:

1. `TRUNCATE TABLE financial.cards_at_expiration` - that deletes the table content,
2. `INSERT INTO` - thanks to which we will complete its contents after `TRUNCATE`, here we will use the previously created query.

Finally we will get:

``` 
DELIMITER $$
DROP PROCEDURE IF EXISTS financial.generate_cards_at_expiration_report; 
CREATE PROCEDURE financial.generate_cards_at_expiration_report(p_date DATE)
BEGIN
    TRUNCATE TABLE financial.cards_at_expiration;
    INSERT INTO financial.cards_at_expiration
    WITH cte AS (
        SELECT c2.client_id,
               c.card_id,
               date_add(c.issued, interval 3 year) as expiration_date,
               d2.A3
        FROM 
            financial.card as c
                 INNER JOIN
             financial.disp as d using (disp_id)
                 INNER JOIN
             financial.client as c2 using (client_id)
                 INNER JOIN
             financial.district as d2 using (district_id)
    )
    SELECT
           *,
           p_date
    FROM cte
    WHERE p_date BETWEEN DATE_ADD(expiration_date, INTERVAL -7 DAY) AND expiration_date
    ;
END;
DELIMITER ;
```

Now all we need to do is check:

``` 
CALL financial.generate_cards_at_expiration_report('2001-01-01');
SELECT * FROM financial.cards_at_expiration;
```
