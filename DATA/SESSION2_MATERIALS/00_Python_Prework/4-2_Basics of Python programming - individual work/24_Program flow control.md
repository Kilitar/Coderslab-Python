# Program flow control

Type: Article

![Program flow control](/presentations/DTL/en/4.9/W/M_04_S_02/194227df-9b71-4fd7-9d3c-c6847cd01546/student_content/f5d3a343-f869-430a-869b-d5a3cd5a36bb/images/kontrola_przeplywu_programu.jpg)

## Introduction

Imagine a situation where you write a program based on data that a user enters.
For example, a login panel. The user has to enter a login and password to log in.
The application they log into needs to check if the login and password match.
If so, the user is logged in. If not, an appropriate message is displayed,
for example: "Wrong sign-in data".

In the above example, you can see a situation where the programmer has to check the data
and, based on them, decide what to do next. You will need **conditional statements** for this type of situations.

Look at another example. We need to display the data of all the users on the screen. We could use the function `print` as many times as we have users.
You probably instinctively feel that this is not the best possible name. Here, **loops** come to our aid.

These are just two of the many possible uses of **conditional instructions** and **loops**.
They are the subject of this article.

## Conditional statements

Conditional instructions in Python consist of two parts: the instruction itself and a block of code.
The code block will only execute if the statement is met.

Conditions can be grouped using expressions `if`, `elif`, and `else`.

1. `if` – the first condition. The code block is executed when it is fulfilled.
2. `elif` – subsequent conditions. The code block is executed only if the condition is fulfilled
  and none of the previous conditions has been.
3. `else` – code block is executed only if none of the above conditions are fulfilled.

##### Example:

``` python
if condition:
    # code block
    # executed if condition is True

elif other_condition:
    # code block
    # executed if other_condition is True
    # but condition is false

else:
    # code block
    # executed if no conditions
    # above are met
```

**Condition** is nothing more than a logical expression that returns `True` or `False`.
More precisely, it is evaluated to a boolean value, because it can be, for example, a variable storing a list or a string of text.
If it is an empty list or empty text, it will be treated as `False`, otherwise as `True`.

A conditional statement can be compared to a statement present in natural language:

1. `if` the condition is met, then execute the instructions in the code block below,
2. if the previous condition is not met and if (`elif`) this condition is met, execute this instruction,
3. if none of the above conditions are met (`else`), execute the instruction below.

Parts `elif` and `else` are optional. A conditional statement may contain any number of `elif` expressions.

### Code block

Notice the colon (`:`) following the conditional instruction. It is mandatory. The instructions that will be executed are in the code block below.
In Python, a block of code is defined by indentation. 4 spaces are recommended.
If you use **PyCharm** (which we recommend) you can use a tab instead of four spaces.
(It is converted to 4 spaces by the program).

This is not just a matter of appearance. If you forget to indent, Python will throw the `IndentationError`.

##### Example:

``` python
if 5 > 3:
print("Missing Indentation!")
```

##### Result:

``` 
File "<ipython-input-29-6b0c5b10458f>", line 2
    print("Missing Indentation!")
        ^
IndentationError: expected an indented block
```

### Keyword `pass`

Python expects a block of code after each conditional statement. If for some reason you don't want to include a meaningful command, use the `pass` keyword.

**The code block must not be empty.

This command does nothing, it only fills the empty space and protects you from an error
resulting from an empty code block.

##### Example:

``` python
if condition:
    pass
elif other_condition:
    pass
else:
    pass
```

### Password validation (example)

To better understand how the conditional statement works, let's analyze the following program. We take a character string from the user and write it to the variable `password`.
Then we check its length:

- if it is shorter than 5 characters, we display the message: `"Password is too short!"`,
- if it is longer than 10 characters, we display the message: `"Password is too long!"`,
- otherwise we display: `"Perfect password!"`.

##### Example:

