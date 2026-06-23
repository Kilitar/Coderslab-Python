# Data types in Python

Type: Article

![Data](/presentations/DTL/en/4.9/W/M_04_S_02/0a25bdae-dcbf-4ef7-8ed0-26ffcb9427f9/student_content/54668b88-7385-43c6-a581-64898a460c2f/images/dane.jpg)

## Introduction

In this article, you will learn how a computer stores data and why we need different data types.
We'll discuss basic data types available in Python language, including:

- numbers,
- text strings
- boolean values
- lists.

We will also discuss operations that can be performed on such data.
You'll also learn what variables are and how to use them.

---

## How does a computer store data?

Data in a computer is stored in binary form. This means that all values are stored as strings of zeros and ones.
We won't go into the details here. However, it is worth remembering that all the complex data types that you will be using is translated into binary data.

---

## Variables

![Variable](/presentations/DTL/en/4.9/W/M_04_S_02/0a25bdae-dcbf-4ef7-8ed0-26ffcb9427f9/student_content/54668b88-7385-43c6-a581-64898a460c2f/images/zmienna.png)

In Python, variables are the primary way to store data. In simple terms, a variable is nothing more than a label referring to some area in the computer's memory.
A variable has three basic features, called attributes:

- name,
- storage location,
- value.

One more parameter can be added to this: the type of data stored by the variable. The type can be permanently assigned to the variable, or not.
Based on this property we distinguish different types of programming languages:

- statically typed – the data type is permanently assigned to a variable,
- dynamically typed – there is no such connection.

**Python is a dynamically typed language!**

To understand it better, you can imagine a variable as a box with a label on it. The name on a label
is the name of our variable. You also don't have to worry about where the box is stored - Python takes care of that for you. We only deal with the label and the contents. The contents of the box is the value. In Python, we can put different objects (data types) into the box.

#### Example:

``` python
answer = 42
```

- `answer` – variable name
- `=` – assignment operator
- `42` – variable value

---

## Variable names

Python is a very specific language. On the one hand it allows us to do a lot, on the other hand there are good practices that have recommendations against some things.

For example, the name of a variable:

- has to start with a letter,
- can contain any number of characters,
- may contain letters, numbers and some special characters (the underscore character is most commonly used).

Following these guidelines only, we can create the variable shown below:

``` python
flkjSFGjad_sdf_sgs = 43
```

You probably instinctively feel that this is not the best possible name. Contrary to what you might think, a lot of attention is paid to proper naming of variables.
Some people joke that a programmer spends more time thinking of individual variable names, than thinking of a name for their own child.

Now let's discuss some basics rules of good naming:

- variables should be descriptive: it is better to use the variable `user_id` to store the user id, than the meaningless variable `x`;
- variable names should consist of lowercase letters, underscores, and possibly digits:
  variable `number_of_users_v2` is much more readable than `numberofusers2`;
- variables should be named in English: nowadays more and more projects take place in an international environment.
  Even if you currently work only with people of your own nationality, in the future someone from abroad may join your team; learn to name your variables in English from the start;
- variable names should be as short as possible: variable `phone` will be better than: `phone_number`;
- variable names should not contain a description of the data type: even though some people like to add a type designation to variable names, such as `address_string` or `address_str` for short: this is not a good practice.
  Python is a dynamically typed language, so this can lead to a situation where we find a number or a complex data structure in such a variable;
  
  
  
  
  It is also difficult to look for errors in such code afterwards, as variable names can be confusing.

A few examples of bad names:

|  |  |
| --- | --- |
| number Of Users | contains spaces |
| 4Users | begins with a digit |
| tep%%por | contains forbidden special characters |
| asdf | makes no sense |
| użytkownik | not written in English and contains diacritics |

Lastly, it should be mentioned that variable names are case-sensitive.
The variable `name` is not the same as the variable `Name`.

---

## Constants

Let's add a special type of variables, namely constants. So... constants or variables? These are variables that are immutable ;) In other words, we shouldn't change their values while the program is running. In Python, they are used based on a convention and are named with capital letters separated by the underscore character.

#### Example:

``` python
FINAL_ANSWER = 42
```

From the Python point of view, they are no different from usual variables. Only their name suggests to other programmers that they should not be changed.

