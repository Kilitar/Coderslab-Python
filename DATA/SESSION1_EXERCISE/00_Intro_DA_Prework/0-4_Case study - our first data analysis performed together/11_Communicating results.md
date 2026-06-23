# Communicating results

Type: Article

## Introduction

We have reached the end of our first data analysis, or rather, the last step is still to come.
You may have domain knowledge, knowledge of statistics and machine learning, perceptiveness and attention to detail.
Even so, what's crucial for you as a data analyst is the ability to communicate your results in a clear and transparent manner.
As you probably remember, our analysis was intended for a business-related person (the product owner).
Such audiences very much appreciate a concise, graphical presentation of the conclusions drawn from the data.
And this is where a variety of data visualizations come to our aid, which we can use in data storytelling.

## Evolution of data visualization

We can actually find data visualizations everywhere - this is because it's the easiest to understand form of explaining a selected issue.
For this reason, there are many different solutions on the market for building visualizations and dashboards, composed of multiple visualizations sharing a common topic.
Over the past few years, the market for data visualization software has grown tremendously.
Tools are available that make it possible to create great-looking visualizations with just a few clicks.
Excel offers the ability to generate charts of various types, but compared to the best solutions, it has its limitations (e.g. difficulty in building complex visualizations, lack of integration with cloud data, or data volume limitations).
That is why we devote a separate course during the Data Lab track, where we uncover the secrets of data visualization using Python libraries, as well as the most widely used **"business intelligence "** tool, Tableau.

![Tableau - sample dashboard](/presentations/DTL/en/4.9/W/M_00_S_04/077daf8a-0bad-4a70-aca5-f9d8cae21ca9/student_content/46babb0c-5f63-446f-88b2-4fb8fcf87cf1/images/Tableau.png)

