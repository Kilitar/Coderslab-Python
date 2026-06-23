# Exploring data

Type: Article

## Introduction

Moving on to data exploration, we usually already know what kind of data we have, and we already have basic data quality issues resolved, such as obvious errors and omissions resulting from, for example, combining datasets or errors during data collection.
Now we're going to learn how to use various transformations and data visualizations to further discover and explore the data in a systematic way.

This will continue to be an iterative process that, in a nutshell, consists of 3 steps:

1. Formulating questions about our data,
2. Seeking answers to these questions through visualizations, transformations and data modeling,
3. Using the new knowledge to refine previously posed questions or formulate entirely new questions.

Exploratory analysis is not a process with strictly defined steps and rules.
It is a state in which we will combine curiosity and imagination with systematic testing and verification of our ideas and hypotheses.
We will be like a detective who methodically verifies the traces and clues that lead to the solution of a mystery.
Some of our ideas may be dead ends, others will turn out to be interesting and lead us further in the analysis process.
Continuing the analysis, over time we'll identify some particularly interesting observations and productive clues worthy of special attention.
It is then worth writing them down and communicating them to stakeholders.
Exploratory analysis is an important part of the data analysis process.
Even if we have received research questions in advance from those ordering the analysis, we must always check the quality of our data.
In fact, data cleaning is one part of exploratory analysis.
We should always ask ourselves: does my data meet expectations for data quality?
If not, we run the risk that our analysis will have a lot to do with the popular statement:

`Garbage in, garbage out`

Therefore, we may also find ourselves frequently returning to the data cleaning stage during the exploratory analysis.

## Airbnb - we are conducting an exploratory analysis

Exploratory analysis is certainly a very interesting part of the data analysis process, because at this point we look at the data to find relationships between variables and answers to the questions we have posed.
Of course, while exploring the data, we may notice other interesting phenomena that will be worth communicating to the audience.
Before we look at each variable individually, we need to briefly discuss how we generally divide variables by their nature:

- quantitative
  
  - continuous (variables that are measured and can take on almost any numerical value, such as length, height or temperature)
  - discrete (variables that are counted and have a finite number of values, such as the number of products in a shipment, the number of reviews)
- qualitative
  
  - nominal (variables whose values have no specific order or ranking, such as gender or race)
  - ordinal (variables whose values have a specific order, such as blood type or level of education)
  - binary (variables that have only two values, such as yes/no)

How we'll analyze each variable is determined by its nature.

For quantitative variables, we'll count basic statistics, that is, we will determine the minimum value, maximum value, as well as the mean or median. We will do the calculation for variables including: `price`, `minimum_nights` or `number_of_reviews`.

For qualitative variables, we will not count statistics, but we will determine the number of unique values, and we will be able to determine how many observations (property listings) we can attribute to a particular value - in other words, we'll answer, for example, the question "In which district is there the highest number of listings?" or "How many private rooms are offered on Airbnb?".

Let's also recall the questions we need to answer during our analysis.

- How does the number of offers break down by type of room?.
- Is there a noticeable difference in activity from one district/neighborhood to another, and what could be the reason for any differences?
- What is the average price for a room according to its type?
- In which neighborhoods will the rent be highest?
- Are hosts more likely to rent rooms for short or long periods?
- How many of the hosts have more than one listing on the site?

## Quantitative variables

In the file let's create a new sheet called `EDA` (exploratory data analysis), where we're going to create a table with the names of columns of quantitative variables and names of statistical measures we want to calculate, in the rows.
To calculate statistics for a selected range of data we'll use the function:

- MIN(range), to determine the minimum value
- MAX(range), to determine the maximum value
- AVERAGE(range), to determine the average value
- MEDIAN(range), to determine the median (the middle value of the considered range of values)

When calculating statistical measures for data that are in another sheet, we need to refer to its name when declaring the range.

