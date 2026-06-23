# Data prepared for classes

Type: Article

# Dataset presentation

When we learn Pandas we are going to use the translation of a dataset sourced from the [Statistics Poland local data bank](https://bdl.stat.gov.pl/BDL/start?lang=en).
Using the example of quarterly average prices of selected food products in Poland (by province), we will perform basic data processing. As a business and technical background, we will assume that the data is to be used later to make a forecast for the next two years.

The dataset is composed of the following groups of food products:

- preserves,
- fats and dairy,
- meat products,
- other.

The dataset has more than 140,000 rows and 7 columns.

The full data set is available in the class materials.

> There are two files in the materials: *product_prices.csv* and *product_prices_renamed.csv*, which differ only in the naming of the columns.

## Column descriptions

1. **Name/province** - the province from which the data comes (including Poland),
2. **Commodity types/product_types** - type of products,
3. **Unit of measure/currency** - currency in which prices are presented,
4. **Group ID/product_group_id** - product group id,
5. **Product types/product_line** - supplement to the *Commodity types* column, as the source data has a different naming convention,
6. **Value/value** - price per commodity,
7. **Date/date** - average monthly price per commodity.

## Additional comment

The dataset used in the course comes from the Statistical Office of Poland, but the following modifications were made for lecture and exercise purposes:

- price data for February-December were generated randomly,
- additional modifications were carried out, creating errors or inaccuracies in the data,
- the true values are from January of a given year (we assume that the annual values are not an average, but a value from the beginning of the year).

The source data used to generate the output dataset is located in the *raw* folder.
