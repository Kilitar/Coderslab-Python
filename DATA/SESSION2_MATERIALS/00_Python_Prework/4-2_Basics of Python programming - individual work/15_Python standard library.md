# Python standard library

Type: Article

![Standard library](/presentations/DTL/en/4.9/W/M_04_S_02/953f69e3-6ff7-4b8a-bc5f-b4e1f5e67e8f/student_content/c931b3e7-42a2-450f-8ef5-58399bfdfe60/images/biblioteka_standardowa.jpg)

## Introduction

You have just learned about the basic data types that are available in the Python language. You also know
the operations that can be performed on the data.

In this article, we will talk about some additional operators
and functions that are also part of the standard library. We will cover topics such as:

- Boolean operators
- retrieving data from the user,
- some useful functions available in the standard library.

---

## Standard library

Before we discuss its useful functionalities let's first explain what the standard library is.
By definition:

**standard library** is a library that contains the basic functions, provided with the compiler
or interpreter of a programming language.

In this case this will be the set of basic operators and functions available in Python.

> **Remember: Never use the names of the standard library functions as the names of your variables!**

---

## Operators

In every programming language there are **operators**, which are special characters used to operate on variables.
We can divide them into four parts:

- arithmetic operators,
- Boolean operators
- assignment operators,
- comparison operators.

Now we will discuss each of these groups.

---

## Arithmetic operators

You have already had a chance to learn about arithmetic operators in a previous article. These are operators used
for mathematical calculations. As a reminder:

| Operator | Description |
| --- | --- |
| + | addition |
| - | subtraction |
| * | multiplication |
| / | division |
| // | integer division |
| % | modulo (division reminder) |
| ** | exponentiation |

In addition to the operators mentioned above, we can also use round brackets to group mathematical operations.

##### Example:

``` python
result_1 = 2 + 2 * 2
result_2 = (2 + 2) * 2
print(f"2 + 2 * 2 = {result_1}")
print(f"(2 + 2) * 2 = {result_2}")
```

##### Result:

``` 
2 + 2 * 2 = 6
(2 + 2) * 2 = 8
```

> **Hint:**
> 
> 
> 
> 
> If you want to perform a square root operation, you can use a fraction as the exponent of a power.
> 
> 
> 
> 
> ##### Example:
> 
> 
> 
> ``` python
> result = 4 ** 0.5  # square root of 4
> print(result)
> ```
> 
> 
> 
> ##### Result:
> 
> 
> 
> ``` 
> 2
> ```
> 
> 
> 
> Another option is to use the appropriate function from the `math` library. You will learn how to use the libraries
> later in the course

---

### Boolean operators

**Logical operators** – a group of operators used to compare variables
They always return `True` or `False` (`bool` type).

| Operator | Description | Example |
| --- | --- | --- |
| == | equal | 2 + 2 == 4 # True |
| != (or <>) | not equal | 6 != 1 # True |
| > | greater than | 12 > 10 # True |
| >= | greater or equal | 12 >= 12 # True |
| < | less than | 10 < 12 # True |
| <= | less or equal | 10 <= 10 # True |

Note that in theory we can compare different types of data. However, remember that when comparing a string with a number,
you always get False. Now let's discuss some basics rules.

##### Comparing numbers

You can compare different numbers. There is no reason not to compare integers
with floating point numbers.

##### Example:

``` python
print(100 == 100.0)
print(100 == 1e2)
print(100.0 == 1e2)
```

- `print(100 == 1e2)` – in Python you can also use scientific notation

##### Result:

``` python
True
True
True
```

**Note!** Look below: watch out for rounding errors.

##### Example:

``` python
print(0.1 + 0.2 == 0.3)
print(round(0.1 + 0.2, 1) == 0.3)
```

##### Result:

``` 
False
True
```

> Explanation: `0.1 + 0.2` gives: `0.30000000000000004`. This is because of the way Python stores
> floating point numbers. To avoid this type of error, use the `round` function, which rounds the number
> to the indicated number of decimal places.

