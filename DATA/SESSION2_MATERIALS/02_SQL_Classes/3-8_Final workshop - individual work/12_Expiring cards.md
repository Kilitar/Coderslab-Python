# Expiring cards

Type: Exercise

## Expiring cards

Write a procedure to refresh the table you created (you can call it e.g. `cards_at_expiration`) containing the following columns:

- client_id,
- card_id,
- expiration_date - assume that the card can be active for 3 years after issue date,
- client_address (column `A3` is enough).

> **Note:**
> The `card` table has cards that were issued until the end of 1998.

> **Determining the card's expiration date:**
> 
> 
> 
> 
> Suppose we have a card issued on `2020-01-01`, its expiration date according to the exercise conditions is `2023-01-01`.
> Because we want to mail new cards a week before the expiration date, then we just need to check the condition `2023-01-01 - 7 days = 2022-12-25 <= DATE <= 2023-01-01`.