*Source: [Tableau Public](https://public.tableau.com/app/profile/ali8773/viz/RetailTransactionDashboard/Dashboard1)*

Nevertheless, at the beginning of our data analysis journey Excel will be a very good choice due to its universality and ease of use in the context of creating simple charts.

## Basic types of charts

In this course, we will discuss the most commonly used visualizations. You will learn how to match the type of chart to the data, as well as how to format the appearance of the chart to increase readability. Considering the type, we can distinguish between charts:

- Column and bar (e.g., to show differences between categories)
  Column chart example
- Line (e.g., to show data trends over time)
  Line chart example
- Scatter plot (e.g., to illustrate differences between two numerical variables)
  Scatter plot example
- Box plot (to quickly present the most important statistical measures of a selected variable)
  Box plot example

## Creating charts to present the results of data analysis - Airbnb

We have talked briefly about what data visualization gives us and what types of charts are the most interesting for us (at this point).
Let's now focus on working with charts so that, we can present the conclusions of our analysis in an interesting way.

Let's return once again to the questions we were asked in the context of our analysis. Looking at the questions again will help us decide on the form in which we'll show the data in the presentation.

**- What is the average price for renting a room for one night?**

Since the average price per unit is a single number, we can add it on a slide with description. There is no need to present it on a chart (for example, as a single column).

- How many of the hosts have more than one listing on the site?

We could present this information analogously to the average price of a property on Airbnb - we could add a single slide with the information given as a percentage.

We could also present it in a pie chart, but this type of chart is not the most effective way to present data. Often visualizations of this type are misleading because the human eye can't quite handle comparing the angles of the slices.

- **How does the number of offers break down by type of property?**.

For this information, it would be best to use a column chart, that can help us see how many offers we can assign to a particular type of property and illustrate the differences between the various types.
We select the data in the pivot table where the number of rooms divided by room type is calculated.

![Airbnb - selecting data in pivot table](/presentations/DTL/en/4.9/W/M_00_S_04/077daf8a-0bad-4a70-aca5-f9d8cae21ca9/student_content/46babb0c-5f63-446f-88b2-4fb8fcf87cf1/images/Airbnb_19.png)

In the "Insert" tab, we click on the "PivotChart" symbol and select the "Clustered Column" chart.

![Airbnb - choosing chart](/presentations/DTL/en/4.9/W/M_00_S_04/077daf8a-0bad-4a70-aca5-f9d8cae21ca9/student_content/46babb0c-5f63-446f-88b2-4fb8fcf87cf1/images/Airbnb_20.png)

Let's create a new worksheet called `charts` where we're going to move all the charts we created.
We will also enable data labels, and change the chart title to clearly indicate what it presents.

![Airbnb - editing chart](/presentations/DTL/en/4.9/W/M_00_S_04/077daf8a-0bad-4a70-aca5-f9d8cae21ca9/student_content/46babb0c-5f63-446f-88b2-4fb8fcf87cf1/images/Airbnb_21.png)

Finally, we'll change the color of the columns - let's choose one that is similar to the color used in the Airbnb logo, and we'll also sort the values in the chart in descending order. To do this, we right-click on the columns, select "Sort" and then "Sort Largest to Smallest."

![Airbnb - columns color selection](/presentations/DTL/en/4.9/W/M_00_S_04/077daf8a-0bad-4a70-aca5-f9d8cae21ca9/student_content/46babb0c-5f63-446f-88b2-4fb8fcf87cf1/images/Airbnb_22.png)
![Airbnb - sorting data in a chart](/presentations/DTL/en/4.9/W/M_00_S_04/077daf8a-0bad-4a70-aca5-f9d8cae21ca9/student_content/46babb0c-5f63-446f-88b2-4fb8fcf87cf1/images/Airbnb_23.png)

**- What is the number of rooms by district? For what reason do some neighborhoods offer more rentals?**

To show the number of rooms divided by neighborhoods we can only consider the ones with the highest number of rooms. We have as many as 244 districts, so if we put them all on the chart, it could become completely unreadable. A bar chart with numerical values sorted in descending order will work well in this case.
First let's sort the list of neighborhoods according to the number of offers (`Count of id`).
We select an interesting range of data (let's assume that we choose the first 20 neighborhoods) and copy it to another place by selecting any cell in the free space of the sheet.
We select the extracted data and from the "Insert" -> "Charts" section we choose the column chart icon and then the "2-D Bar" chart.

![Airbnb - bar chart](/presentations/DTL/en/4.9/W/M_00_S_04/077daf8a-0bad-4a70-aca5-f9d8cae21ca9/student_content/46babb0c-5f63-446f-88b2-4fb8fcf87cf1/images/Airbnb_24.png)

We perform similar operations as before - turn on the data labels, change the color of the bars and set the appropriate title of the chart. We also need to increase its size slightly so that all the axis labels, on which the names of the districts are located, are visible.

We set the sorting in descending order - so that the bar showing the neighborhood with the highest number of offers is the highest. We click the labels of the axis where the names of the districts are located, and then check the "Categories in reverse order" option in the axis options, because by default Excel has set ascending sorting.

![Airbnb - sorting in a bar chart](/presentations/DTL/en/4.9/W/M_00_S_04/077daf8a-0bad-4a70-aca5-f9d8cae21ca9/student_content/46babb0c-5f63-446f-88b2-4fb8fcf87cf1/images/Airbnb_25.png)

You will create the visualizations for the other two questions yourself, analogous to those made in the article. Nevertheless, we'll give you a hint on how to approach this and what chart to use.

**- In which neighborhoods will the rent be highest?**

When considering the ranking of the most expensive neighborhoods, taking into account the average rental price in the neighborhood, a column chart will work very well.
The audience will be able to instantly determine the differences between neighborhoods.
In order to maintain the readability of the chart, we'll limit the number of neighborhoods we show on the chart.

**- Are hosts more likely to rent rooms for short or long periods?**

We will present the categorization of premises in relation to the length of the minimum rental period in a bar chart. The length of the bars will help you quickly get an answer to the question.

## Ordering data for presentation purposes

We have already created individual visualizations that answer the questions we were asked.
The results of the analysis, which are carried out in Excel, are very often summarized in the form of a PowerPoint presentation.
We are able to transfer charts from Excel to a presentation very quickly. All we need to do is select the desired chart, press "CTRL+C", move to the desired slide in Powerpoint and press "CTRL+V".
The question remains as to what would be the best way to put charts in the presentation.
And here's the answer - it is a good practice to follow the "top-down" approach.
In our case, the "top" -" general" information will be, for example, the average price of a property or the percentage of hosts with more than one property on offer. Then we can present more detailed data, such as the number of units by room type, and finally present detailed data on neighborhoods.

Accordingly, we have created a title slide, two slides with important figures we calculated during the analysis, and two slides with charts created in this article.
Your task will be to add the other two visualizations to the presentation to complete the results of the analysis and be able to communicate them to the audience.

## Summary

We are one step away from completing our first data analysis together. In this article, we covered the part related to charts.
We recalled the types of charts, and how to generate some of them in Excel and then put them into a PowerPoint presentation.
The knowledge of visualization is very extensive, so we'll discuss further topics in the lecturer's class.

**Now it is your turn to create charts — good luck!**
