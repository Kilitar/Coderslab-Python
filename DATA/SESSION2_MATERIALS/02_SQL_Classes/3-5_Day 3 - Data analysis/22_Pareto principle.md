# Pareto principle

Type: Exercise

## Pareto principle

[Pareto principle](https://en.wikipedia.org/wiki/Pareto_principle) In short states that 20% of the society holds 80% of wealth.

In the context of a video rental company, we want to perform a similar analysis - to do this we will use window functions. Let's once again use the actor data from the `actor_analytics` view and check what % of actors is responsible for what % of income of the rental shop.

How should we approach this task?

1. Create a window function using `ROW_NUMBER`,
2. Using `COUNT` and a empty window (`OVER ()`) count the number of rows in the table,
3. Dividing point 1./2. you are going to get an increasing sequence representing the % of actors,
4. Use your knowledge from subpoints 1-3, to do the calculation for the % of income.

Make an interpretation of the query results for a sample actor.

> **Hint:**

You can perform calculations on window functions, for example.

> ``` 
> MAX(1) OVER () / COUNT(1) OVER ()
> ```

Remember to sort partitions uniformly where necessary. For the purpose of this exercise, we will assume that we sort from maximum to minimum.

You can also use the solution of the cumulative sums exercise to help you here.
