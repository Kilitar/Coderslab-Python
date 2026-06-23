# Cleaning and processing data

Type: Article

## Introduction

Let's summarize what we've done so far - we've spent our time and energy defining the problem we need to solve.
We formulated additional questions that helped us better understand the task at hand.
We also learned how the data is stored and how to obtain data for our analysis.
Now that we're at this point, for sure you already have it on your computer.
So we can move on to the actual work with the data.

## Why do we clean and process data? - brief reminder

Cleaning and processing data is the third step of the Data Science process. The activities we're going to do are key to the next steps.
Let's review the aims of cleaning and processing data:

**- Better understanding of data definitions**

As we go through the data, we can take a closer look at the individual variables.
By seeing the names of the variables along with their values, we're able to better understand what they describe.
For example the column name: `neighbourhood_group` does not clearly explain what areas they describe.
On the other hand, if we look at the data that is stored in this column (e.g. Brooklyn, Queens), we know that we're dealing with boroughs of New York City.
With the use of filters, we can easily see what values are in the selected column.

**- Checking and improving data quality**

Working as a data analyst, you'll spend a lot of time doing data quality activities.
What does this mean? You may encounter missing or incorrect values in the data.
The `last_review` column may be an example of missing data.
As you can see, some rows have empty values, while others have a date entered. Let's investigate with a filter that chooses only the observations where `last_review` has no value.
What catches our eye?
The `last_review` column is empty only when the `number_of_reviews` column has the value of 0.
It seems logical, because since we have no opinions, it is impossible to determine the date of the last one.
However, sometimes it happens that variables are empty or, for example, have text values instead of numbers, and this happens as a result of an error, arising from a gap in data collection by, for example, an API.
The types of errors and how to deal with them will be discussed in detail during the first session.

**- Change of structure of data making the analysis easier**

