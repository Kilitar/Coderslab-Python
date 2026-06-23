# Installing required libraries

Type: Article

For web scraping, we need a library to provide us with data and a library to extract the necessary information from this data.

We are going to use the `requests` library to retrieve data, and parse it with the `beautifulsoup4` library.

In addition to this, to extract data from some pages we will need a whole browser, which we will control from Python. To control the browser we will need:

- `Selenium` library
- a browser: **Firefox** or **Chrome**
- a driver for the browser we chose:
  
  - [This is where the driver for Firefox is](https://github.com/mozilla/geckodriver/releases)
  - [This is where the driver for Chrome is](https://chromedriver.chromium.org/downloads)
  - drivers for other browsers are available, but for the duration of the course, choose one of the ones listed above.

Choose one of the drivers that will suit your browser and system. We are only going to need one file from the archive: `geckodriver`, `geckodriver.exe`, `chromedriver` or `chromedriver.exe` – depending on which driver you want to use.

The file has to be placed in one of the directories in the `PATH` variable of your system (type `echo $PATH` in MacOS or Linux console, or `echo %PATH%` in Windows) or in the same directory as the script that uses it (during classes we are going to use the second option).
