# Framing the problem

Type: Article

## Introduction

In the previous materials you were able to learn what the Data Science process is.
You know what it is characterized by and what steps this approach to data analysis consists of.
In the course of the lecturer's classes, we will gradually expand our knowledge of each step of the process.
For this moment, we want to show you what data analysis looks like with a practical example.
This way, even before the classes begin, you'll see the specific challenges you're going to face as a data analyst .
Now that we know the basics, there's no need to wait.

### **Let's start our first data analysis!**

## Framing the problem

The first step in the data analysis process that we will focus on, is defining the problem.
This stage is very important, because during it we determine what our task will actually be during data analysis. It is important to gather as much knowledge as possible about the problem we're studying.
There are several good ways to build your own knowledge base:

- Asking the right questions
- Getting familiar with the documentation
- Talking to employees who have knowledge in the area you are interested in

What are we going to analyze?

You are surely familiar with (or have heard of) the name Airbnb. Founded in 2008, Airbnb is an online service (one of the founders has Polish roots ) that allows people to rent accommodation from private individuals. The portal has about 4 million hosts, 85% of whom are from outside the United States.

Let's say Airbnb is looking for a person to join its analytics team to help solve problems based on the data the company collects. An Airbnb recruiter sends you a specific proposal along with a dataset in an .xls file. Let's say you want to try your hand at recruiting. At this point, you only have the data file, the meaning of which you don't quite know. To get started, you need to ask a series of questions. This will give you a good understanding of the problem you want to solve.

In the context of Airbnb and the dataset, we can ask:

- What exactly does Airbnb do?
- What do the different columns in the data file mean?
- What is the aim of analysis?

Being employed as a data analyst in a company, some questions of this type may be obvious to you. For example - the meaning of the different columns will be familiar to you, because you have previously happened to work with data in the given format. Secondly, one of the employees at your company may have prepared documentation explaining the meaning of each variable. The detail of the questions needed to accurately define and understand the problem will be different in each case and will depend on your knowledge, as well as the people you work with. Time plays in your favor - the more time you spend working with data in the company solving various problems, the greater your knowledge of the product or company strategy will be.

In the meantime, the recruiter wrote us back pretty quickly, answering the questions:

Airbnb is a service through which people from almost all over the world can use rent out their property to tourists or long-term clients.
The portal verifies landlords and the listings they post, allows correspondence between landlords and tenants, and allows the secure transfer of funds between parties.
The file contains a range of information about the offers that were shown on the search results. Below you'll find a glossary explaining the meaning of each column:

- **id** – offer id
- **name** – offer name
- **host_id** – id of the landlord
- **host_name** – name of the host
- **neighbourhood_group** – name of one of the five NYC boroughs: a district of smaller neighborhoods
- **neighbourhood** – name of the neighborhood
- **latitude** – room location latitude
- **longitude** – room location longitude
- **room_type** – type of the rented property
- **price** – rental price for the room
- **minimum_nights** – the smallest number of nights the room can be rented for
- **number_of_reviews** – number of reviews for the room
- **last_review** – date of the newest review
- **reviews_per_month** – average number of reviews per month
- **calculate_host_listings_count** – total number of listings published by the host
- **availability_365** – number of available days per year
- **number_of_reviews_ltm** – number of reviews in the last 12 months
- **license** – permission to rent the room

New product owner would like to know something more about the people renting rooms in particular areas.
The next, more detailed analysis will be the seed for making recommendations to users of rental listings.
PO prepared a list of questions they would like to know the answers to:

- **What is the average price for renting a room for one night?**
- **How many of the hosts have more than one listing on the site?**
- **How does the number of listings break down by type of room?**
- **What is the number of rooms by district? For what reason do some neighborhoods offer more rentals?**
- **In which neighborhoods will the rent be highest?**
- **Are hosts more likely to rent for short or long periods?**

## Summary

OK - as you can see, we obtained answers to the questions we asked. As a result, our knowledge of the problem, as well as of the data itself, has increased significantly.
But does this mean that we already know everything we need to make an informed, complete analysis of the problem presented?
Since we put the question this way, you can probably guess that we don't.
We mentioned earlier that asking questions is key - don't be afraid to do so.
Again, analyze the answers carefully, as well as the data table, and think about what information might be relevant to you.

### Good luck!
