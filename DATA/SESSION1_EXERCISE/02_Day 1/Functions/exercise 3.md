# Exercise 3

Type: Exercise

## Exercise 3

Write a function `anonymize(email)`, that takes an email address as an argument, and returns a text consisting of:

- the first three characters in an email address
- three asterisks: `'***'`
- the last five characters in an email address

If the address is less than 10 characters long, the function should return a text consisting of:

- three asterisks: `'***'`
- the last five characters in an email address

Example:

``` python
anonymize('j.connor@gmail.com')
```

``` 
j.c***l.com
```

``` python
anonymize('jco@o2.pl')
```

``` 
***o2.pl
```
