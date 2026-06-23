# Data generation

Type: Exercise

## Exercise 4

Using the solutions from the previous exercises, write a script that retrieves the data from all categories and saves it into a csv file named `coderslab-shop-data.csv`.

The file should be a table with the following headings:

``` 
name | price | description_short | qty | category
```

Set `|` as the column separator

### Hint

- if you want to track the progress of retrieving category data you can use the `tqdm` library (not discussed in class - [click](https://pypi.org/project/tqdm/)),
- change the default file encoding to write the currency symbol correctly (unless it has been removed earlier),
- it may be useful to set the appropriate new line character when opening the file.
