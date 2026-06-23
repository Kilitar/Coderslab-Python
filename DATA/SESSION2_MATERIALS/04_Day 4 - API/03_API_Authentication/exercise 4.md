# Exercise 4

Type: Exercise

# Exercise 4

## Part 1

With the `input` function ask the user what currency they want the PLN to be converted to.

Then ask the user for the amount they would like to convert.

Assume that user input is correct. e.g. `USD`.

With the `requests` library, query the current exchange rate of the input currency to `PLN`. Use the resulting rate in your calculations to convert the specified amount into the currency of your choice, and display the result in the form:

``` 
<INPUT AMOUNT> PLN = <CALCULATED AMOUNT> <INPUT CURRENCY>
```

E.g. if the user enters `USD` and `1000`:

``` 
1000 PLN = 269.44 USD
```

Use the `round` function to give the result to two decimal places.

## Part 2

Test your code by specifying a currency that does not exist.

Do not modify the code that asks the user and sends the request to the server. **Using nothing but the server response** decide whether you need to display the converted amount (as in part 1 of the exercise), or to inform the user that the currency they entered does not exist. **Hint:** responses to incorrect queries have a special `status_code`.

E.g. if the user enters `LOL` and `1000`:

``` 
There is no such currency!
```
