# Exercise 2 discussion

Type: Article

## Instruction

Write a function,`find_first_duplicate(text)`, that takes a string as an argument, and returns the first letter that, from its position until the end of string, appears more than once. If no letter repeats, the function should return `None`.

Example:

``` python
print(find('Calamary'))
```

Result:

``` 
a
```

## Discussion

Start the task by writing an empty function, just like in task one:

``` python
def find_first_duplicate(text):
    pass
```

The instructions explicitly say that we are looking for the **first** repeating letter, that is, we need to check each letter in turn:

``` python
def find_first_duplicate(text):
    for letter in text:
        print('Looking at the letter', letter)
```

When function is passed the value of `"monitor", the `for`loop first looks at the letter`"m"`, then:`"o"`, then: `"n"`...

Just knowing the letter is not enough, we need to somehow determine if it's the one to return. Let's see if the `str` type offers something that can help. In the [documentation for `str`](https://docs.python.org/3/library/stdtypes.html#string-methods) we can find a description of the `.count()` method - exactly what we need!

``` python
def find_first_duplicate(text):
    for letter in text:
        if text.count(letter) > 1:  # if there's more letters like the one I'm looking at...
            return letter
```

The exercise also mentions that the function has to return `None`, when letters do not repeat. We already met that requirement: if the function ends because it has no more code to execute, by default it returns `None`.
