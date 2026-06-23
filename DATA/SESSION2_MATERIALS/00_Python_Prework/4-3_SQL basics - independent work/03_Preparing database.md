# Preparing database

Type: Article

During prework, we will use a database holding information about the school. This is a very simplified database created solely for the course. As a rule, databases have many more tables and hold much more information.

Take a look at the schema of this database:

![](/presentations/DTL/en/4.9/W/M_04_S_03/42c88f19-c227-437d-a0bd-dcdc3de961bc/student_content/b278224f-2319-414d-8288-5c6da49dc1fc/images/ex_rel_database.png)

## Importing database to our server

To use the data, we need to earlier upload it to the server. To do it we are going to need the `dump.sql` file. The file is in the LMS, packaged for download as a ZIP file.

After downloading the file, do the following:

1. Create a new database named School (creating databases was discussed earlier),
2. Open the `Query tool` window of the newly-created database,
3. Open the `dump.sql` file. We do this by clicking on the file load button: ![open file](/presentations/DTL/en/4.9/W/M_04_S_03/42c88f19-c227-437d-a0bd-dcdc3de961bc/student_content/b278224f-2319-414d-8288-5c6da49dc1fc/images/open_file.png) and we search our computer for the correct file.
4. Once the file is loaded (our editor should get filled with SQL queries), we run it by clicking the "Run" button. The result window should say: `Query returned successfully in XXX msec.`.

After importing the database it is worth checking if everything worked correctly. In our `Query tool` window, let's enter the query (remember to remove any earlier queries that might be there — best open a new `Query tool` window):

``` sql
SELECT * FROM Students;
```

In the results window we should see data about the students who are in the database.

## How to do the prework exercises?

During the prework you will have to write a dozen or so simple SQL queries. These queries should be saved in a single text file and sent to the mentor via Slack with information about completing this part of the prework.

Next to each SQL query, there should be an indication of which task it solves.
