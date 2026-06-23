# Actors ratings

Type: Exercise

## Actors ratings

Using the `actor_analytics`table write a query that groups actors according to the following criteria:

1. if `avg_film_rate` <  2 - 'poor acting',
2. if `avg_film_rate` is between 2 and 2.5 - 'fair acting',
3. if `avg_film_rate` is between 2.5 and 3.5 - 'good acting',
4. if `avg_film_rate` is above 3.5 - 'superb acting.

Call the column created this way: `acting_level` and use it in an analysis that calculates:

1. number of occurrences in each group,
2. the total revenue of each group,
3. number of films in each group,
4. the average rating in a group.

> **Hint**:
> Do the exercise in two steps:
> 
> 
> 
> 1. Write a subquery that creates an `acting_level` column,
> 2. Based on the results from the previous subpoint, do the rest of the exercise.