The result of the comparison can be assigned to a variable.

##### Example:

``` python
result = 70 < 50
print(result)
```

##### Result:

``` 
False
```

##### Comparing strings

We can also compare strings of characters. This works a little different than comparing numbers. Comparing strings
of characters uses **lexicographic order**.  Examine the following example.

##### Example:

``` python
result_1 = "Alice" == "Alice"
result_2 = "Alice" == "alice"
result_3 = "2" < "10"

print(result_1)
print(result_2)
print(result_3)
```

##### Result:

``` 
True
False
False
```

You can read more about this statement here:

- [https://en.wikipedia.org/wiki/Lexicographic_order](https://en.wikipedia.org/wiki/Lexicographic_order)
- [https://mathworld.wolfram.com/LexicographicOrder.html](https://mathworld.wolfram.com/LexicographicOrder.html)

### Combining logical values

You can combine logical values with the operators `and` and `or`.

#### `and`

If the first condition is not met, the next part is not checked, and the value False is returned.

#### `or`

It is enough that one of the conditions is met for the value of True to be returned.

#### `not`

We can negate the given logical value by preceding it with `not`.

#### `^` (XOR)

The **XOR** operator checks if one of the two conditions is satisfied, while both cannot be satisfied.
If one condition is met, then it returns True; if none or two, False.

##### Example:

``` python
is_ready = True
is_running = False

result_1 = is_ready and is_running
result_2 = is_ready or is_running
result_3 = is_ready ^ is_running
result_4 = not is_ready
result_5 = (is_ready == True) and (is_running == False)  # parentheses are optional; added for readability

print(result_1)
print(result_2)
print(result_3)
print(result_4)
print(result_5)
```

##### Result:

``` 
False
True
True
False
True
```

### Assignment operator

You have already learned the basic assignment operator, which is the `=` character. It assigns a value to a variable.

##### Example:

``` python
number = 42
text = "Lorem Ipsum"
```

There are several other useful assignment operators in Python Before we describe them,
let's introduce two additional concepts: **increment** and **decrement**.

- **Increment** – increasing a value by `1`.

``` python
i = 0
i = i + 1
```

- **Decrement** – decreasing a value by `1`.

``` python
i = 0
i = i - 1
```

These expressions are so popular that shorthand notation was created for them:

- **increment**: `i += 1`
- **decrement**: `i -= 1`

Besides addition and subtraction, we can also use abbreviated notation for other mathematical operations.
It is of course also possible to use a value other than `1`.
Look at the example below:

##### Example:

``` python
i = 10

i += 1  # equivalent i = i + 1
print(i)

i -= 2  # equivalent i = i - 2
print(i)

i *= 10  # equivalent i = i * 10
print(i)

i **= 2  # equivalent i = i ** 2
print(i)

i /= 10  # equivalent i = i / 10
print(i)

i //= 7  # equivalent i = i // 7
print(i)
```

##### Result:

``` 
11
9
90
8100
810.0
115.0
```

**Note!** We should use shorthand notation if possible!

---

## Retrieving data from the user

You already know how to display information from the program to the user using the `print` function.
Now let's see how to easiest retrieve the information coming from the user. The `input` function is used for this.
It takes one optional parameter which is a string. It is displayed to the user when
the program waits for keyboard input. How to use it? Let's see:

##### Example:

``` python
user_lucky_number = input("Enter your lucky number!")
```

##### The parameter is optional. It can also be written like this:

``` python
print("Enter your lucky number!")
user_lucky_number = input()
```

##### Data submitted by the user is always stored as a string. Even if it is a number!

What if you want to perform some operations on data that has been submitted using the `input` function?
We have to use type conversion.

## Type conversion

As you probably noticed, for some operations (for example, division), there was an automatic type conversion of `int`
to `float`. We can force explicit type conversion. Of course, only if it is possible. Some operations
are not possible on different data types For example, if we try to add a number to a string, Python will
throw an error.

##### Example:

``` python
result = 42 + "PLN"
```

##### Result:

``` 
--------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-8-1d9501e161d0> in <module>()
----> 1 42 + "PLN"

TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

The conversion can be done by entering the name of the **type** and putting the value in brackets. Of course, such conversion must
be possible. Otherwise, we will get an error.

Here are some examples of the most commonly used conversions.

- int → string:

``` python
text = str(2)  # '2'
```

- string → int:

``` python
value = int("42")  # 42
```

- int → float

``` python
value = float(128)  # 128.0
```

- string → list

``` python
letters = list("Alice has a cat")  # ['A', 'l', 'i', 'c', 'e', ' ', 'h', 'a', 's', ' ', 'a', ' ', 'c', 'a', 't']
```

- list → string

``` python
text = str([42, "text"])  # "[42, 'text']"
```

- string → bool

``` python
is_checked = bool("checked")  # True
is_not_checked = bool("")  # False
```

> If the conversion is not possible, we get an appropriate error:
> 
> 
> 
> 
> ##### Example:
> 
> 
> 
> ``` python
> value = int("blah")
> ```
> 
> 
> 
> ##### Result:
> 
> 
> 
> ``` 
> ---------------------------------------------------------------------------
> ValueError                                Traceback (most recent call last)
> <ipython-input-9-85d4770f5a23> in <module>()
> ----> 1 value = int("blah")
> 
> ValueError: invalid literal for int() with base 10: 'blah'
> ```

## Useful Python built-in functions

See below for some useful functions available in the standard library. There are many more. You can find them all in the official documentation:
[https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html).

- `abs`: returns absolute value of the given number.

``` python
result = abs(-42)  # 42
```

- `eval`: executes Python code placed in a text string. This function should not be overused, as it provides an
  opportunity to perform **code injection** attacks.

``` python
result = eval("2 + 2 * 2")  # 6
```

> **Code injection** – a type of attack passing malicious code in data. For example, we want to execute the code entered by
> the user with an `input` function. A sneaky user with malicious intentions can include instructions in the code,
> which, for example, will delete files placed on our hard drive.

`len`: returns the length of a list or string (Do you remember this instruction from one of the earlier articles)

``` python
result = len([1, 2, 3])  # 3
```

- `max`: returns the maximum value from a list.

``` python
result = max([1, 2, 3])  # 3
```

- `min`: returns the minimum value from a list.

``` python
result = min([1, 2, 3])  # 1
```

- `pow`: raises a value to the specified power. The same can be done with the `**` operator.

``` python
result = pow(2, 10)  # equivalent to: result = 2 ** 10
```

- `sorted`: returns a sorted list.

``` python
result = sorted([2, 3, 1])  # [1, 2, 3]
```

- `sum`: return the sum of list elements.

``` python
result = sum([1, 2, 3])  # 6
```

- `type`: returns the type of the given object.

``` python
result = type(42)  # int
```

- `round`: rounds a fraction to the given number of decimal spaces.

``` python
result = round(3.14159, 2)  # 3.14
```

## Summary

In this article, you learned about the basic operations available in the Python standard library.
You know how to retrieve data from the user. You know how to convert different types of data. You have also learned a number of useful functions.
Don't try to learn the names of these functions by heart - you can find any of them on the web in a few seconds.
Instead, try to remember what they do.

> **Pro tip**
> If you forget something, all you have to do is use a search engine, and type something like: `How to sort list in Python?` But if you don't remember that such a functionality exists... you won't know what to look for.

Over time, you will remember the most commonly used functionalities. It is impossible to remember all of them: there are too
many. The sooner you learn to use the official documentation, the better.
Therefore, to better consolidate your knowledge, try to find in the documentation functionalities mentioned above and
read their descriptions. This is where you'll find them: [https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html).

If something is not clear enough, read the paragraph calmly again, looking at the attached links
with sources.