``` python
password = input("Enter password: ")

if len(password) < 5:
    print("Password is too short!")
elif len(password) > 10:
    print("Password is too long!")
else:
    print("Perfect password!")
```

Other examples of conditional statement usage:

- If the password is incorrect: display a message to the user and ask them to log in again.
- If the element on the page is visible - hide it, otherwise - show it.
- After user entry: if the user does not have a valid subscription - log them out.

---

## Loops

Loops allow you to execute some instruction repeatedly. There are two types of loops in Python:

- `for` loop,
  -`while` loop

### `for`loop

![for loop](/presentations/DTL/en/4.9/W/M_04_S_02/194227df-9b71-4fd7-9d3c-c6847cd01546/student_content/f5d3a343-f869-430a-869b-d5a3cd5a36bb/images/p%C4%99tla%20for_en.png)

The most common loop in Python is the `for` loop. It is based on iterators, i.e. elements
over which we can iterate.

> **Iteration** (from Latin *iteratio* - repetition) - the act of repeating the same operation
> in a loop a certain number of times or until a certain condition is met.

An example of such an iterator is a list. The `for` loop will perform the operation for each of its elements, assigning them to variables.
It will end its operation when it has retrieved all the elements from the list.

The operations are placed in a **code block**. Remember to indent this block!

##### Example:

``` python
data = [1, 2, 3]

for element in data:
    print(f"Element : {element}")
```

- `element` – variable to which subsequent elements of the list will be assigned,
- `print(f"Element : {element}")` – a block of code executed for each element. It can be of any length.
  **Remember to indent!**

##### Result:

``` 
Element: 1
Element: 2
Element: 3
```

There can be any values in the list. For example, the names of characters from the "Star Wars" movie:

##### Example:

``` python
heroes = [
    "Luke Skywalker",
    "Princess Leia",
    "Han Solo",
    "Chewbacca",
    "Obi-Wan Kenobi"
]

for character in heroes:
    print(character)
```

##### Result:

``` 
Luke Skywalker
Princess Leia
Han Solo
Chewbacca
Obi-Wan Kenobi
```

#### `range` instruction

Sometimes we need to execute our instruction a certain number of times. We could create a list with consecutive numbers, but this solution is not really efficient.
In such case, the `range` instruction comes in handy.

The `range` instruction must take one parameter: it is the upper bound of the returned values.

##### Example:

``` python
for i in range(10):
    print(i)
```

##### Result:

``` 
0
1
2
3
4
5
6
7
8
9
```

- By default, values are generated from zero.
- **The last number generated is one less than the specified range**.

If you want, you can limit the range of returned values by setting a lower bound.

##### Example:

``` python
for i in range(5, 10):
    print(i)
```

##### Result:

``` 
5
6
7
8
9
```

You can also specify a third parameter – (`step`). It specifies the difference between successive values.

##### Example:

``` python
for i in range(0, 10, 2):
    print(i)
```

##### Result:

``` 
0
2
4
6
8
```

The step can also be negative. In that case, the values are generated in descending order. Therefore, remember to enter bounds in reverse order.

##### Example:

``` python
for i in range(10, 0, -1):
    print(i)
```

##### Result:

``` 
10
9
8
7
6
5
4
3
2
1
```

Finally, let's examine an example of how you can use `range` to create a list:

- We can create an empty list and then add more values to it using a loop.

##### Example:

``` python
result = []
for i in range(10):
    result.append(i)

print(result)
```

##### Result:

``` 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

We can also cast to a list:

##### Example:

``` python
result = list(range(10))

print(result)
```

##### Result:

``` 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Voilà! The list is ready without much of a hassle.

### `while` loop

![while loop](/presentations/DTL/en/4.9/W/M_04_S_02/194227df-9b71-4fd7-9d3c-c6847cd01546/student_content/f5d3a343-f869-430a-869b-d5a3cd5a36bb/images/p%C4%99tla%20while_en.png)

The simplest loop. It can be compared to the statement:

"as long as the condition is met, repeat the block of code".

