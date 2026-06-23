# Loading data in Pandas

Type: Article

## DataFrame - introduction

DataFrame is one of the basic data structures in Pandas. In fact, it can be somewhat equated with a two-dimensional table known from SQL or spreadsheets.
However, due to its properties, DataFrame is closer to the tables known from databases, as each column has a specific type contained in it.

Before analyzing the structure of the DataFrame, we will introduce examples of how to load data into Pandas, so that later on the example of the dataset used, we can present methods for analyzing and processing data.

## Loading the data into the DataFrame

As we mentioned earlier, Pandas allows loading data from multiple sources. Notice that the names of all methods used to import data start from `read_*`. The most popular ones, which we are going to discuss in more detail are:

- `read_csv()` - reads data stored in csv (comma-separated file),
- `read_excel()` - reads data from Excel files,
- `read_sql()` - if we want to read data from a database.

Of course there are many more supported data formats. All of them can be reviewed in the [project documentation](https://pandas.pydata.org/pandas-docs/stable/reference/io.html).
It is important to know that regardless of the method we use the type of returned object will be `pandas.DataFrame`.

## read_csv

As we mentioned earlier, the `read_csv` method is used to read the data from a .csv  file into a DataFrame. Below is an example of loading a data file, we will use in our work:

``` python
import pandas as pd
df_raw = pd.read_csv(
                    '../01_Data/product_prices.csv', # path to the file with data (if we want to enter the name: filepath_or_buffer)
                    sep=';',  # column separator
                    decimal=','  # sign separating the whole and fractional parts of a number
)

df_raw.head() # display the first few rows and check if the data actually got loaded (the function itself will be discussed later)
```

.dataframe tbody tr th:only-of-type {vertical-align: middle;}
.dataframe thead th {text-align: right;}

|  | Name | Types of goods | Unit of measurement | group ID | Types of products | Value | Date |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | SUBCARPATHIA | NaN | zł | 2 | pork ham cooked - per 1kg | 21.37 | 2013-3 |
| 1 | ŁÓDŹ | NaN | zł | 4 | bread - per 1kg | NaN | 2018-2 |
| 2 | KUYAVIA-POMERANIA | NaN | zł | 2 | barley groats sausage - per 1kg | 3.55 | 2019-12 |
| 3 | LOWER SILESIA | NaN | zł | 2 | dressed chickens - per 1kg | 6.14 | 2019-2 |
| 4 | WARMIA-MASURIA | NaN | zł | 2 | Italian head cheese - per 1kg | 5.63 | 2002-3 |

> Make sure to list your local path to the file when copying. Otherwise you may get an error like `FileNotFoundError`.

Selected parameters:

- `filepath_or_buffer` - path to the file we want to load (by default this is the first argument so it is most commonly skipped),
- `separator` - column separator (',' by default), but due to the risk of having ',' in text content .csv use ';' as a separator,
- `encoding` - character encoding ('UTF-8' by default). If we don't know what kind of coding we're dealing with, it's worth using **Notepad++** - with its help we can check it easily,
- `decimal` - decimal separator in numbers; by default it is: '.' (dot), but some systems also use: ',' (comma),
  The world is divided in terms of the separator used, a list of countries and the separator used can be found [here](https://en.wikipedia.org/wiki/Decimal_separator).

All available information on this method can be found in [documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html).

## read_excel

It loads data from the **spreadsheet** and returns a data frame. Below is an analogous example for our dataset placed as a spreadsheet.

``` python
df_raw = pd.read_excel(
                        r'..\01_Data\product_prices.xlsx', # path to the file with data (if we want to enter the name: io=r'..\01_Data\product_prices.xlsx')
                        sheet_name='data' # the name of the sheet holding the data we want to process
)

df_raw.head() # display the first few rows and check if the data actually got loaded (the function itself will be discussed later)
```

.dataframe tbody tr th:only-of-type {vertical-align: middle;}
.dataframe thead th {text-align: right;}

|  | Name | Types of goods | Unit of measurement | id | Types of products | Value | Date |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | SUBCARPATHIA | NaN | zł | 2 | pork ham cooked - per 1kg | 21.37 | 2013-3 |
| 1 | ŁÓDŹ | NaN | zł | 4 | bread - per 1kg | NaN | 2018-2 |
| 2 | KUYAVIA-POMERANIA | NaN | zł | 2 | barley groats sausage - per 1kg | 3.55 | 2019-12 |
| 3 | LOWER SILESIA | NaN | zł | 2 | dressed chickens - per 1kg | 6.14 | 2019-2 |
| 4 | WARMIA-MASURIA | NaN | zł | 2 | Italian head cheese - per 1kg | 5.63 | 2002-3 |

> Make sure to list your local path to the file when copying. Otherwise you may get an error like `FileNotFoundError`.

- `io` - path to the worksheet file we want to load. Like in the case of `read_csv()` it is the first argument, so it is most often skipped. In Pandas version 1.2.1, the following file formats are supported: .xls, .xlsx, .xlsm, .xlsb, .odf, .ods and .odt,
- `sheet_name`- name of the sheet with data. Both the name of the sheet and its position (indexing from 0) can be passed.
  
  
  > Excel workbooks have three visibility modes: Visible, Hidden, but discoverable, and Very Hidden (hidden, but only visible from the VBA console). For this reason, it's better to reference by sheet name rather than by index, only to be surprised that it's not the workbook that has been read into the table.

You can find all available information on this method in the [documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html#pandas.read_excel).
