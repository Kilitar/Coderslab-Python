# Introduction

Type: Article

## What is Pandas?

![Pandas Logo](/presentations/DTL/en/4.9/W/M_05_S_08/38c87fba-ab61-4418-b1c2-f1ca2279e1da/student_content/792279f7-0a41-44dc-b512-b6d16911faff/images/pandas.svg)
In a nutshell, it can be said that Pandas is an open-source library that provides powerful, easy-to-use data structures to perform analysis using Python.
The library was first released in 2008, and its name is based on [panel data](https://en.wikipedia.org/wiki/Panel_data) – **pan**el **da**ta.

Pandas is mainly used for analysis or data processing, additionally it allows importing data from various sources such as Excel, SQL or text files (e.g. .csv). So using a single package, it is possible to integrate, process and then analyze data from different sources.

You can find full library documentation at the [link](https://pandas.pydata.org/pandas-docs/stable/reference/index.html).

## Pandas vs Excel

`Excel` is currently one of the most popular tools for reporting and communicating data. The simplicity of introducing *manual* corrections to data and the ability to quickly manipulate individual elements of the sheet, made Excel not only synonymous with spreadsheet software but also used as a basis for building supporting tools for everyday work. (e.g. using `VBA`).

Nevertheless,`Excel` and its versatility bring their own, quite important limitations:

- the number of rows is limited (as of version 2007 it is 1,048,576),
- the speed of operation leaves much to be desired (especially if you work on *larger* data sets - more than 20-30 thousand rows),
- building more advanced functions requires either writing clumsy, long formulas or using (also not very friendly and fast) VBA code,
- versioning the file is cumbersome,
- automating data processing is more difficult to both implement and hand over.

`Pandas` is free from such limitations, data operations are significantly faster, and the amount of data that can be processed is considerably greater (it also depends on the memory available in our machine). What's more, the code can be easily versioned and distributed to others, and if well organized and properly annotated, it can be easily passed on to another person.

## ETL with Pandas

ETL is a general name for how data is processed. It is an abbreviation for the following process:

1. **E**xtract - that is, taking data from a source, in this case we can understand the source as a website, an external database, a text file or spreadsheet or other anything else we need to take data from,
2. **T**ransform - is the processing of the extracted data in such a way that it meets the technical or business requirements in our system. It could be, for example, aggregation, filtering, deletion of data, merging with other sources or any other operation that modifies the input data.
3. **L**oad - this is the loading of data into our system after transformation - usually a database / data warehouse.

In this context, Pandas works perfectly, because it has an implementation of all the above methods, as long as the input data is in tabular form.
Methods of extracting (loading) data for future processing start with *read_**,, while methods for exporting have the prefix to_*_.

![image](/presentations/DTL/en/4.9/W/M_05_S_08/38c87fba-ab61-4418-b1c2-f1ca2279e1da/student_content/792279f7-0a41-44dc-b512-b6d16911faff/images/file_types.png)

## Pandas in data analysis

`Pandas` is a very convenient tool for data analysis. In addition to the data processing methods, the following functions are also available:

- calculation of all basic descriptive statistics such as *mean* and *median*,
- ability to determine other, even our own, custom statistics (using our own functions),
- creation of charts such as bar chart, line chart, box chart and many others,
- grouping and analysis of data subsets (`groupby()`),
- time series analysis,
- methods facilitating work with missing data (e.g. `dropna()`, `isnull()`),
- construction of pivot tables (similar in their idea to those known from spreadsheets).

* actually `Pandas` uses `Matplotlib` library, but it considerably helps with building charts. The topic of creating charts will be discussed in detail at a session devoted to them.

## Installation

By default, with the installation of `Anaconda`, `Pandas` should already be installed. However, if we wanted to install it manually in `Jupyter Notebook`, the command below is enough:

``` 
!pip install pandas
```

This command installs the latest versions of the library. During classes we are going to use `pandas` version 1.4.2. To make sure that we have the same version, we can use the following command to check the version of the library:

``` python
!pip show pandas
```

If it turns out that we have a lower version, e.g. 1.3.* (newer versions shouldn't cause any problems), then we can additionally execute the following commands on the command line:

``` python
!pip install --upgrade --force-reinstall pandas==1.4.2
```

### `openpyxl` library

During the session we will be discussing also the `openpyxl`, library for manipulating spreadsheet files. It also comes by default with the `Anaconda` package. However, if we want to install it manually, then we need to call the command in Jupyter Notebook:

``` 
!pip install openpyxl==3.0.9
```