In Python, `while` looks like this:

``` python
while condition:
    # code block executed in loop
```

##### Example:

``` python
i = 0
while i < 10:
    print(i)
    i += 1  # short for i = i + 1
```

##### Result:

``` python
0
1
2
3
4
5
6
7
8
9
```

The above example is just to show how using the `while` loop looks like. In this case, a much better choice would be to use the `for` loop with the `range` statement.
In a moment, a practical example.

### When to use `for` and when to use `while` loop

In practice, we use the `for` loop when we are given a collection (e.g. a list), or we know how many times we want to execute an instruction.
The `while` loop can be used when we cannot predict how many iterations the loop should make.
Here is a good example of using the `while` loop:

##### Example:

``` python
import random

i = 0
while i != 5:
    print(i)
    i = random.randint(1,10)
```

- `import random` – we import the module for generating random numbers.
- `while i != 5:` – execute the instruction as long as `i` is different from 5.
- `i = random.randint(1,10)` – substitute `i` with a random value between 1 and 10.

##### Result (sample):

``` 
0
7
9
8
```

> In an earlier article, we mentioned that you should avoid single-letter variable names.
> However, in the examples above, we used the variable `i`. This is the conventional name for a variable that takes
> consecutive numeric values and in this particular case is not an error.

## Keywords `break` and `continue`

### `break`

You can break a loop at any time using the `break` keyword. It is most often used
in combination with a conditional statement. It works both with the `for` and `while` loop.

##### Example:

``` python
import random

i = 0
while i < 3:
    print(i)
    if random.randint(1,10) == 5:
         print("break")
         break
    i += 1
```

We want to break the loop if the drawn value is `5` or if 3 draws occur.

##### Result (sample):

``` 
0
1
break
```

### `continue`

The `continue` keyword allows you to move immediately to the next iteration of the loop, without executing the instructions below it.

##### Example:

``` python
sum_even = 0
for i in range(10):
    if i % 2:
        print(f"i = {i} skip odd numbers!")
        continue

    print(f"i = {i}")
    sum_even += i

print(f"The sum of even numbers in range 0 - 9: {sum_even}")
```

##### Result:

``` 
i = 0
i = 1 skip odd numbers!
i = 2
i = 3 skip odd numbers!
i = 4
i = 5 skip odd numbers!
i = 6
i = 7 skip odd numbers!
i = 8
i = 9 skip odd numbers!
The sum of even numbers in range 0 - 9: 20
```

## `for – else` construction

There is a very useful construction that most programmers are not familiar with.
It consists of a loop with a `break` statement nested inside it, and an `else` statement.

The code block under the `else` statement is executed only if the `break` instruction has not ran.
Examine the following example.

##### Example:

``` python
numbers = [1, 3, 5]

for i in numbers:
    if i % 2 == 0:
        print("Even number found!")
        break

else:
    print("There are no even numbers on the list!")
```

##### Result:

``` 
There are no even numbers on the list!
```

Now, let's modify the input list:

``` python
numbers = [1, 2, 5]

for i in numbers:
    if i % 2 == 0:
        print("Even number found!")
        break

else:
    print("There are no even numbers on the list!")
```

##### Result:

``` 
Even number found!
```

You can read more about this statement here:

- [https://www.geeksforgeeks.org/using-else-conditional-statement-with-for-loop-in-python/](https://www.geeksforgeeks.org/using-else-conditional-statement-with-for-loop-in-python/)
- [https://book.pythontips.com/en/latest/for_-_else.html](https://book.pythontips.com/en/latest/for_-_else.html)

---

## Summary:

After reading this article you should know:

- what the following instructions are used for:
  
  - `if`,
  - `elif`,
  - `else`,
- how to execute a block of code a certain number of times using the `for` statement,
- what `range` does,

- how `while` works and when to use it,
- what is the difference between `break` and `continue`.

If something is not quite clear, read the paragraph calmly again, looking at the attached links with sources.
