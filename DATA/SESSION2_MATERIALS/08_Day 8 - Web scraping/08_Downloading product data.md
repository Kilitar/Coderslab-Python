# Downloading product data

Type: Exercise

## Exercise 3

Complete the implementation of the `download_product_data(product_url)` function that takes `product_url` of the product and returns a dictionary of the data with the following information:

- `price` and currency symbol,
- `name`,
- quantity (`qty`)
- short description (`description_short`)

### Example

``` python
product_url = 'https://mystore-testlab.coderslab.pl/index.php?id_product=1&id_product_attribute=1&rewrite=hummingbird-printed-t-shirt&controller=product#/1-size-s/8-color-white'

download_item_data(product_url)
```

Result:

``` python
{'name': 'Hummingbird printed t-shirt',
 'price': '€19.12',
 'description_short': 'Regular fit, round neckline, short sleeves. Made of extra long staple pima cotton.',
 'qty': '999970'}
```

### Hints

- if you don't find an attribute for the product quantity, assume that its value is 0
- remember to handle the exception when there is no expected tag in the document