![Airbnb - statistics](/presentations/DTL/en/4.9/W/M_00_S_04/a44296d1-15f7-4aff-88db-27065be8ae17/student_content/48e3bebe-6368-4576-9117-b009bcb9ba13/images/Airbnb_9.png)

OK, let's take a closer look at the calculated values:

### Exploring the `price` variable

The minimum room price per night is  0 USD.
From this we can see that some premises are provided for free (?), the host made a mistake when completing the parameters of the offer, or the data is wrong.
We can check the latter ourselves, so let's go to the source data.
After opening the filter on the `price` column, we can see the -" USD" value that in our case is wrong and that Excel qualified as 0 when setting the minimum value.
Let's think about what we can do so that we don't lose other information about these listings, and on the other hand don't distort reality.
In these places we can enter the average price calculated in our table, which is  198 USD.
The maximum value of the price is  16500 USD (for one night!), which means that among the listings on Airbnb we can deal with the most luxurious apartments in Manhattan.
The average price per night is  198 USD, and the median price is  130 USD.
This means that among our listings, 50% of them are cheaper than  130 USD, and the remaining 50% of listings are for units more expensive than  130 USD/night.
Taking into account the relationship between the median and the average, we can confidently conclude that the average is inflated by the presence of edge values (in other words: outliers), that is, in our case, the offers of rental units for the richest customers.
Let's use the `price` column filter again and set the condition so that Excel only return the offers above the average price.

![Airbnb - filtering by price](/presentations/DTL/en/4.9/W/M_00_S_04/a44296d1-15f7-4aff-88db-27065be8ae17/student_content/48e3bebe-6368-4576-9117-b009bcb9ba13/images/Airbnb_28.png)

After filtering, we see that we have 11917 such offers out of 39881 total offers.
This means that even less than 30% of the offers are more expensive than the average price. At first glance, we don't see outlier offers here.
Let's modify the filtering condition and set it so that we only see offers with the price greater than  1000 USD.
At this point, the list of bids has been narrowed significantly, as only 1.1% of all bids are now visible in the listing.
Looking through the listings, we see offers with really high prices, such as  9900 USD or the aforementioned offer with a price of  16500 USD.
As we predicted, both offers are for rental units located in Manhattan's Harlem district.
Scrolling through the list from top to bottom, we're able to see that the vast majority of the listings with a price of min.  1000 USD are specifically for Manhattan.
We have analyzed the `price` variable quite thoroughly and in doing so, answered one of the product owner's questions:

**"What is the average price for a property according to its type? "**.

We already know that it is ** 198 USD** .

### Exploring the `minimum_nights` variable

Among all listings, the minimum number of nights for which you can rent a room is 1.
This means that among the listings on Airbnb in New York there are units for tourists who are in the city only in passing.
On the other hand, the maximum value is as much as 1250 nights!
This means that there is a listing (or listings) in which a tenant can rent a unit, but on the condition that they declare for a minimum of 1250 nights.
So let's check all the offers in the data where the value of this variable is a minimum of 365.
We see that only 25 listings have a condition set for a minimum rental length of more than a year.
Reviewing these offers, we see an offer with a minimum number of nights of 1250 nights (~3.5 years).
The offer is for a unit in Manhattan with a price of  180 USD per night.
This means that if the landlord finds a client who meets the minimum number of nights of 1250, they will earn  225000 USD for the entire lease for almost 3.5 years.
OK, we checked the offers with high values of the minimum number of nights.
The average number of this variable is 19, and the median is 14.
As with price, we have a relationship of mean > median, which means that among our listings, more than half of them have a condition for a minimum rental duration of 19 days.

### Exploring the `number_of_reviews` variable

The number of reviews on each listing also has a considerable spread.
The minimum number is 0, which means that there are offers in our collection that have no reviews posted by users.
On the other hand, there are also offers that have quite a few, and the offer with the highest number of them has as many as 1480.
On average, each offer has 27 reviews, and 50% of offers have less than 5 reviews.
From this we can see that in our collection, most of the offers have collected fewer reviews than the average.
Let's check this in the source data. Let's set a filter on the `number_of_reviews` column with the value of our average.
We can see that Excel returned 9468 offers, which corresponds to 23.74% of all offers.
Just as we thought, this means that most of our listings have less than 27 reviews, so the average is heavily inflated by listings that:

- Have a large number of short-term rentals, so potentially more users can leave a review.
- Have been published on Airbnb for a long time (we don't know this because we don't know the date the listing was added), but we can assume so.
  This is potentially data that we could request from the people in charge of data collection mechanisms from various databases and applications (e.g., data engineers) if it were relevant to our analysis.
- The reviews are duplicated (added several times each by the same user) or added by bots.

We don't have such knowledge either, because we don't have access to qualitative data (such as offer text and user IDs).

Your task will be to analyze the other quantitative variables in a similar way, i.e. by calculating the indicated statistics and reviewing the source data to be able to better understand and interpret them.

## Qualitative variables

Now let's look at the qualitative variables in our data, such as: `host_id`, `neighbourhood` or `room_type`.

What we would like to examine at the beginning is how many unique values are in the selected column. Now the question is, how can we do this?

In Excel 365 we can just use the `UNIQUE` function, that returns the list of distinct values.
Next we pass its result to the `COUNTA` function, that counts all non-empty values.

![Airbnb - counting unique values](/presentations/DTL/en/4.9/W/M_00_S_04/a44296d1-15f7-4aff-88db-27065be8ae17/student_content/48e3bebe-6368-4576-9117-b009bcb9ba13/images/Airbnb_10.png)

We see that we have 26292 hosts, 244 districts and 4 types of rooms.

As you may remember, our task is to answer the questions we were asked.
Using the analysis of the `neighbourhood` or `room_type` variables, we will be able to answer some of them.

To do so we're going to use the pivot table function. In order to keep the sheets clear, let's create a new sheet that we'll call `EDA_pivot_tables`.

### Exploring the `neighbourhood` variable

In our table in the "Values" field let's put the `price` label, and in "Rows" let's drop the `neighbourhood` label.
We are shown a two-column table that counts the listings by New York City neighborhoods.
As for the variable storing the price, we need to set the appropriate aggregation type.

We want to answer the question:

- In which neighborhood will the rent be highest?

Therefore, we need to look at the average price of rental units in each borough. We click the label of the variable in the "Values" field and choose "Average" from the list.

![Airbnb - average price per neighborhood](/presentations/DTL/en/4.9/W/M_00_S_04/a44296d1-15f7-4aff-88db-27065be8ae17/student_content/48e3bebe-6368-4576-9117-b009bcb9ba13/images/Airbnb_11.png)

It turns out that the most expensive neighborhood is Prospect Park, where the average rental price is more than  653 USD, which is much more than the average rental price per night in all of New York.

### Exploring the `room_type` variable

Let's create one more pivot table using the `room_type` variable. Let's drag the label with the name of the variable to the "Rows" field, and to "Values" let's drag the `id` label.
Again we see a two-column table, which this time answers our other question:

**"How does the number of listings break down by type of room? "**.

![Airbnb - number of offers per room type](/presentations/DTL/en/4.9/W/M_00_S_04/a44296d1-15f7-4aff-88db-27065be8ae17/student_content/48e3bebe-6368-4576-9117-b009bcb9ba13/images/Airbnb_12.png)

In our table, we see that most listings are for entire home/apt or private room rentals.
On Airbnb, we'll book a hotel room from a choice of 202 listings (as a reminder, there are 39881 total listings), and a shared room from 557 listings.

## Summary

We've done a thorough exploration of our data and we already know more and more about Airbnb rental listings in New York.
Of course, as in the previous step, we intentionally didn't do all the work.
We want to give you the opportunity to discover more interesting phenomena in our data on your own.
Your task will be to complete the data exploration process and formulate answers to the remaining questions.

### Good luck!
