# Summary

Type: Article

The first session of the Python Data Analysis course is behind you - it's time to sum up all the knowledge you've gained.

## Functions

A function is code that you can jump to, execute it, and then return with the result to the place it was called from. A good function solves **one** problem comprehensively - so it will be easy to use it many times, in many places.

Syntax:

``` python
def function_name(comma, separated, arguments):
    # function code
    # always indented in relation to "def"
    return function_result # also the end of the function
# no indent - this line is not part of the function!
```

## Text strings

Strings are variables of the `str` type. In Python, you can declare them in several ways:

``` python
"Text"
```

``` python
'Text'
```

``` python
"""Three
lines
of text"""
```

``` python
'''Three
lines
of text'''
```

Strings can be added together.

``` python
print("Violets" + " " + "are" + " " + "blue")  # Result: Violets are blue
```

Strings can be replicated with the multiplication operator – the type of number has to be `int`:

``` python
print("ho " * 5)  # Result: ho ho ho ho ho
```

### Formatting text

You can also write a text template, and then fill it in:

``` python
address = """Hand- Deliver to {} {},
{} Apt. {}
{} {}"""
print(address.format('Thomas', 'Anderson', 'Mockingbird Lane', 101, '1313', 'Anytown'))
```

The result is:

``` 
Hand- deliver to Thomas Anderson,
Mockingbird Lane Apt. 101
1313 Anytown
```

Another way is to name gaps in the text:

``` python
email = "{username}@{domain}"
print(email.format(username='jconnor', domain='somewebsite.org'))
```

The result is:

``` 
jconnor@somewebsite.org
```

### f-string

The **F-string** is declared by preceding the regular string with the letter `f`:

``` python
e = 2.71
pi = 3.14
print(f"The value of e constant is {e}, and pi is {pi}")
```

Result:

``` 
The value of e constant is 2.71, and pi is 3.14
```

## Lists, tuples, and sets

These are containers for other data. Lists - they remember the order and allow repeated values. Sets, on the other hand, decide the order themselves, and don't allow duplicates - a set is used to see if an element is in it or not.

``` python
my_list = ['This', 'is', 'a', 'list!']
my_tuple = ('and', 'a', 'tuple')
my_set = {'or', 'a', 'set!'}
print(my_list)
print(my_tuple)
print(my_set)
```

Result:

``` 
['This', is', 'a', 'list!']
('and', 'a', 'tuple')
{'set!', 'or', 'a'}
```

Each of these structures can be converted to another one using: `list(...)`, `tuple(...)` i `set(...)`.

You can read more about them [in the documentation](https://docs.python.org/3/tutorial/datastructures.html).

**Note:** To declare an empty string use `set()`instead of `{}`.

## Dictionaries

It's a data structure that allows you to give a label to any value. It is used to organize code and data. A single dictionary doesn't offer much benefit yet - instead of using a dictionary and several keys, you can use several variables; only a list of multiple dictionaries shows how useful they are.

Creating a dictionary:

``` python
my_dict = {
  'name': 'Buddy',
  'type': 'Dog'
}
```

Adding new data (or changing existing data) to an existing dictionary:

``` python
my_dict['breed'] = 'Dachshund'
```

Reading data:

``` python
name = my_dict['name']
```

Removing data from a dictionary:

``` python
del my_dict['type']
```

## Keyword `in`

You can think about it as yet another operator (along with `<`, `==`, `!=`, etc.). The result is `True` or `False`.

The operator behaves differently for different types of data:

``` python
some_value in my_list  # is the element in my_list?
some_value in my_tuple  # is the element in my_tuple
some_string in some_bigger_text  # is some_string a part of some_bigger_text?
some_value in my_dict  # does my_dict have a key with some_value?
```

## Exceptions

Sometimes an operation will end with an error, such as trying to read the fifth element from a three-element list. How to terminate such an operation? One of the first ideas that come to mind is to return `None`. But returning `None` may suggest that `None` was actually the fifth element – can you imagine how frustrating debugging such a program would be?

Instead of **returning** the result, the operation can **throw an exception** - the very syntax makes sure that the two cannot be confused.

``` python
my_list = ['Simson S51', 'Jawa 350', 'Daewoo Tico', 'Peugeot 206']
try:
    # this code can finish with IndexError:
    print(my_list[4])
except IndexError:
    print('Sorry, you have never owned that many vehicles!')
```

## Files

To open files Python uses `open(file_name, mode='r')`.

Specifying only the name of a file will open it for reading - it must previously exist on disk.

Passing`"w"` as the second argument results in opening the file in the write mode – if the file already exists it will be overwritten.

Once you finish working with the file you need to close it with `.close()`. Python also provides us with syntax that will see to it that the file will close itself when it is finished:

``` python
with open('my_file.txt') as my_file:
    # you can used the opened my_file here

# after you leave the "with" block the file is closed
```

## Regular expressions

**Regular expressions** provide the ability to define a "text pattern". - a more general definition of what we want to find or replace.

Python's built-in `re` module is used to handle regular expressions. There, we can find functions such as: `re.findall`, `re.search`, `re.sub` and `re.match`.

It is important to precede the text that is a regular expression with the letter `r`. Thanks to this, combinations such as `\n` will not be interpreted by Python in the special way and will have a chance to reach the function code in the `re` module unchanged.

`r"This is [mruoy]{2,4} regex!"`
