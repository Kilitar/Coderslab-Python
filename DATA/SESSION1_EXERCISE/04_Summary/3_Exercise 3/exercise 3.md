# Exercise 3 discussion

Type: Article

## Instruction

In the`archive/` folder there are subfolders: `2018`, `2019` and `2020`, and inside each of them more subfolders with three-letter month-name abbreviations  (`jan`, `feb` etc.).

Each of these folders contains `.csv` files (one per day of the month) with information on the number of new, returning and VIP customers who visited the store that day.

Write a script to sum up how many new, returning and VIP customers visited the shop in 2018, 2019 and 2020.

Expected results:

``` 
In 2018 the shop was visited by:
 - 853 new customers
 - 2842 returning customers
 - 315 VIP customers
In 2019 the shop was visited by:
 - 851 new customers
 - 2859 returning customers
 - 252 VIP customers
In 2020 the shop was visited by:
 - 757 new customers
 - 2767 returning customers
 - 255 VIP customers
```

## Discussion

The exercise requires that we search for files: to do it we are going to use the `glob` module. All files are **csv** type, so to read them we are going to use the `csv` module.

``` python
import glob
import csv
```

### Finding files

The next step is to find the files we want to sum up. To do it we will write a `files_in_year(year)` function that returns the list of their paths:

The paths to the files have the structure:

``` 
archive/YEAR/MONTH/DAY.csv
```

So to find all the files in a given year, we will use:

``` python
glob.glob(f'archive/{year}/**/*.csv', recursive=True)
```

The entire function looks as follows:

``` python
def files_in_year(year):
    return glob.glob(f'archive/{year}/**/*.csv', recursive=True)
```

### Analyzing files

All files have the same structure:

``` 
New customers,100
Returning customers,200
VIP customers,300
```

This means that in each file we expect to find 3 rows, and two cells in each. Here, we are going to use the `reader` function from the `csv` module.

``` python
with open('path/to/the/file.csv', newline='') as my_file:
    report = csv.reader(my_file)
```

How to inquire about, for example, the second cell in the first row? It is possible to use the value returned by `reader` in a `for` loop, but it cannot be queried for a specific row. Luckily, anything that works with a `for` loop, can also work with the `list()` function: so let's convert `report` to a list.

``` python
with open('path/to/the/file.csv', newline='') as my_file:
    report = csv.reader(my_file)
    data = list(report)
```

Now the structure of the `data` variable is:

``` python
data = [
  ['New customers', '100'],
  ['Returning customers', '200'],
  ['VIP customers', '300']
]
```

To read how many VIP customers were in the store that day, use:

``` python
data[2][1]
```

It would also be good to convert this value to the `int` type: this will let us calculate the sum for the whole year:

``` python
int(data[2][1])
```

### Completed script

We have discussed the most important problems that need to be solved in order to generate an aggregate report. It's time to put all the pieces of the puzzle together.

You need to generate a summary for each year separately. To do this, we are going to write a `for` loop, that executes the code for `2018`, then `2019`, and later `2020`:

``` python
years = (2018, 2019, 2020)

for year in years:
    print('Making a report!')
```

Within each year (loop iteration), we need to look for all the files that apply to that year:

``` python
years = (2018, 2019, 2020)

for year in years:
    filenames = files_in_year(year)
```

Next, we are going to read each of them (probably when you see the word **each** you already expect that we are going to need the `for` loop) and add the values from them to the variables that count the clients from the full year: we also need to declare these variables.

``` python
years = (2018, 2019, 2020)

for year in years:
    filenames = files_in_year(year)

    new = 0
    old = 0
    vip = 0

    for filename in filenames:
        with open(filename, newline='') as my_file:
            report = csv.reader(my_file)
            data = list(report)
            new = new + int(data[0][1])
            old = old + int(data[1][1])
            vip = vip + int(data[2][1])
```

Take care where you create the `new`, `old` and `vip` variables: we only want them to zero out when we start reporting each year (*outer* `for` loop, on `years`), and not when we read each file (*inner*, on `filenames`).

When the loop iterating `filenames` finishes, we are ready to display the summary for one year: we need to do it in the *outer* `for` loop, to display it after each year.

``` python
...
for year in years:
    ...

    print(f'In {year} the shop was visited by:')
    print(f' - {new} new customers')
    print(f' - {old} returning customers')
    print(f' - {vip} VIP customers')
```

The entire script is:

``` python
import glob
import csv

def files_in_year(year):
    return glob.glob(f'archive/{year}/**/*.csv', recursive=True)

years = (2018, 2019, 2020)

for year in years:
    filenames = files_in_year(year)

    new = 0
    old = 0
    vip = 0

    for filename in filenames:
        with open(filename, newline='') as my_file:
            report = csv.reader(my_file)
            data = list(report)
            new = new + int(data[0][1])
            old = old + int(data[1][1])
            vip = vip + int(data[2][1])

    print(f'In {year} the shop was visited by:')
    print(f' - {new} new customers')
    print(f' - {old} returning customers')
    print(f' - {vip} VIP customers')
```
