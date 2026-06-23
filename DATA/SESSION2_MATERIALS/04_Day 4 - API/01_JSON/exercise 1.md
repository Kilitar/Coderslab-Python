# Exercise 1

Type: Exercise

# Exercise 1

Get familiar with the [weather endpoint documentation](https://openweathermap.org/current#name).

Write a `get_weather` function that takes three arguments:

- `city` - name of the city, **required**,
- `state` - name of the state/province, optional,
- `country` - name of the country, optional.

In the function use the API [https://openweathermap.org](openweathermap.org) to check current weather. Use all available information (`city`, `state`, `country`) in the request in such a way that the function still works if only `city` or `city` and `country` is passed.

The function should return a short name of the weather: `"Clouds"`, `"Rain"`, `"Clear"` - read it from the JSON returned by the server.

Remember to pass `appid`.