---

## Data types

Now let's discuss what data types can be stored in variables.

### Numbers

Python allows us to store two types of numeric data. They are:

- integers (`int`),
- real numbers, otherwise known as floating point numbers (`float`).

(We can also store **complex** numbers, but they are not used often, so we will skip them.)

The maximum size of a number we are able to store depends on the operating system we use and is, respectively:

- 8 to the power of 32 for 32-bit systems,
- 8 to the power of 64 for 64-bit systems.

#### Example:

``` python
# int
income = 900
counter = -18  # negative number
color = 0xf200b5  # hexadecimal number
access = 0o777  # octal number
binary = 0b1101  # binary number

# float
bank_balance = -183.05
product_price = 29.99
pi = 3.141592653589793

# complex
sqrt_minus_four = 2j
complex_number = (5+7j)
```

---

### Operations on numbers

![Operations on numbers](/presentations/DTL/en/4.9/W/M_04_S_02/0a25bdae-dcbf-4ef7-8ed0-26ffcb9427f9/student_content/54668b88-7385-43c6-a581-64898a460c2f/images/operacje_na_liczbach_en.png)

We can perform basic mathematical operations on numbers:

- `+` – addition,
- `-` – subtraction,
- `*` – multiplication,
- `**` – exponentiation,
- `/` – division,
- `//` – integer division,
- `%` – modulo division.

You are probably already familiar with addition, subtraction, multiplication, or division, so we won't discuss them in more detail.
Instead, let's say a few words about the other operations.

#### Division

In Python version 3.X the result of division is always **cast** as the `float` type. Casting is just a change of data type.
We will say more about this in the next article.

##### Example (Python 3.X):

``` python
result_1 = 9 / 5
result_2 = 10 / 5

print(result_1)
print(result_2)
```

##### Result:

``` plaintext
1.8
2.0
```

---

#### Integer division

**Integer division** returns the integer value from division. No data conversion takes place here as in the case of the normal division.
The data type of the result depends on the input data. If either value (dividend or divisor) is of the floating point type (`float`), the result will also be of the floating point type.
If both values are integers, the result will also be an integer.

##### Example:

``` python
result_1 = 9 // 5
result_2 = 9.0 // 5
result_3 = 9 // 5.0

print(result_1)
print(result_2)
print(result_3)
```

##### Result:

``` plaintext
1
1.0
1.0
```

What happens in the case of dividing by zero? This operation is, of course, incorrect - so Python will throw an error:

##### Example:

``` python
result_1 = 5 / 0
```

##### Result:

``` plaintext
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-9-0106664d39e8> in <module>()
----> 1 5/0

ZeroDivisionError: integer division
```

---

### Modulo division

**Modulo division** is simply the division remainder. For positive numbers, it works exactly the way we were taught at school.

##### Example:

``` python
result_1 = 10 % 2
result_2 = 13 % 3
result_3 = 1523 % 13

print(result_1)
print(result_2)
print(result_3)
```

##### Result:

``` plaintext
0
1
2
```

**Modulo** for negative numbers is a bit more complicated and we won't cover it here. You can read more about it here:

