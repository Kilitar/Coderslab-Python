# Introduction to workshop

Type: Article

# Introduction

We are approaching the final element of the "Python - Data Analysis" module: the workshop. We will take on the role of an analyst in a newly established online bookmaker site. Our task is to obtain hockey league results from publicly available sources and then determine initial betting odds, which will be updated as new data comes in.

To structure the work on the project, we divided it into the following stages:

- **Data Download** - in this step, we will download data from the [Scrape This Site](https://www.scrapethissite.com/pages/forms/) website (notebook `01_DataDownload`),
- **Data Processing** - we will parse HTML pages and prepare the data for analysis (notebook `02_DataProcessing`),
- **Data Analysis** - we will conduct exploratory data analysis to familiarize ourselves with its characteristics (notebook `03_DataAnalysis`),
- **Recommendations** - we will formulate initial betting odds and discuss possible ways to further improve our process (notebook `04_BusinessRecommendations`).

# Required Libraries

During this workshop, we will mainly work with the following libraries:

1. **Selenium** - to download information about currently existing games results,
2. **BeautifulSoup** - to process unstructured data (HTML code) into tabular data (DataSet),
3. **Pandas** - to perform data transformations,
4. **Matplotlib** - to present results.

## What to review before the Workshop

The workshop will build on knowledge from the entire course. However, some things are worth reviewing. These include:

- Downloading page code using Selenium and saving this code to a file.
- Reading the saved file from the disk.
- Searching folders (the glob module covered during Python classes).
- Iterating over data structures (lists, dictionaries, etc.).
- Finding elements in the page code using BeautifulSoup.

# Project Structure

To facilitate work during the workshop, we will adopt certain assumptions about the project structure. Working with the same structure will avoid additional work when sharing the solution.

## data

This folder will contain all the data you generate during the task.

### data/raw (source data)

Here we will place raw `.html` files downloaded from the site. These will be unprocessed files, with no additional handling - in other words, a clean copy of the HTML.

> Aside from the project context, source files often come in the form of Excel files that are easy to manually modify. Best practice suggests that source files should be non-editable; that is, all changes should be in scripts to later replicate the work.

### data/interim (temporary data)

Here we will place the result of parsing data from the **raw** folder into a `json` list. Only data from this folder will be forwarded for further processing/transformation.

### data/processed (output data)

This folder will contain output data - cleaned, ready for further analysis. In the context of the workshop, we will base our conclusions and recommendations on this data.

## drivers

Required drivers for using Selenium

## notebooks

Here we will place all the notebooks created during the workshop. Their naming should follow the format -.ipynb, so that the order of steps will be known when trying to recreate the workshop.

## venv (optional)

A folder containing a virtual Python environment with only the packages needed for it to work correctly. Instructions for creating this are additionally described in the materials after the session.

## Additional Comment

The presented structure is called cookiecutter for Data Science, but to avoid additional confusion, it has been simplified for workshop purposes. More information about this approach can be found [here](https://cookiecutter-data-science.drivendata.org/).

# Task Structure

After reading this document, download the zip file available on LMS. Start your work with the notebook "01_DataDownload.ipynb". It describes the process step by step on how to approach and solve this workshop.

### Note

This task only simulates and presents an example process of how to approach such a formulated problem.
