# In-depth data analysis

Type: Article

## Summary of data exploration

We are getting close to the end of conducting our data analysis - the fifth and penultimate step, i.e. in-depth data analysis, is ahead of us.
This is the moment when we already have a great understanding of the problem we need to solve and we know the limitations of our data. We also know what relationships our data represent.
We have learned the answers to the questions:

- What is the number of units by neighborhood? For what reason do some neighborhoods offer more rentals?

There are as many as 10 neighborhoods in New York City that offer 1000+ rental units (on Airbnb alone!).
Why is there a lot of variation, given the number of listings between neighborhoods? There could be many reasons, such as:

- proximity to the center,
- location in relation to public transportation,
- proximity of location to tourist spots (important especially for tourists!).
- Are hosts more likely to rent rooms for short or long periods?

The largest number of offers is for units that can be rented for a minimum of 30 days. Grouping offers for short, medium, and long-term rentals, we see that the largest number of units are rented on a short-term basis.
This may be due to the fact that it is much easier for hosts to find a client for a few days (tourism) than for, say, a few months (e.g., students).

- How many of the hosts have more than one listing on the site?

We counted how many hosts we have by the number of listings (units) on the portal.
One unit in the listing has 54.47% of them, so it follows that as many as 45.53% of hosts have two or more units for rent (only through Airbnb).
It's possible that hosts actually own an even higher number of properties.

## What is in-depth exploratory analysis?

In-depth exploratory analysis is about building a model that will bring applicability to the business and make a real difference.
To create the best possible solution, dedicated to our problem, we need to:

- make a selection of different models, so that the algorithm used, has a chance to be selected appropriately for our data,
- select the most relevant variables in our data,
- divide the dataset into two: training and testing,
- select model fitting parameters and train the model on the training set,
- verify that the model trained in this way performs adequately on the test set,
- compare the models and select the one that best represents our data and meets the requirements for the metrics (both technical and business).

As you can see, the process consists of several well-defined steps, which may now seem a bit difficult.
Of course, building machine learning models requires specialized knowledge. However, you need to know that getting to a place where the model you have built can find application in solving your problem is extremely rewarding.

The most mature and popular tool for building machine learning models is Python - a very friendly, easy-to-learn programming language, which you will learn in a dedicated Data Lab path course.
The wealth of libraries written in this language allows you to build solutions based on the simplest algorithms like. **"k nearest neighbors "**, possible to implement with a few lines of code.
Of course, the applications of Python tools are huge and we can build much more complicated solutions such as models using neural networks. We will elaborate on the topic of the possibilities offered by in-depth data analysis during the class with the lecturer.

## In-depth analysis of Airbnb data with Excel

### Linear function

For the moment, let's return to what interests us most. We want to use our knowledge in Excel for in-depth data analysis.
You probably got familiar with linear function at some point in your math classes.

Linear function (straight line in a chart) is described by the `y = a * x + b` equation,

where `y` is the dependent variable and `x` is the independent variable. The letter `a` describes the directional coefficient of the relationship, and `b` describes the free expression.

