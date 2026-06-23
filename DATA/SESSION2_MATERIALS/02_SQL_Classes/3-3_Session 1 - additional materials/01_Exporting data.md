# Exporting data

Type: Article

## Exporting data from the database

All the queries we have written so far, we displayed on the `DataGrip` screen and did not use any further. In practice, however, we need to pass on the data acquired through queries. We can cite the following situations as examples:

- as the result of an analysis report, the data from the database is written to a file and passed directly on to the end user,
- as the first stage of analysis to be continued later in another tool - typically `Excel`, (preferably) `Python` or `R`, where post-processing and visualization occurs,
- as data acquisition for modeling and simulation purposes,
- and many, many more.

Regardless of the purpose for which we write a query, the above examples have one part in common - **calling a query from the workspace**.

> Of course, you can also write the results of the query first to a `*.csv` file and then load it, but we will show the export to `csv` file only for `DataGrip`.

In this article, we will learn about export methods using:

- `Excel` sheet - because it is the most popular office tool,
- power query (also available in `Excel`),
- `Python` - using the `Pandas` library.

We are going to export the very simple query below, but of course it could be any other query as well:

``` 
SELECT * FROM sakila.actor
```

## Export from `DataGrip` to a csv file

1. We execute the query whose result we want to save,
2. When it finishes, in the bar between the query content and the result, you will see a download symbol as shown in the image below:
  ![DataGrip-Download](/presentations/DTL/en/4.9/W/M_03_S_03/7d5477d6-7d6c-497a-9075-088fa4b0d790/student_content/fd7da8b1-65fd-459e-af47-c3febf0d34b6/./images/datagrip-download-symbol.png)
3. When clicked, it will open a data export window:
  ![DataGrip-Form](/presentations/DTL/en/4.9/W/M_03_S_03/7d5477d6-7d6c-497a-9075-088fa4b0d790/student_content/fd7da8b1-65fd-459e-af47-c3febf0d34b6/./images/datagrip-download-form.png)

Here we have the following options:

- **Transpose** - swap rows with columns of the table,
- **Add Column Header** - decide to add column headers to the data,
- **Add Row header** - decide to add the row number,
- **Output file** - path to the file where the data is to be saved.

1. After saving the file in this manner, we can proceed as with any other csv file.

## Connecting to the database from within `Excel`.

> **Note:**
> 
> This method of linking is potentially not in compliance with security rules. Any connection to a DB should be removed from the file before sending it to a third party!

1. After opening the spreadsheet, we go to **Data** -> **Get Data** -> **From DataBase** -> select the DB we are working on: in our case - `MySQL` Database:
  ![Excel-Connection](/presentations/DTL/en/4.9/W/M_03_S_03/7d5477d6-7d6c-497a-9075-088fa4b0d790/student_content/fd7da8b1-65fd-459e-af47-c3febf0d34b6/./images/excel-connection.png)
2. The following window about connecting to the database should open. We are interested in the *Advanced options* section:
  ![Excel-Connection-Form](/presentations/DTL/en/4.9/W/M_03_S_03/7d5477d6-7d6c-497a-9075-088fa4b0d790/student_content/fd7da8b1-65fd-459e-af47-c3febf0d34b6/./images/excel-connection-form.png)

where:

- **Server** - IP of the server we want to connect to,
- **DataBase** - name of DB on the server,
- **Command timeout** - maximum time Excel should wait for the query to be completed,
- **SQL statement** - we specify the query to be executed and loaded into `Excel` (remember the limits of rows in the sheet, otherwise the results may be *cut*)

1. We will be asked to provide some more information:
  ![Excel-Connection-Form2](/presentations/DTL/en/4.9/W/M_03_S_03/7d5477d6-7d6c-497a-9075-088fa4b0d790/student_content/fd7da8b1-65fd-459e-af47-c3febf0d34b6/./images/excel-connection-form2.png)
2. If everything went fine, we will see such a screen along with a preview of the results:
  ![Excel-Query-Results](/presentations/DTL/en/4.9/W/M_03_S_03/7d5477d6-7d6c-497a-9075-088fa4b0d790/student_content/fd7da8b1-65fd-459e-af47-c3febf0d34b6/./images/excel-query-results.png)
3. Clicking *Load* will save the query to the sheet.
4. **Once we're done working on the file, in order to send it to a third party, we remove the connection from the sheet:**
  ![Excel-Query-Removal](/presentations/DTL/en/4.9/W/M_03_S_03/7d5477d6-7d6c-497a-9075-088fa4b0d790/student_content/fd7da8b1-65fd-459e-af47-c3febf0d34b6/./images/excel-connection-delete.png)

## `PowerQuery` (example based on Excel 365)

> `PowerQuery` has been introduced to Excel in version 2016. It has existed as an add-on since Excel 2010.

1. Open the `PowerQuery` editor window with **Data**->**Get Data**->**Launch Power Query Editor...**
  ![PowerQuery-Init](/presentations/DTL/en/4.9/W/M_03_S_03/7d5477d6-7d6c-497a-9075-088fa4b0d790/student_content/fd7da8b1-65fd-459e-af47-c3febf0d34b6/./images/power-query-init.png)
2. The editor window opens. To select the connection, we follow the steps according to the image below:
  ![PowerQuery-Connection](/presentations/DTL/en/4.9/W/M_03_S_03/7d5477d6-7d6c-497a-9075-088fa4b0d790/student_content/fd7da8b1-65fd-459e-af47-c3febf0d34b6/./images/power-query-connection.png)
3. We perform steps 2-6 in the same way as for `Excel`.

## `Python`

In the case of `Python` we have a lot of options at our disposal. In this article we will focus on `Pandas`.

> At `CodersLab` the `psycopg2` library which gives more freedom to configure and manipulate the results of a query,  is taught in more detail during the `Python - Data Analysis` course.

Assuming you have `Pandas` installed in your `Python` instance, we can reduce retrieving the data to configuring the following code accordingly (follow the comments):

``` 
# importing required libraries
import mysql.connector as sql
import pandas as pd

conn = sql.connect(
    host='****', # database IP
    database='**',  # DB name
    user='username',
    password='password'
    )

# Executing the query and loading as a DataFrame
df = pd.read_sql("SELECT * FROM sakila.actor", conn)
df.head()
```

> **Pro tip**
> Remember to check that you have the `pandas` and `mysql` libraries installed before running the code.
