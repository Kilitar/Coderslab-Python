# Retrieving list of products

Type: Exercise

## Exercise 2

Complete the implementation of `download_category_items` function that takes category `url` as a parameter and returns a list of products from it.

> To make things easier, focus only on getting the results from the first page. This means that you don't need to iterate the pages and find how many pages there are.

### Example

``` python
url = 'https://mystore-testlab.coderslab.pl/index.php?id_category=3&controller=category'
products = download_category_items(url)

print(products)
```

Result:

``` python
[
    "https://mystore-testlab.coderslab.pl/index.php?id_product=1&id_product_attribute=1&rewrite=hummingbird-printed-t-shirt&controller=product#/1-size-s/8-color-white",
    "https://mystore-testlab.coderslab.pl/index.php?id_product=2&id_product_attribute=9&rewrite=brown-bear-printed-sweater&controller=product#/1-size-s",
    ...
]
```

### Hint

- Try to go to the page of any product and find its address in the page content - remember that you can find panels by their id.