- [https://en.wikipedia.org/wiki/Modulo](https://en.wikipedia.org/wiki/Modulo)
- [https://math.stackexchange.com/questions/519845/how-to-calculate-a-b-bmod-n-and-b-bmod-n](https://math.stackexchange.com/questions/519845/how-to-calculate-a-b-bmod-n-and-b-bmod-n)

---

### Text strings

Another type that can be stored in variables is a text string, represented in Python by the `str` type. In Python version 3.X, this is a string of unicode characters.
In Python 2.7, to interpret a string as unicode, it needed to be preceded by a `u` character.
Currently all texts are `str` type objects. To create a string longer than one line, put it in triple quotes.

#### Example:

``` python
company = 'CodersLab'
best_programming_language = "Python"
crawler = """
It is a period of civil war.
Rebel spaceships, striking from a hidden base,
have won their first victory against the evil Galactic Empire.
"""

# Unicode in Python 2
text_to_show = u'The qųičk břoŵń ƒōx ʝūmƥś ŏvēŕ țhę łāżȳ đőģ.'
```

We can put special characters inside the strings, such as the newline character: `\n`.
Because the *backslash* character (`\`) is one of the special characters , to actually write it , we need to prefix it with an additional `\` character.
We may also use the `raw string` construct, which does not interpret special characters.

#### Example:

``` python
text = "first line \n second line"
print(text)
```

##### Result:

``` plaintext
first line
second line
```

#### Example:

``` python
text = r"first line \n second line"
print(text)
```

##### Result:

``` plaintext
first line \n second line
```

> #### Good to know
> 
> 
> 
> - Python 3 supports unicode, which means it supports international diacritics.

---

#### String operations

We can also perform some "mathematical" operations on strings. Division and exponentiation of strings makes no sense and Python is going to throw an error if we try to do it.
Because what would we get by raising:
"Alice has a cat" to the power of 2? On the other hand, two mathematical operations are supported:

- `+` – addition, or more precisely concatenation of strings,
- `*` – multiplication of strings.

*Addition* simply combines strings together. It is important to remember that both components of the addition must be strings.

##### Example:

``` python
result = "Alice " + "has a cat"

print(result)
```

##### Result:

``` plaintext
Alice has a cat
```

*Multiplication* of strings is only possible by an integer. The result is the string written the given number of times.

##### Example:

``` python
result = "blah" * 3
print(result)
```

##### Result:

``` plaintext
blahblahblah
```

---

### Passing variables to strings

In Python, there are several ways to pass a variable to a string. Let's discuss two of them:

- `format` method,
- **fstring**.

##### `format` method

The `format` method allows to easily pass some variables to the string. It consists of two parts:

- first we need to put placeholders for variables in the string, using curly brackets – `{}`,

- then we call the `format` method, passing as many variables as we need.

Sounds complicated? Look at the example below:

##### Example:

``` python3
cat = "Garfield"
result = "{} has a cat named {}.".format("Alice", cat)
print(result)
```

- `{}` – the places where our variables will be.
- `.format("Alice", cat)` – here we pass our data. We can enter it directly or pass it on with the use of variables.

##### Result:

``` plaintext
Alice has a cat named Garfield.
```

There is a second way that is even more convenient. Using the `fstring` syntax. It was first introduced in Python 3.6.
To pass a variable to a string using this construction, add the letter `f` before the string, and then pass the variable in curly brackets `{}`.

##### Example:

``` python
answer = 42
result = f"The answer is {answer}!"
print(result)
```

##### Result:

``` plaintext
The answer is 42!
```

---

### Boolean values

![Boolean values](/presentations/DTL/en/4.9/W/M_04_S_02/0a25bdae-dcbf-4ef7-8ed0-26ffcb9427f9/student_content/54668b88-7385-43c6-a581-64898a460c2f/images/true_false.png)

Python allows us to store Boolean values using the `bool` type:

- `True`
- `False`

> True and False values are always capitalized.

#### Example:

``` python
is_checked = True
development_mode = False
```

The following values are also interpreted as **false**:

- `0` – zero,
- `""` – empty string,
- `None` – a special value representing **nothing**,
- `[]` – empty list (more about lists in a moment),
- `{}` – empty dictionary (you will learn about dictionaries later in this course).

---

### Lists

What are lists? Imagine you want to store 10 different numbers in one variable. You will not be able to do this with simple data types.
Instead, you can use a **list** (type `list`).

A **list** (often called an array in other programming languages) is nothing more than an ordered collection of data.
We declare it like regular variables, but instead of single value we pass data in square brackets – `[]`, separating them with commas (see example below):

##### Example:

``` python
numbers = [1, 2, 3, 4, 5]
club_members = ["Ike", "Mike", "Spike"]
various = [1, None, "x", 4.2, False]
empty = []
```

Notice a few things:

- we put values in square brackets,
- we separate individual values with commas,
- we can put different types of data in a list,
- we can also create an empty list.

#### Retrieving values from a list

The simplest way to retrieve a value from a list is to use **index**. This is nothing more than a number indicating where the element is located in the list.
We place this number in square brackets just after the variable that stores it.

**Remember that elements are numbered from ZERO!** To retrieve the first element we need to use the `0` index.

##### Example:

``` python
club_members = ["Ike", "Mike", "Spike"]
print(club_members[0])
print(club_members[1])
print(club_members[2])
```

##### Result:

``` plaintext
Ike
Mike
Spike
```

What happens if you try to reference an element with an index greater than the index of the last element in the list?
Let's find out:

##### Example:

``` python
club_members = ["Ike", "Mike", "Spike"]

print(club_members[3])
```

##### Result:

``` plaintext
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-10-15d3f83f6683> in <module>()
      1 club_members = ["Ike", "Mike", "Spike"]
      2
----> 3 print(club_members[3])

IndexError: list index out of range
```

As expected, Python threw an error: `IndexError: list index out of range` which says that your index is greater than the list size.

Python also supports **reverse indexing**. Simply put, you can refer to elements by counting them in order from the end of your list.
The following example should make this clearer:

##### Example:

``` python
club_members = ["Ike", "Mike", "Spike"]

print(club_members[-1])
print(club_members[-2])
```

##### Result:

``` plaintext
Spike
Mike
```

- We have retrieved the last and penultimate element of the list, respectively.
- Notice that we index from the end from `-1`, not from `-0`.
- The simplest way to think of reverse indexing is as a **list-length - index** construct.
- In our case, the list length is **3** (the list has **3** elements), so `club_members[-1]` is `club_members[3 - 1]`, which is the same as `club_members[2]`.

Using the index, you can not only retrieve any element of the list, but also overwrite it. See the example below:

##### Example:

``` python
club_members = ["Ike", "Mike", "Spike"]
print(club_members)

club_members[1] = "Big Mike"
print(club_members)
```

##### Result:

``` plaintext
["Ike", "Mike", "Spike"]
["Ike", "Big Mike", "Spike"]
```

#### List operations

You can perform similar operations on a list as you can on strings:

- `+` – addition, or rather concatenation: merges two lists into one,
- `*` – multiplication of the list, it duplicates it the indicated number of times.

##### Example:

``` python
result_1 = [1, 2, 3] + [4, 5, 6]
result_2 = [1, 2, 3] * 3

print(result_1)
print(result_2)
```

##### Result:

``` plaintext
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 1, 2, 3, 1, 2, 3]
```

#### List length

To retrieve the length of a list, use the `len` function. It is built into Python. You can use the same function to retrieve the length of a string.
The length of a list is always equal to the number of elements in it and is greater by one than the index of the last element.

##### Example:

``` python
club_members = ["Ike", "Mike", "Spike"]
club_members_length = len(club_members)
print(club_members_length)

text = "blah"
text_length = len(text)
print(text_length)
```

##### Result:

``` plaintext
3
4
```

#### Adding elements to lists

We can add new elements to a list in several ways. You already know that you can replace an element in a list using an index.
There are also some special methods built into the list. They are:

- `append` – allows you to add an element to the end of the list,
- `extend` – allows concatenation of lists (similar to the `+` operation),
- `insert` – allows to add the element in place of the given index.

> Explanation:
> 
> 
> 
> 
> Function – a piece of code separated from a program, that can be used repeatedly in different places in the program.

> Method – a function assigned to some object (in our case, a list).
> You will learn about both functions and methods later in this course.

##### Example:

``` python
numbers = [1, 2, 3]
print(numbers)

numbers.append(4)
print(numbers)

numbers.extend([5, 6])  # equivalent to `numbers + [5, 6]`
print(numbers)

numbers.insert(2, 42)  # insert number 42 on index 2; rest of the numbers moves one right
print(numbers)
```

##### Result:

``` 
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5, 6]
[1, 2, 42, 3, 4, 5, 6]
```

> For volunteers
> 
> 
> 
> 
> In addition to the methods built into lists mentioned earlier, there are several others. You will learn about them later in this course.
> You can read about them in the official Python documentation:
> [https://docs.python.org/3.7/tutorial/datastructures.html#more-on-lists](https://docs.python.org/3.7/tutorial/datastructures.html#more-on-lists)

## Summary

We have discussed how data is stored in Python. You should already know how to use variables. You have learned about the basic data types and the range of operations that can be performed on that data.
You know what a list is and you know the basic operations that use the list.

If you didn't understand something, read the paragraph calmly again, looking at the attached links with sources.
