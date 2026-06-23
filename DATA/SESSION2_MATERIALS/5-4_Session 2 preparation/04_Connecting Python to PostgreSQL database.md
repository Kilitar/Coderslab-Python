# Connecting Python to PostgreSQL database

Type: Article

In this article you are going to learn how to use Python to connect to a PostgreSQL database and retrieve data from it with `SELECT` queries.
That’s what the `psycopg2` library is for. From this article you will learn how to install it before classes.

## Install psycopg2 library using conda package manager.

To install the `psycopg2` library we must start the Anaconda Navigator application. Next:

1. Open the "Environments" tab on the left,
2. Select our environment. It is usually called base,
3. From the selectable list choose `Not installed` (you may need to update indexes before — just click the "Update index..." button),
4. In the searchbox type: `psycopg2`,
5. Choose the library you're interested in from the list. Select it.
6. Click the Apply button.
7. The installation usually takes a moment.

If you get the `UnsatisfableError` during the installation follow the steps:

1. Open the "Anaconda Navigator" program,
2. Select the Environments tab.
3. Create a new environment,
4. Give it an appropriate name and set the python version to 3.6,
5. Install the library on the new environment according to the previously described steps.

## Installing the psycopg2-binary library manually.

If the installation with the package manager has failed, there is always the possibility to install this library manually. Its installation, however, is so complex and troublesome (it requires many libraries installed in the operating system and a compiler), that there also is `psycopg2-binary` - a ready, precompiled version of the library - we recommend installing it instead.

To install it, in Jupyter call the command:

``` 
!pip install psycopg2-binary
```

## Using the `psycopg2` module

The `psycopg2` module's most important component is the `connect` function - this is where we are going to start:

``` python
import psycopg2

connection = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='postgres',
    dbname='classicmodels',
)
```

Of course, in the example above, the password that was created during the database installation should be entered.

Now the `connection` variable should have the object representing the connection to the database. However, the query is not executed directly on the connection, but on the cursor - the connection has a method that such a cursor will return to us:

``` python
cursor = connection.cursor()
```

The object representing the cursor has several methods that are relevant to us:

- `execute(SQL query)` - sends a query to the database,
- `fetchone()` - returns the single, next row matching the query result; it throws an exception when there are no more rows to fetch,
- `fetchall()` - returns a list of tuples: all rows that matched the query

Of course, the `fetchone()` and `fetchall()` methods can only work if the `execute(...)`method with the query that returns the data was used earlier.

In addition, the cursor object can be iterated over - it then returns the found rows one by one:

``` python
cursor.execute('SELECT * FROM customers LIMIT 3')

for row in cursor:
    print(f'{row[1]}, telephone: {row[4]}')
```

Result:

``` 
Atelier graphique, telephone: 440.32.2555
Signal Gift Stores, telephone: 7025551838
Land of Toys Co. telephone: 2125557818
```

## Summary

The basics of using `psycopg2` to send queries and receive data are very simple; what's complex are the SQL queries that you can execute with it. This article explains how to execute `SELECT` queries, during classes with the lecturer, you are going to learn how to execute other ones.
