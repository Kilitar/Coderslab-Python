# Advanced filtering

Type: Article

> Remember to edit the queries according to your database user. For an explanation, see **Course preparation -> Connecting to the CodersLab database -> Executing SQL queries on the server**

So far we have learned the basic methods of filtering rows using only one of the `AND`, `OR` connectives. An extension of this topic is to combine them in a single query and apply additional properties.

Filtering is a priceless skill: it allows you to save time when working with data, because you'll only work on records that you're interested in. A collection created in this way is usually called a *domain*.

## Order of connectives

The interpretation of logical conditions is read *from left to right*, but `AND` takes precedence over `OR`. Let's examine the following example:

``` 
SELECT *
FROM sakila.film
WHERE 
    rental_rate = 0.99 
    AND rating = 'G' 
    OR special_features = 'Trailers'
```

How will it be performed?

1. At first only the rows where `rental_rate = 0.99` will be chosen from the `sakila.film` table.
2. Next, from the results from step 1 only the rows where `rating = 'G'` will be selected.
3. From the `sakila.film` table the rows where `special_features = 'Trailers'` will be selected.
4. Next the results from point 2 and 3 will be joined.

> **Note:**
> 
> In point 3, the entire table is searched to find the results.

What if we change the query a little? E.g.:

``` 
SELECT *
FROM sakila.film
WHERE 
    rental_rate = 0.99 
    OR rating = 'G' 
    AND special_features = 'Trailers'
```

How will it be performed?

1. At first only the rows where `rental_rate = 0.99` will be chosen from the `sakila.film` table.
2. Next, from the `sakila.film` table, only the rows where `rating = 'G'` **AND** `special_features = 'Trailers'` will be selected.
3. Results from point 1 and 2 will be joined.

**Note that changing the operator significantly changes the interpretation of the logical condition!**

The conjunctions `AND` and `OR` are customarily compared (respectively) to multiplication and addition, since they have similar properties. However, if you are not sure of the order, you can always combine the conditions into groups using parentheses, e.g.:

``` 
SELECT *
FROM sakila.film
WHERE 
    (rental_rate = 0.99 
    AND rating = 'G') 
    OR special_features = 'Trailers'
```

``` 
SELECT *
FROM sakila.film
WHERE 
    rental_rate = 0.99 
    OR (rating = 'G'
    AND special_features = 'Trailers')
```

Above, the parenthesis was given in such a way that it does not change the previous results, but the code has become more readable, because now there is no longer any doubt about what will be done first and in which groups (**the parenthesis has the highest priority**).

### Parentheses can also be nested

In parenthesis, too, we can write further components of a logical condition, that is, nest them.

For example, to add `in`:

``` 
SELECT *
FROM sakila.film
WHERE 
    rental_rate = 0.99 
    OR (
        (rating = 'G' AND special_features = 'Trailers') 
        OR (film_id in (1, 2, 3, 4))
    )
```

## `NOT` again

The logical conjunction `NOT` appeared when we talked about the basics of data filtering. At this point we will analyze it again, but this time as a way to negate entire logical expressions, where its use is most evident.

Let's make some modification of the previous examples:

``` 
SELECT *
FROM sakila.film
WHERE 
    NOT (rental_rate = 0.99 
    AND rating = 'G')
    OR special_features = 'Trailers'
```

At this point the query changes its interpretation:

> From the `sakila.film` table select the rows that **do not fulfill the conditions** `rental_rate = 0.99`, `rating='G'` or **fulfill** `special_features = 'Trailers'`

Notice that the `NOT` connective only worked for the expression in parenthesis. `NOT` negates the first expression it can apply to.

The table below contains sample logical conditions:

| condition | NOT condition |
| --- | --- |
| p AND q | NOT p OR NOT q |
| p OR q | NOT p AND NOT q |
| NOT p | p |
| NOT p AND q | p OR NOT q |
| NOT (p OR q) AND r | (NOT p AND NOT q) AND r |

`p`, `q` represent certain logical conditions, e.g. `p: rating='G', q: special_features='Trailers'`.

You can find more theoretical examples at this  [link](https://sites.millersville.edu/bikenaga/math-proof/truth-tables/truth-tables.html).

## Others

If we are in the phase of building a query and are not sure which conditions we will use, the following syntax will work well:

``` 
SELECT *
FROM sakila.film
WHERE True  -- an artificial creation for the purpose of forcing the use of a logical conjunction
    AND rental_rate = 0.99 
    AND rating = 'G' 
    OR special_features = 'Trailers'
```

You can easily comment out the individual components of filtering, and you don't have to change much of the code:

``` 
SELECT *
FROM sakila.film
WHERE True
    -- AND rental_rate = 0.99 -- this filtration condition is not going to be considered now
    AND rating = 'G' 
    OR special_features = 'Trailers'
```
