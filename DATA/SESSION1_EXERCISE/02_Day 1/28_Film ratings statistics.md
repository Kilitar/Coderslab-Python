# Film ratings statistics

Type: Exercise

## Film ratings statistics

Get familiar with the structure of `sakila.rating_analytics`, which has aggregated information regarding particular ratings for all films. Then do the following:

1. Analyzing only the data structure, consider which row can determine statistics for **all** ratings (without *rating* division),
2. Find the ratings which are **higher** than the average for all movies, without *rating* division,
3. Find the ratings where the renting time is **shorter** than the global average,
4. Use a subquery to display the statistics for `id_rating = 3`,
5. Use a subquery to display the statistics for `id_rating = 3, 2, 5`,

Additionally, as an exercise:

1. Write a query that shows which rating in the most popular one,
2. Write a query that reveals which rating has, on average, the shortest movies.

> Remember to remove the rating for all movies.