It turns out that for any pair of variables in the data it is possible to find a best-fit (which doesn't at all mean that the fit will meet our expectations) linear function.
In that case, let's see what linear functions Excel will select for our chosen data.

Let's look at our source data and think about what relationships between numerical variables we want to examine.
Let's say we want to see if the price of renting a property depends on the minimum number of nights for which the reservation can be made.

You might think that the longer the rental, the lower the price per night (because the owner is guaranteed a rental, which isn't obvious, for example, in short-term rentals, where there can be downtime between bookings).

### Let's estimate a trendline to our data.

Let's create a new data sheet named "in_depth_analysis" and then from the "Insert" tab, we select the icon with drawn points in X and Y space, which stands for scatter plots.

![Airbnb - adding scatter plots](/presentations/DTL/en/4.9/W/M_00_S_04/fb9acccd-13cd-4e42-8322-1045b7f9c1b4/student_content/b65b52b3-0c92-4a0c-a516-f659a416d916/images/Airbnb_13.png)

Then, we click "Select Data" and go to the sheet with the source data.

Let's select the data belonging to the `price` variable (Y axis) and `minimum_nights` (X axis).

![Airbnb - assigning variables to axes](/presentations/DTL/en/4.9/W/M_00_S_04/fb9acccd-13cd-4e42-8322-1045b7f9c1b4/student_content/b65b52b3-0c92-4a0c-a516-f659a416d916/images/Airbnb_14.png)
![Airbnb - assigning variables to axes](/presentations/DTL/en/4.9/W/M_00_S_04/fb9acccd-13cd-4e42-8322-1045b7f9c1b4/student_content/b65b52b3-0c92-4a0c-a516-f659a416d916/images/Airbnb_15.png)

Excel generated a scatter plot, showing the relationship between the two variables. At this point, we would like to estimate straight line for our data - we click "Add Chart Element" and then "Trendline" and "Linear", which corresponds to a linear function.

![Airbnb - generating trendline](/presentations/DTL/en/4.9/W/M_00_S_04/fb9acccd-13cd-4e42-8322-1045b7f9c1b4/student_content/b65b52b3-0c92-4a0c-a516-f659a416d916/images/Airbnb_16.png)

A straight line which describes our relationship appears on the chart.
By double-clicking the generated straight line, we can have Excel display the equation of the straight line on the chart and the R2 coefficient (a measure of the quality of the model's fit to the data).

![Airbnb - adding equation and R2 to the chart](/presentations/DTL/en/4.9/W/M_00_S_04/fb9acccd-13cd-4e42-8322-1045b7f9c1b4/student_content/b65b52b3-0c92-4a0c-a516-f659a416d916/images/Airbnb_17.png)

The equation of our line is `y = -0.3983x + 205.32`, which makes it a decreasing function (`a` is negative).
Let's select any point separated from the line – we chose the offer where the `minimum_nights` variable is 360, and the price per night is USD 5143.
Putting 360 for `x` in the formula gives `y` (or price) equal to `-0.3983 * 360 + 205.32`, that is: USD 61.93.
As you can see, the difference is huge and this proves one thing.

Our relationship is not linear and the vast majority of observations, are concentrated in a narrow interval (0, 200) on the X axis.
From this it follows that we must reject our hypothesis, because we do not see a linear relationship in the data that would say that as the number of minimum nights of a single booking increases, the price per night decreases.

Let's test two other variables in an analogous way - the number of reviews, and the number of reviews over the last twelve months.

Here the situation is slightly different, as we can see some linearity in the data.

![Airbnb - linear model for the second pair of variables](/presentations/DTL/en/4.9/W/M_00_S_04/fb9acccd-13cd-4e42-8322-1045b7f9c1b4/student_content/b65b52b3-0c92-4a0c-a516-f659a416d916/images/Airbnb_18.png)

In this case, the R2 coefficient is much higher and indicates that there is some linear relationship between the observations.
Of course, it is still not perfectly linear, due to outliers (that is, points furthest from the straight line), which is one of the characteristics of a linear model. Still, putting `x` in the linear function formula, yields a much smaller difference between the calculated and real values than in th case of the first pair we analyzed.

However, there are certainly relationships that are likely to be more linear, such as price per unit vs. number of rooms in a unit.
Of course, this is our hypothesis, which we can't test, since we don't have information on the number of rooms in a unit.
Nevertheless, it could be that there is a strong relationship between these variables, and we could build a model that could, for example, assist hosts in determining an adequate price for renting a unit when filling out the Airbnb listing form (based on various variables, including the number of rooms).

## Summary

We supplemented our knowledge with answers to the remaining questions based on an exploratory analysis.
We also talked about what in-depth data analysis is and how powerful it can be when working with data.
We learned how to generate a simple linear model and test its effectiveness.
We analyzed the fit of two pairs of variables in our data to a linear function generated by Excel.
In the class with the lecturer we will learn more and talk about other tools, such as non-linear models.
Now it's your turn - your task will be to check the relationship between the two variables indicated.

Maybe you can discover more interesting information in our data?

### Good luck!
