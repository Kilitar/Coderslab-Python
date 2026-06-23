# Introduction to JSON

Type: Article

In this article you will learn a few things about data format called `JSON`. This is the absolute standard for exchanging data between information systems. And so
it is the standard used on the internet and it is absolutely necessary to know it.

## What is JSON?

`JSON` is a lightweight data exchange format. What it means is that a data object created on one system
can be easily read on another.

For us that means that a remote server we'll be connecting to will serve us data formatted as `JSON`.

`JSON` stands for `JavaScript Object Notation`. Admittedly, JavaScript appears in the name itself, but it is a type of
data structure available in most programming languages.

There are also .json files. These files store objects that are compatible with the `JSON` format.

The simplest `JSON` object is a closed pair of curly brackets:

``` json
{}
```

Putting data in this object consists in adding key-value pairs, separated by commas:

``` json
{
    "firstname": "John",
    "lastname": "Smith",
    "age": 18,
    "status": true
}
```

The value can also be another `JSON` object (*address* key in the example below):

``` json
{
    "firstname": "John",
    "lastname": "Smith",
    "age": 18,
    "status": true,
    "address": {
        "city": "Austin",
        "state": "TX",
        "street": "Nowhere"
    }
}
```

A list known from Python (cars) can also be entered as a value:

``` json
{
    "firstname": "John",
    "lastname": "Smith",
    "age": 18,
    "status": true,
    "address": {
        "city": "Austin",
        "state": "TX",
        "street": "Nowhere"
    },
    "cars": [
        "ford",
        "honda",
        "fiat"
    ]
}
```

This is the whole `JSON` format. Using only these basics, you can create structures with an enormous level of complexity.

---

## JSON and Python

One thing that's obvious from the start, is that in principle `JSON` is the same as a dictionary in `Python`.

In `Python`, `JSON` is represented as a `string` and can easily be converted to a
dictionary. And a dictionary - to `JSON`. `JSON` is a string because the data we receive from or send to a server has to be a string.

`JSON` is handled by the `json` module. This module is available in Python standard library
And all you have to do is import it:

``` python
import json
```

To convert Python's dictionary to `JSON` we need to use the `dumps` function:

``` python
import json

s = {
    "author": "Stephen King",
    "title": "The Gunslinger",
    "is_ok": True
}

j = json.dumps(s)
print(j)
```

In the example above `s` is a Python dictionary and `j` is `JSON`. The result of executing this program is what print will write out, that is:

``` 
{"author": "Stephen King", "title": "The Gunslinger", "is_ok": true}
```

Note the `true`value. As you remember, in Python, logical values `true` and `false`
are capitalized (`True` and `False`). And so in the dictionary it is `True`, and in `JSON` - `true`.

To convert `JSON` into a dictionary, simply use the `loads` function:

``` python
import json

j = '{"author": "Stephen King", "title": "The Gunslinger", "is_ok": true}'
s = json.loads(j)
print(s)
```

The result of the program is a dictionary:

``` 
{"author": "Stephen King", "title": "The Gunslinger", "is_ok": true}' True}
```

## Summary

In this article you learned the basics of `JSON`.
We should remember that:

1. `JSON` can be written to a file.
2. It is practically the same as a dictionary in Python (except for the logical values true/false).
3. It is a universal format for exchanging data between different computer systems.
