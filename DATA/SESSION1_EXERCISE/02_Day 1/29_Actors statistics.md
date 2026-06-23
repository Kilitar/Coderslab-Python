# Actors statistics

Type: Exercise

## Actors statistics

Do the following:

1. Find the actor/actress with the name of ZERO and the surname: CAGE, display all statistics for their id,
2. Display actors who played in at least 30 films,
3. Using the results from the previous point display all of their information from `sakila.actor`.

Additionally:

4. Find the actors who played in the movies with the length of (`longest_movie_duration`) of 184, 174, 176, 164,

5. Using the results from the previous subpoint, find these films in `sakila.film` (this will require more than one subquery).

> **Hint:**
> 
> In the last task you can for example divide the queries for `sakila.actor_analytics` and `sakila.film_actor` tables into modules, and query `sakila.film` at the end, joining them appropriately in `WHERE`.
