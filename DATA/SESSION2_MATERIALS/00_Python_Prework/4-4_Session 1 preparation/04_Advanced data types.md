# Advanced data types

Type: Article

From this article you will learn what primitive (basic) and complex types Python offers, how they differ, and what data types will be most useful in the work of a data analyst.

## Primitive types

Primitive types are those that store only one information item (`int` or `float`), logical value (`bool`), a string of characters (`str`). Additionally, the values of these types can not be changed - at most, you can replace the current value of a variable with a new value.

``` python
some_text = "Example text"
some_text = "Completely new text"
some_text.upper()  # Creates "COMPLETELY NEW TEXT", but does *not* modify the original one
some_text = some_text.upper()  # The *created* text *replaces* the original
```

## Complex types

Complex types are those that consist of data with different values. You are already familiar with lists - you must know that, in practice, what matters is the data that is in the list, and the list itself is just a container used to organizing the code better.

### Lists

They are the right choice when you care about preserving the order of a certain set of elements (names, months, tax thresholds). Lists allow you to read, add and delete elements anywhere (indicated by a number - **index**). They also provide convenient ways to work with each element, one at a time.

Lists are the right choice when there is more data and their order is important.

### Set

This is a type of container that does not remember the order, nor does it remember duplicates. It only allows you to add an element to the set, check whether such an element is already in it, and remove it from the set. It doesn't allow you to read a single selected element, while, as with a list, it's possible to "visit" each element in turn - in the order decided by Python:

``` python
spammers = {'abubakar@nigerianprince.com', 'helpdesk@freeipads.com'}

print('helpdesk@freeipads.com' in spammers)  # True

print('stonks@dogecointothemoon.net' in spammers)  # False
spammers.add('stonks@dogecointothemoon.net')
print('stonks@dogecointothemoon.net' in spammers)  # True

for spammer in spammers:
    print('email:', spammer)
# email: abubakar@nigerianprince.com
# email: stonks@dogecointothemoon.net
# email:helpdesk@freeipads.com

spammers.remove('stonks@dogecointothemoon.net')
print('stonks@dogecointothemoon.net' in spammers)  # False
```

Sets are a suitable tool when you want to remember that some value has already occurred (e.g. a banknote number when you're looking for counterfeits, a PESEL number if you're checking whether someone has registered twice).

As you can see, to create a set, you need to specify its values separated by commas inside the curly brackets. Once the set exists, you can change its value using the method such as`.add(...)` and `.remove(...)`.

> **Note:**
> 
> To create an empty set, use `set()`. Empty curly brackets mean not an empty set, but an empty dictionary - we talk about it in the next paragraph.

### Dictionary

It is a container that allows certain values to be given arbitrary labels (keys). In this respect, it works quite like a dictionary of foreign words - that's why its called that:

``` python
pl_to_en = {
    'kot': 'cat',
    'pies': 'dog',
    'ptak': 'bird'
}
print(pl_to_en['kot'])  # cat

animal = 'pies'
print(pl_to_en[animal])  # dog

print('ptak' in pl_to_en)  # True
print('bird' in pl_to_en)  # False

print('ryba' in pl_to_en)  # False
```

Do we need dictionaries when variables also consist of a name and a value?

``` python
kot = 'cat'
print(kot)  # cat
```

Yes, because types such as dictionaries and lists allow you to create a complex data structure. The number and names of the variables must be known at the time of writing the program. In contrast, the subsequent elements of lists and the keys and values of dictionaries can appear during the execution of the program, as needed - based on the data being processed.

``` python
taxes = {
  'pl': [
    {'amount': 0, 'rate': 0.17},
    {'amount': 85528, 'rate': 0.32},
  ],
  'en': [
    {'amount': 0, 'rate': 0},
    {'amount': 12500, 'rate': 0.2},
    {'amount': 50000, 'rate': 0.4},
    {'amount': 150000, 'rate': 0.45},
  ]
}
```

## Summary

Complex data types are particularly important in the work of an analyst - thanks to them you can handle sets of data of any size and ensure that they have a meaningful structure. This will make working with datasets simple and convenient and allow you to quickly extract the information you need.
