# Connecting to the CodersLab database

Type: Article

## Data to connect with the database

To connect with the database used in the course you are going need the following:

1. **Host**: kurs-sql.coderslab.pl
2. **Port**: 8001
3. **Login**: received via email
4. **Password**: received via email

## Creating a new connection

Using `DataGrip` you can configure the new connection like this:

1. Click '+' near the upper left corner as shown in the image:

![step 0](/presentations/DTL/en/4.9/W/M_02_S_01/b000d210-04ad-428c-97c2-8c1b1f4ac13c/student_content/39b44bc8-067d-4f58-9646-aec5af44ed2d/./images/db_connection_01.png)

1. Next, select `MySQL` from the drop-down list (similar to the image below, but the location may be different):

![step 1](/presentations/DTL/en/4.9/W/M_02_S_01/b000d210-04ad-428c-97c2-8c1b1f4ac13c/student_content/39b44bc8-067d-4f58-9646-aec5af44ed2d/./images/db_connection_02.png)

1. Complete the fields marked in the image, according to the information given below:

![step 2](/presentations/DTL/en/4.9/W/M_02_S_01/b000d210-04ad-428c-97c2-8c1b1f4ac13c/student_content/39b44bc8-067d-4f58-9646-aec5af44ed2d/./images/db_connection_03.png)

> Each student has a dedicated database, so the connection data is different for everyone.
> You will receive connection parameters via email. If you didn't get them yet, please contact your mentor. In addition, we will need to modify the queries accordingly (see note *Starting SQL queries on the server*).

1. You can verify whether the connection is configured correctly by clicking the `Test connection` button. If so, a success message should appear:

![step 3](/presentations/DTL/en/4.9/W/M_02_S_01/b000d210-04ad-428c-97c2-8c1b1f4ac13c/student_content/39b44bc8-067d-4f58-9646-aec5af44ed2d/./images/db_connection_04.png)

## Executing SQL queries on the server

To send an SQL query to our server, first you need to create a new file with the `.sql` extension. To do this, you need to:

- From the top menu, select `File -> New -> SQL file`,
- enter the name of the file (we recommend keeping all the query files in one folder, and naming them to have a logical meaning),

After doing this, a new file should open, where we can type queries.

To run the saved queries, just click the green arrow button (it is located above the editor in which we write queries).
During the first attempt, DataGrip may ask which session to use to send the queries. Select the `New Session` option and next choose the connection to the Coders Lab database created earlier.

> **NOTE**
> 
> As mentioned earlier, each student has a dedicated database. This means that the queries that will appear in the materials have to be **modified**.
> 
> 
> 
> 
> For example, if the student login is `student1_2`, then **all** queries need to be appropriately modified:

from

`SELECT * FROM sakila.film`

to

`SELECT * FROM sakila1_2.film`.

Where, in this case:

- 1 - is the number of the course,
- 2 - number of the student.

## Summary

After following the steps from this article, we should not encounter any major problems with establishing a connection to our database and being able to send SQL queries to it. If this is not so, there's no time like the present. Write to your mentor now and ask for support, to solve the problem.
