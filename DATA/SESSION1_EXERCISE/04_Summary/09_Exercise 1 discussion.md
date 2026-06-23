# Exercise 1 discussion

Type: Article

## Instruction

Write a `count_letters(text)` function that takes a string as an argument and returns a dictionary with the string characters as keys and the number of occurrences as values.

Example:

``` python
print(count_letters('Katharina'))
```

Result:

``` 
{'K': 1, 'a': 3, 't': 1, 'h': 1, 'r: 1, 'i': 1, 'n': 1}
```

## Discussion

How will you perform such a task when the string is a row of magnetic letters on the refrigerator, and only a pencil and a notebook are available for taking notes?

You will probably draw a blank table, two columns wide. You'll look at the first letter - is it already included in the table? If not, you create a new row, writing "1" in the second column. If such a letter was already there, you'll read its previous count, and replace it with a new one, increased by 1.

When all letters are done, the table in the notebook will be the solution to the task. Now let's do the same thing, but in Python.

Lets start from the declaration of the `count_letters` function:

``` python
def count_letters(text):
    pass
```

The `pass` keyword is here only to ensure the correct syntax of the program: functions cannot be empty.

Next, we will create a dictionary to store the counts of all the letters for us:

``` python
def count_letters(text):
    counters = {}
```

The next step will be to visit each letter:

``` python
def count_letters(text):
    counters = {}
    for letter in text:
        print('Looking at the letter', letter)
```

In the body of the `for` loop we have a chance to execute the same code many times, with a different `letter` from the `text` string in each execution. If there is no such letter we will add it to the dictionary with the counter equal `1` (because we met it for the first time).

``` python
def count_letters(text):
    counters = {}
    for letter in text:
        if letter not in counters:
            counters[letter] = 1
```

We can already tell that the letters in the dictionary were at least once in `text`: now it's time to count the second, and next occurrences:

``` python
def count_letters(text):
    counters = {}
    for letter in text:
        if letter not in counters:
            counters[letter] = 1
        else:
            counters[letter] = counters[letter] + 1
```

The function counts letters correctly but does return the result, it does not have the `return` word, that points to a value that will the result of the function:

``` python
def count_letters(text):
    counters = {}
    for letter in text:
        if letter not in counters:
            counters[letter] = 1
        else:
            counters[letter] = counters[letter] + 1
    return counters
```

It is important for the `return` instruction to be executed **after** the loop and not during it: then the function would finish too soon and its results would be incomplete.
