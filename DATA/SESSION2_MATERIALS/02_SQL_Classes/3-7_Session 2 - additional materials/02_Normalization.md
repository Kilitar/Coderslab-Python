# Normalization

Type: Article

## Normalization

## Introduction

Database normalization is a process where we restructure the database in accordance with normal forms. Normal form is an organization of the database that is free from redundancy of data, that is data repetition and dependency. There are fundamental normal forms.

Suppose we encounter the following data set:

| Order Number | Client Name | Client Address | Order Date | Order Details |
| --- | --- | --- | --- | --- |
| 101 | Joe Due | 5000 T-Rex Ave, Boca Raton, 33431 Florida | 2020-01-02 | Tires 205 R16, 4 pcs, price 300 USD |
| 102 | Ann Dumna | 1600 Amphitheatre Pkwy, Mountain View, 94043 Calif | 2020-03-22 | Alloy wheels Silver 4  pcs, price 540 USD |
| 103 | John Dude | 1981 Landings Dr Bldg K, Mountain View, 94043 California | 2020-03-14 | Alloy wheels Silver 4  pcs, price 540 USD |
| 104 | Joe Due | 5000 T-Rex Ave, Boca Raton, 33431 Florida | 2020-10-10 | Bulbs, price 20 USD |
| 105 | Joe Due | 401 Dell Way, Round Rock, 78664 Texas | 2020-05-12 | Liquid 1 piece, Warning triangle 1 pc, price 15 USD |

## Characteristics of non-normalized tables

### Disadvantages:

- The same information is stored multiple times in multiple rows, for example, the customer's address.
- Repeated data causes a problem during updates and makes it difficult to maintain data consistency.
- Data is not decomposed, for example, prices in order details do not allow easy calculation of summaries.
- Deletion of an order record results in loss of customer information.
- Adding information to be specified in the future is a problem: for example, data about a customer who has not yet ordered anything.

### Advantages

- In some cases, certain operations are performed faster on non-normalized data. For example, it is not necessary to perform joins.

## First normal form (1NF)

### Atomized columns

| # | Order Number | Client Name | Address | Post Code | City | State | Date | Element | Quantity | Net Unit | Net Total | Tax |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 101 | Joe Due | 5000 T-Rex Ave | 33431 | Boca Raton | Florida | 2020-01-02 | Tires 205 R16 | 4 | 75 | 300 | 7 |
| 2 | 102 | Ann Dumna | 1600 Amphitheatre Pkwy | 94043 | Mountain View | California | 2020-03-22 | Alloy wheels Silver | 4 | 135 | 540 | 7 |
| 3 | 103 | John Dude | 1981 Landings Dr Bldg K | 94043 | Mountain View | California | 2020-03-14 | Alloy wheels Silver | 4 | 135 | 540 | 7 |
| 4 | 104 | Joe Due | 5000 T-Rex Ave | 33431 | Boca Raton | Florida | 2020-10-10 | Bulbs | 1 | 80 | 80 | 7 |
| 4 | 104 | Joe Due | 5000 T-Rex Ave | 33431 | Boca Raton | Florida | 2020-10-10 | Bulbs | 1 | 80 | 80 | 7 |
| 5 | 105 | Joe Due | 401 Dell Way | 21-120 | Round Rock | Texas | 2020-05-12 | Liquid | 1 | 10 | 10 | 7 |
| 5 | 105 | Joe Due | 401 Dell Way | 21-120 | Round Rock | Texas | 2020-05-12 | Liquid | 1 | 10 | 10 | 7 |
| 6 | 105 | Joe Due | 401 Dell Way | 21-120 | Round Rock | Texas | 2020-05-12 | Warning triangle | 1 | 5 | 5 | 2 |
| 6 | 105 | Joe Due | 401 Dell Way | 21-120 | Round Rock | Texas | 2020-05-12 | Warning triangle | 1 | 5 | 5 | 2 |

This form allows us to create convenient reports. We can query for:

- Distribution of orders by state.
- Total values of orders by period.
- The product that sells best.

## Second normal form (2NF)

In this form, there are **no partial dependencies** in the database:

- `Net Total` can be calculated multiplying `Net Unit` by `Quantity`.
- Similarly, `Tax` rate depends only on the type of product and not on the specific order.  *(We naively assume that sales tax remains constant over time and across states)*

> **Potential key** is a name used for the minimum set of attributes (columns) of a relation (table), uniquely identifying each tuple (row) of this relation.

In the second normal form, we want the values to depend entirely on each potential key.

In our case, however, if the city depends on the post code and the tax rate on the type of product: we need a breakdown into separate tables.

![2NF](/presentations/DTL/en/4.9/W/M_03_S_07/5d492312-19d1-4607-a118-8a6c5d1cc211/student_content/f6b22efa-1c7a-47be-acda-bba26aea9e2d/./images/second-normal.png)

The second normal form can be understood as removing trivial dependencies.

> In the second normal form, the assumptions of the first normal form are met.

## Third normal form (3NF).

In the third normal form **there are no transitive dependencies**.

Let's assume that `A, B, and C` are columns and:

- `A` -> `B`,
- `B` -> `C`.

We can say that `A->C` is a transitive dependency.

In our case, the attributes:

- Post code,
- City,
- State,

could potentially be considered a transitive dependency, but because there are towns with the same name but with a different code and in different states, the definition is not met.

## Summary

- Normalization is giving the data model more and more restrictive rules about the structure.
- Normalization makes the data more structured.
- In some cases, it is useful to carry out the reverse process - denormalization, to improve the efficiency of reading some data that require recalculation in a normalized database.
