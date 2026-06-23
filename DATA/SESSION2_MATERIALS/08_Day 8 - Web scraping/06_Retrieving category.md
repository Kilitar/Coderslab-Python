# Retrieving category

Type: Exercise

# Business context

At the address [click](https://prod-kurs.coderslab.pl/index.php) there is a CodersLab online store that sells a variety of accessories: tshirts, mugs, etc.

Take on the role of an analyst from a competing company who wants to compare their product line with the market. The analysis is focused on the content of the three product categories:

- clothes
- accessories
- art

At this time our job is mostly to get the information from the available websites.

## Exercise 1

Complete the implementation of the `get_categories_urls` function to use `requests` and `bs4` and retrieve the available categories of products (`clothes`, `accessories`, `art`) and return the urls leading to them with category names as a list of dictionaries.

### Example

``` python
categories_urls = get_categories_urls()
print(categories_urls)
```

Expected result:

``` 
[
    {
        "url": "https://mystore-testlab.coderslab.pl/index.php?id_category=3&controller=category",
        "name": "Clothes"
    },
    {
        "url": "https://mystore-testlab.coderslab.pl/index.php?id_category=6&controller=category",
        "name": "Accessories"
    },
    {
        "url": "https://mystore-testlab.coderslab.pl/index.php?id_category=9&controller=category",
        "name": "Art"
    }
]
```

> The order of elements can be anything

### Hints

- use your browsers DevTools to find the top panel with names of categories,
- find the panel using its `id`,
- it may be useful to use the `data-depth` attribute to find the link in `a` tag,
- to get the category name you need to remove the string: `'\ue313\n\ue316\n\n\n'` from the text.
