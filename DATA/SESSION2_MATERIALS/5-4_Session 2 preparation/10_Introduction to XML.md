# Introduction to XML

Type: Article

`XML` data format has the same goal as the `JSON` you learned about earlier, but creating its internal structure requires more work. This is the main reason behind the declining popularity of `XML`; it is, however, still used and that is why it is good to know it.

In this article we will talk about the basics of `XML`. How to read it and how to understand it. More of it will be mentioned in the course.

## What is XML?

The simplest `XML` looks like this:

``` xml
<?xml version="1.0" encoding="UTF-8"?>
```

The example above specifies the `XML` version and character encoding, but there is no data. To add some data, we have to do it using so-called xml tags (tags). Between the tags there is a value. We can treat a tag like a key in `JSON`:

``` xml
<key>value</key>
```

It will be best if we build our `XML` on the basis of the `JSON` from the previous article, which looked like this:

JSON file:

``` json
{
    "firstname": "John",
    "lastname": "Smith",
    "age": 18,
    "status": true
}
```

Analogous XML file

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<firstname>John</firstname>
<lastname>Smith</lastname>
<age>18</age>
<status>true</status>
```

Similarly, `XML` can be nested:

JSON file:

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

Analogous XML file

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<firstname>John</firstname>
<lastname>Smith</lastname>
<age>18</age>
<status>true</status>
<address>
    <city>Austin</city>
    <state>TX</state>
    <street>Nowhere</street>
</address>
```

Let's add a list. A list in `XML` is a single tag containing more than one identical tag. In this case, the *cars* tag contains three *car* tags, creating a list of cars:

JSON file:

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

Analogous XML file

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<firstname>John</firstname>
<lastname>Smith</lastname>
<age>18</age>
<status>true</status>
<address>
    <city>Austin</city>
    <state>TX</state>
    <street>Nowhere</street>
</address>
<cars>
    <car>ford</car>
    <car>honda</car>
    <car>fiat</car>
</cars>
```

---

## Summary

After reading this article you can recognize and understand data formatted as `XML`. This is also an excellent starting point to learn more.
