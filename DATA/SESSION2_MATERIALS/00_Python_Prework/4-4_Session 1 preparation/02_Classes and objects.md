# Classes and objects

Type: Article

Prework has given us the opportunity to work with data of different types. In this article, we will discuss what a type (also known as a class) is, and what an object (also known as an instance) is.

Take a look at the code below:

``` python
primes = [1, 2, 3, 5, 7, 11, 13, 17, 19]
```

You probably already know that the `primes` variable holds a **list**, with numbers.

Again, look at the code below:

``` python
squares = [1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Here is also a **list** of numbers. What do these two lists have in common, and what makes them different?

## Similarities

In the case of both lists, to add the next element, use:

``` python
selected_list.append(new_element)
```

While to retrieve the last element, use:

``` python
selected_list[-1]
```

There are, of course, many more similarities, but these two will suffice for now.

## Differences

The obvious difference is that the lists have completely different values – `primes` is a list of several prime numbers, `squares` is a list of several consecutive numbers squared. Adding another prime number to `primes` will not make the new squared number appear in `squares` (in fact nothing is going to appear there).

# Classes and objects

As long as the data has the same **type** (or **class**), we can expect the same behavior and properties from it – the fact that you will add a new number with `.append(some_value)` is a feature of Python's in-built `list` type, and not of a specific list (`primes` or `squares`).

The fact that `primes` and `squares` have the same type, does not mean they are the same – the numbers they store are different; querying the first one for its last element gives `19`, the second one: `81`. This is because `primes` and `squares` are separate **instances** (or **objects**).

The `append` we mentioned above is a **method**. Methods are functions associated with some type, and they always work in the context of an instance of that type. See the examples below:

``` python
append(23)  # BAD EXAMPLE! DOES NOT WORK!!!
append(100)  # BAD EXAMPLE! DOES NOT WORK!!!
```

To which list will the number `23` be added, and to which `100`? To none - such code is simply wrong, because it lacks necessary information. To use a method, you need to reach it through the instance whose data we are interested in:

``` python
primes.append(23)
squares.append(100)
```

## Summary

You have just learned some of the basic ideas of object-oriented programming: class, instance and method. As a reminder:

- **Class** (or **type**) - defines how objects look and behave,
- **Object** - an **instance** of a class; multiple objects can share the same class and yet be completely independent of each other,
- **Method** - a type of function that is associated with a class, and only makes sense in the context of objects of that class.

In this course we will not focus on creating our own classes and methods - in the work of an analyst you can make do without this knowledge.

Instead, it is essential to understand what the relationship is between object and class, or method and object - all values that can exist in Python are instances of some type, and this dictates how such values should be handled.
