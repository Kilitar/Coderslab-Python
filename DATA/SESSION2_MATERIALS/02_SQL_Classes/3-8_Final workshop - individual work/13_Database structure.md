# Database structure

Type: Article

## Structure of `financial` database

Get familiar with the schema of the database and answer the following questions:

1. What are the primary keys in the individual tables?
2. What relationships do particular pairs of tables have?

## Schema

![schema](/presentations/DTL/en/4.9/W/M_03_S_08/08bd92d2-49bd-498b-bcb3-f6d4eddbea3a/student_content/31983321-6947-4c0b-839f-e535cad1d320/./images/financial.svg)

## Description of tables

### Card

The table contains credit card data

Columns:

- `card_id` - id of the card,
- `disp_id` - id of the card disponent,
- `type` - type of card (classic, gold, etc.),
- `issued` - date of card issue.

### Disp

The table contains information about people assigned to the card. Its name is an abbreviation of the legal term: disponent, and refers to an additional person who can use the card.

Columns:

- `disp_id` - id of the card disponent,
- `client_id` - id of the client,
- `account_id` - id of the account the card is assigned to,
- `type` - type of card management (owner or disponent).

### Client

The table contains basic client information.

Columns:

- `client_id` - id of the client,
- `gender` - gender of the client,
- `birth_date` - date of birth of the client,
- `district_id` - id of the client's area of residence.

### District

The table contains the demographics for the area.

Columns:

- `district_id` - id of the district,
- `A2` - name of the district,
- `A3` - region,
- `A4` - number of residents,
- `A5` - number of communities below 499 residents,
- `A6` - number of communities with 500-1999 residents,
- `A7` - number of communities with 2000-9999 residents,
- `A8` - number of communities above 10000 residents,
- `A9` - number of cities,
- `A10` - ratio of urban to rural area residents,
- `A11` - average salary,
- `A12` - unemployment rate in 1995,
- `A13` - unemployment rate in 1996,
- `A14` - number of entrepreneurs per 1000 residents,
- `A15` - number of crimes committed in 1995,
- `A16` - number of crimes committed in 1996,

### Account

The table contains information about accounts.

Columns:

- `account_id` - id of account,
- `district_id` - id of the district with the branch that opened the account,
- `frequency` - frequency of issuing statements,
- `date` - date of opening the account.

### Trans

The table contains information about transactions

Columns:

- `trans_id` - id of transaction,
- `account_id` - id of the account the transaction is assigned to,
- `date` - date of transaction,
- `type` - debit/credit transaction,
- `operation` - type of transaction,
- `amount` - amount of transaction,
- `balance` - account balance after transaction,
- `k_symbol` - characteristics of transaction,
- `bank` - transaction partner's bank,
- `account` - transaction partner's account.

### Order

The table contains the characteristics of payment order.

Column:

- `order_id` - identifier,
- `account_id` - id of account,
- `bank_to` - id of recipient's bank,
- `account_to` - id of recipient's account,
- `amount` - transfer amount,
- `k_symbol` - payment characteristic.

### Loan

The table contains information about loan status.

Columns:

- `loan_id` - id of loan,
- `account_id` - id of loan applicant's account,
- `date` - data of giving out loan,
- `amount` - amount of loan,
- `duration` - duration of loan,
- `payments` - amount of monthly repayment,
- `status` - loan repayment status.

## Solution:

### Primary key

Here the task is quite simplified, because:

- `account` - `account_id`,
- `card` - `card_id`,
- `client` - `client_id`,
- `disp` - `disp_id`,
- `district` - `district`,
- `loan`- `loan_id`,
- `order` - `order_id`,
- `trans` - `trans_id`.

### Type of relationship

Take `account` and `trans`, that is, the `account` - `client` relationship. We can guess that most likely this is a 1:n type of relationship (one client can have multiple transactions, but each transaction has one client).

Now let's check it with `SQL` (the database schema does not specify the types of relationships):

``` 
USE financial; -- from now on, the default database schema we use is: financial

-- checking type of relationship
SELECT
    account_id,
    count(trans_id) as amount
FROM trans
GROUP BY account_id
ORDER BY 2 DESC
```

Note that in this case, it is enough to check whether there are multiple `trans_id` transactions in the `trans` table for a given `account_id`. We can do this, for example, using `GROUP BY`, as in the example above. Just select the `account_id`, and check the number of transactions for it. Using sorting guarantees that if there is an `account_id` with many transactions in the database, it will appear at the top of the results.

> Of course, this can also be done using `HAVING`. For the purposes of this exercise, these approaches are equivalent.