It is not uncommon that we need to analyze a particular problem and we're given a set of raw, unprocessed source data.
In such a set, there can often be variables that, for example, we won't need during the analysis, and the best option is to remove them from the dataset.
This will make it easier to view the data on the screen (you'll have a constant view of only the relevant variables, without having to scroll).
The second reason for getting rid of unnecessary columns applies especially to large data sets.
Fewer columns means smaller data size, which will positively affect computational efficiency, since the tool we choose won't have to process superfluous data.
In addition to removing superfluous columns, we can also create new ones that can allow us to show the problem from a different perspective.
E.g., using the `price`, with room price per night we can create the column `price_level` with possible values of: "Cheap", "Normal" and "Expensive" based on the value of "price" which will enable offer aggregation based on price level.

## Example of cleaning and processing data

The theoretical introduction to cleaning and processing data is behind us; now it's time for practice. We open the file with data.

![Airbnb - data](/presentations/DTL/en/4.9/W/M_00_S_04/51eb931d-5b60-408c-957f-0ccf70cd08a0/student_content/d9b93215-1f42-4dfe-9c2e-904281110fb3/images/Airbnb_1.png)

Let's first deal with removing the columns that are irrelevant to the analysis of our problem. Let's remind ourselves what the goals are for our analysis:

- What is the average price for renting a room for one night?
- How many of the hosts have more than one listing on the site?
- How does the number of offers break down by type of room?.
- What is the number of units by district? For what reason do some neighborhoods offer more rentals?
- In which neighborhoods will the rent be highest?
- Are hosts more likely to rent rooms for short or long periods?

By looking at these questions, we're able to determine which data we will not need.
It may seem that the `longitude` and `latitude` columns aren't going to be necessary.
In our analysis, we will not create visualizations using a map.
The same is true of the "license" variable, which describes whether the landlord who offers the premises has a rental license (if required; in the US, each state has a different law).

![Airbnb - deleting columns](/presentations/DTL/en/4.9/W/M_00_S_04/51eb931d-5b60-408c-957f-0ccf70cd08a0/student_content/d9b93215-1f42-4dfe-9c2e-904281110fb3/images/Airbnb_2.png)

### Identifying the occurrence of empty values

We have cleared the data of unnecessary variables. The next step will be to look at whether there are observations in the set that have empty values in individual variables.
The easiest way to do this is to create a simple pivot table that will count the number of values in each column. We will put the table in a new sheet called `null_values`.

![Airbnb - pivot table with empty values](/presentations/DTL/en/4.9/W/M_00_S_04/51eb931d-5b60-408c-957f-0ccf70cd08a0/student_content/d9b93215-1f42-4dfe-9c2e-904281110fb3/images/Airbnb_3.png)

In the pivot table wizard, we drag a few (for now) selected column names that are in our dataset into the "Values" section.
We set Excel to perform a count for every variable.

![Airbnb - changing aggregation in pivot table](/presentations/DTL/en/4.9/W/M_00_S_04/51eb931d-5b60-408c-957f-0ccf70cd08a0/student_content/d9b93215-1f42-4dfe-9c2e-904281110fb3/images/Airbnb_4.png)

Let's take a look at the numerical values corresponding to the contents of each column.
We can notice that the number **39881** (the number of observations in our dataset) appears in most cases.
This means that the column in question has no blank values.
We can see that the values are less than 39881 for two columns: `name` and `host_name` and are - respectively: 39870 and 39831.
This means that we don't have the names of 11 listings and the names of hosts for 50 listings.
So let's go back to the source data and take a closer look at these observations.

To do it we will use filters available from the `Filter` icon.
Open the filter for the `name` variable, and check if we have the `(Blanks)` value on the list.
If we don't see such an item in the list, we can try to do some filtering of the data in this column, setting the rule so that the value in this column has to equal the space character.
But in our case we can see that some cells are `(Blanks)` and we can use the first method to display them.
This turned out to be a success.
Excel showed us 11 rows where the `name` column is not filled.
Nevertheless, we can get around this problem.
We will definitely have to count the number of listings by, for example, type of property, so we can't remove this data from the collection, but on the other hand, we have to count it. We can do it with the `id` column which is an identifier of the offer and has all data filled out.
Then we can fill out the `name` column with `Undefined` values.

![Airbnb - entering default values in the name column](/presentations/DTL/en/4.9/W/M_00_S_04/51eb931d-5b60-408c-957f-0ccf70cd08a0/student_content/d9b93215-1f42-4dfe-9c2e-904281110fb3/images/Airbnb_5.png)

We do the same for the name of the host: assign the `Undefined` value to the rows where it is empty.

![Airbnb - entering default value in host_name column](/presentations/DTL/en/4.9/W/M_00_S_04/51eb931d-5b60-408c-957f-0ccf70cd08a0/student_content/d9b93215-1f42-4dfe-9c2e-904281110fb3/images/Airbnb_6.png)

### Verify the types of data in each variable.

It looks like we're done with filling in the empty values.
Let's now verify that the individual columns have their data type set according to the values they store.
This is another important step in the context of data processing, because an inappropriate data type (for example, when numeric data is interpreted as text) will prevent mathematical operations in a column.
To change the type of data in a column, we click on the column header and select the appropriate type from the drop-down list in the "Home" tab, or use the cell formatting available by right-clicking on the selected column.
We will assign the `Number` type to numerical values, `Text` type to texts, `Short Date` to dates, and to the fields with prices – `Currency`.
It looks like now all our data has correct types assigned.

![Airbnb - data types](/presentations/DTL/en/4.9/W/M_00_S_04/51eb931d-5b60-408c-957f-0ccf70cd08a0/student_content/d9b93215-1f42-4dfe-9c2e-904281110fb3/images/Airbnb_7.png)

### Adding new variables to data

At the end of the data cleaning and processing, let's see if we can create any variables from our data that could potentially be useful to us and enrich our analysis.
Let's try adding a variable that will tell us whether a particular listing is for a short-term rental, a long-term rental or perhaps a medium-term rental.
Their values depend on the value of the `minimum_nights` variable, where 1 to 14 nights is short-term rent; 15 to 30 is mid-term, and above 30 nights - long term rent.
We call the variable `rental_duration` fill it with "Short-term", "Mid-term" and "Long-term" values. We are going to use the following IF function:

`=IF(I2  <= 14; "Short-term"; IF(I2 <= 30; "Mid-term"; "Long-term"))`

![Airbnb - adding new variable](/presentations/DTL/en/4.9/W/M_00_S_04/51eb931d-5b60-408c-957f-0ccf70cd08a0/student_content/d9b93215-1f42-4dfe-9c2e-904281110fb3/images/Airbnb_8.png)

After dragging the formula all the way to the end, we found that we had created another variable that could be useful in showing relationships in our data, such as the average price of a unit per night depending on the length of the lease.

## Summary

We went through a very important step of the data analysis process together - data cleaning and processing.
In our table, we identified redundant columns, empty values, as well as relevant data types.
In addition to this, we added a new variable that may be useful to us in the rest of the analysis.
However, this is not the end of the work.
You may have noticed that some things could have been done better.
We intentionally skipped part of the operation, because we want you to make the rest of the changes as part of practicing and consolidating the material.

### Good luck!
