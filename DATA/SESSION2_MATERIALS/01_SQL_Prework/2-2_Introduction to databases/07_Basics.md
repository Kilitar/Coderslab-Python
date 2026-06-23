# Basics

Type: Article

> Remember to edit the queries according to your database user. For an explanation, see **Course preparation > Connecting to the CodersLab database > Executing SQL queries on the server**.

## Introduction

The basics of logic are the basis of `SQL` queries, and affect its results. The most common business requirement is appropriate row filtering, that is why it is so important to be really familiar with the basics of the `and`, `or`, `not` operators.

In this section we will present only their basic properties and assume (provisionally) that the logical value of a query can take the following values: 1 (true), 0 (false)

In order to show the differences between them, we will use the following business query format:

> I need information on all  **films released with the 'NC-17' rating** `(operator)` **over 60 minutes long**

## `AND`operator

It can be understood as `and/as well as' in plain English. Paraphrasing our query gives us the following table filter condition:

> Find information about **either** 'NC-17' rated, **and** over 60 minute-long films.

It is worth noting that a query formulated in this way will only return **films with a rating of 'NC-17' with a duration of more than 60 minutes**.

Using `SQL`:

``` 
SELECT *
FROM sakila.film
where length > 60 AND rating = 'NC-17'
```

### Logical table

| condition A | condition B | AND |
| --- | --- | --- |
| 1 | 1 | 1 |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 0 | 0 | 0 |

With the `AND` operator only the records that meet **both** conditions will be returned.

## `OR` operator

In plain English: any of the two. Paraphrasing our query gives us the following table filter condition:

> Find information about 'NC-17' rated **or** over 60 minute-long films .

In other words, information about all movies with rating 'NC-17' (with any duration) will be returned, along with movies with any rating with a duration of more than 60 minutes.

Using `SQL`:

``` 
SELECT *
FROM sakila.film
where length > 60 OR rating = 'NC-17'
```

### Logical table

| condition A | condition B | OR |
| --- | --- | --- |
| 1 | 1 | 1 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 0 | 0 | 0 |

With the `OR` operator the records that meet **any** of the conditions will be returned.

## `OR` operator

Also called `Exclusive OR`.

### OR vs. XOR

`Exclusive` is used here to mean **either one or the other - but not both**; from the point of view of logic these are **very different**: XOR can be expressed as:

> Find information about **either** 'NC-17' rated **or** over 60 minute-long films (but not both).

This returns films with 'NC-17' rating and any duration up to 60 minutes as well as all other ratings with the duration over 60 minutes.

Using `SQL`:

``` 
SELECT *
FROM sakila.film
where length > 60 XOR rating = 'NC-17'
```

### Logical table

Also, the logical `XOR` table is significantly different from the `OR` one:

| condition A | condition B | XOR |
| --- | --- | --- |
| 1 | 1 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 0 | 0 | 0 |

That is, only those records that meet **only one** of the conditions will be returned.

## `NOT` operator

The `NOT` operator is intended to negate a certain expression, such as a query.

> Find movies with rating 'NC-17'.

when negated, will turn to:

> Find all movies with a rating other than 'NC-17'.

Using `SQL`:

``` 
SELECT * 
FROM sakila.film 
WHERE NOT rating = 'NC-17'
```

Of course it is also possible to use `<>` here, but the example is only an introduction to syntax.

### Logical table

| condition A | NOT |
| --- | --- |
| 1 | 0 |
| 0 | 1 |

## Summary

In this article we have discussed the logical operators: `OR`, `AND`, `NOT` - these are most commonly used in databases. Still, `XOR` (**exclusive or** ) is also important: in spite of its surface similarity to `OR` (**inclusive or**). It represents a very different logical condition.

The next thing we're going to learn is the combination of individual logical conditions and the order they are executed in.
