# Data Science process in detail

Type: Article

We will now present the details of the *Data Science* process by discussing each of its steps:

![Data Science Process](/presentations/DTL/en/4.9/W/M_00_S_03/982fb032-d39c-4390-a4ff-0d46080bf0db/student_content/92f918c9-89c6-4e7e-8d4c-64c1a7afb02b/images/Data_Science_Deconstructed_loop.png)

## 1. Framing the problem

This is the most important stage of the work: determining the actual scope of the task. In some industries, this step is obvious and natural. In the construction industry, a design is needed before work can begin, and the design requires information from the client: roughly what kind of building they want to put up, on what kind of land, and at what standard and budget. Those who have ever built a house or renovated an apartment know that the implementation of such projects doesn't always go smoothly and there are surprises. At the same time, it is more-less clear what to expect.

In scientific research activities, things are sometimes much less clearly defined. Often work begins with a very generally posed problem, such as *developing a method for early detection of cancer*.
Of course, one would have to ask subsidiary questions, similar to those for building a house:

- What kind of cancer do we want to detect? Lungs? Pancreas?
- What methods do we want to use to detect cancer? CAT scan? Blood count?

Suppose we want to detect pancreatic cancer, which is difficult to detect at an early stage, based on blood count. It attacked Hans Rosling, whom you have already had the opportunity to meet, and Steve Jobs - one of the founders and former CEO of Apple. A hospital, which specializes in the diagnosis and treatment of pancreatic cancer, has collected historical blood count results from its patients and is now asking for your help in using this data to find a way to more effectively select patients for more accurate tests.

The possibilities are endless: we may be asked to price houses and apartments in urban areas, to predict how likely a customer is to leave our client's business, or what product they would like to buy next from an online store.

It is worth asking how a given problem is currently being solved. Why does someone want to improve an existing solution? How deep would the change be? How would the results of our analysis be used?

### The knowledge and skills you need

- **Domain knowledge** - this is the knowledge that is closely related to the problem being solved, such as the knowledge of a doctor specializing in the diagnosis and treatment of a particular condition or a real estate appraisal specialist. With domain knowledge, people will find it much easier to understand the essence of the problem, learn the terminology currently used and understand the meaning of the available data.
- **Product knowledge and intuition** - by gathering product knowledge, you will learn what kind of data you may still have available and what kind of data you may not be able to obtain. Often this is the key limitation. In addition, you'll learn what the limitations and expectations are for the solution you're preparing. E.g., a product for the automatic sale of advertising space on the internet has to make a decision on what ad to display to the user - and it has 15 milliseconds to do so. This is very little time for a decision, even for a computer, so the final solution must be computationally simple.
- **Business strategy** - by knowing the company's strategies, goals and business priorities, we can better guide our data analysis and narrow its goals. Continuing with the example of a company that sells ads on the Internet: through a conversation with a business partner, we learn that current solutions are good, but the company would like to improve them further, increasing the likelihood of clicks on displayed ads.
- **Building an interdisciplinary team and key resources** - this is an important element because data analysis is, in fact, a team sport. It is very difficult to quickly gain domain and product knowledge and at the same time understand business strategies and goals. It is much easier to assemble a team to support us in these tasks. In our example regarding ads, we can involve a sales manager. Such a person knows well what kind of website ads the company sells or in which places banner ads are usually displayed, and how users respond to them. This way, we don't have to waste time getting such information ourselves. With a sales application database programmer who knows what data on the ads displayed in a given session can be easily obtained, we will be able to design the first analysis of this problem. By contacting the product manager who is responsible for implementing the business strategy, we'll also quickly learn whether the results of our analysis have significant business value.

### Ask a lot of questions

At the beginning of your work, it is crucial to ask as many questions as possible. They will deepen your understanding of the developed issue, as well as the business objective itself.

In the example of the advertising company, increasing the probability of clicking on an ad by 0.5% may not be a significant improvement, but increasing the probability of a user buying after clicking on an ad 0.5% at first glance may not be a big difference. However, it is a significantly different problem pursuing different business objectives and requiring significantly different data for analysis (e.g., data from contractors on actual sales).

## 2. Collecting raw data

After initially asking questions and assembling a formal or informal project team, it was time to identify available data sets for analysis and convert them into a useful format for analysis. In the previous step, we gathered enough information to define well the purpose of the analysis and to define the required data that will make this analysis possible. In this step, we actually gain access to those data that enable the collection of other data: among others, from social networks. They include the company's application databases, external databases, public data sets in the form of files, data extracted through APIs (*application programming interface*). Stand-alone applications are sometimes created to collect them, if the task seems to justify the need.

Very often, raw data from external data sources are copied into a new database created for analysis or copied into files in useful formats on the data analyst's computer. There are several reasons for doing this:

1. Reading data from source systems is sometimes time-consuming and can put a strain on application servers, destabilizing the service.
2. We usually only have the ability to read data without the ability to write intermediate analysis results to the source systems.
3. The source systems are distributed and don't have the capability or tools to further edit and process the data.

At this stage of analysis, it is often useful to have the help of a database administrator or programmer who is well versed in database programming languages and can help extract the right information from an often complex and constantly changing database in a format that is relatively easy for us to read. Similar to the previous stage of framing the problem. In the course of extracting **raw data**, we may need to perform this task several times before the database programmer or ourselves extract all the necessary information from a database, application or data repository in another format (such as excel files or text files). Data can also be stored in distributed datasets in cloud infrastructure, supported by technologies such as *Hadoop*, *Spark* or *Flink*, but we can also get it in unstructured form. A good example of such data is textual data, such as that contained in public posts on social networks or in comments under articles on news portals.

It is worth looking carefully at whether the **data** we have collected is likely to contain the **information** we are looking for. What could this mean? Continuing with the example of an online advertising company, we should verify that our dataset contains the kind of data that will enable us to measure the effects we are looking for, here: the impact on sales on the advertising company's customer platforms. The impact of how ads are displayed on sales is the *information* we are looking for.

Having all possible data on the number of displayed ads of a given type on a page and information on whether any were clicked doesn't necessarily mean that in the same set we'll find data on whether an ad click resulted in a purchase on the advertiser's platform. It may turn out that this type of information will be stored in separate datasets, or it simply wasn't there because no one needed to combine such information before. That's why it's a good idea to check this before going further in the analysis process.

Still, one of the most popular ways of storing data are databases that support SQL language implementations. You will learn how to work with such databases in the course ***SQL - Data Analysis***.

## 3. Processing and cleaning data

Data processing at the initial stage has 3 main goals:

1. To better understand the definition of data stored in datasets,
2. To check and improve the quality of the data,
3. Change of structure of data making the analysis easier.

### Knowledge

At this stage of the process, you'll learn in detail the definitions of the variables that you'll come to work with in the collected datasets. A variable is a characteristic that can be measured and can take different values (e.g. height, income, gender, date of birth). You will understand what the information in the datasets you have acquired really means in relation to the processes, phenomena or objects they describe.
You will have the opportunity to find out whether you can trust every variable in a given dataset or only some of them; completely or to a limited extent. E.g., optional fields in web forms are often left unfilled by users. Other fields are sometimes filled in with incorrect information or are used only occasionally, but these are the use cases you care about most. You may want to correct some of the observed gaps or errors based on other available information, or simply exclude them from your analysis if you think that's the best solution.

This is also the point at which you want to **order the data** in a way that will be easy to further analyze and visualize. What does this mean? Often this depends on the type of analysis and data storage you'll have available. Most often, however, it comes down to collecting the data in the form of a *table*, which in *columns* describes the variables chosen to illustrate each data point. In the *rows*, we usually want to have unique *observations* or data points about the problem being analyzed. At this stage, it's worth checking that you have as many *rows* as you expect. There may be many reasons for the discrepancy - you'll learn about some of the possibilities during the *prework* and in the course.

***Example:***
Our company operates an online store and always sends its products by courier to customers. For processing orders, it collects their contact information in databases. The company intends to expand its distribution centers to be closer to its customers and reduce delivery times. To this end, it has asked for an analysis of the customer delivery database. Reviewing the data, we quickly realized that it contained data on several hundred thousand shipments, and that each shipment was described by as many as 89 different variables. We noticed many variables with names such as *Customer_ID*, *Order_ID*, *Shipment_ID*, as well as *Residence_Address*, *Invoice_Address*, *Delivery_Address*, and other similarly named variables related to zip code, city and country.
Reviewing samples of address data, we noticed that the residence address fields are usually populated with values that look like address data. Those related to billing address are rarely filled in, at about 10%. In contrast, the field with delivery address usually contains a string of digits. In a conversation with an online store application developer, we learned that each customer can have several delivery addresses. The list of customer delivery addresses is stored in a separate dataset, and it is through the *Delivery_Address* variable that this data can be included. We also learned that the field should have been named slightly differently: *ID_Delivery_Address*. However, the change that introduced the possibility of having multiple delivery addresses in the system took place a very long time ago, when there were not yet good programming practices in the company related to variable naming.
During this conversation, we also agreed that the programmer would add the correct shipment address data to our dataset as additional variables in our collection for analysis.

### Skills

When processing and cleaning the data, good skills in data processing tools are crucial. This can be **Excel** or more advanced data analysis systems (e.g. SAS, DataIKU) or programming languages (**SQL**, **Python** or R).
Intuition, which comes with experience, proves to be very useful, as well as.... unfettered curiosity. Therefore, do not limit yourself and ask a lot of questions!

In this course, you'll use Excel, which is often used by programmers as well - as a tool for relatively quick viewing of data and easy interaction with data. Excel also serves as a practical platform for sharing data and results with a wider range of stakeholders, and as a basic tool in the next stage of analysis: *data exploration*.

## 4. Exploring data

Going into data mining, we usually already know what kind of data we have and how good a condition it is in. We also have a few trips back to the beginning of the process to refine the purpose of the analysis, or to look for missing columns that turned out to be empty in the originally acquired dataset.

At this stage, we're interested in learning more about the subtleties in the data. We are looking for patterns and interdependencies in the data. For example, which variables are very similar to each other or which variables best differentiate the observations in the set. Depending on the problem, this may mean grouping data into categories and comparing them with each other, or looking for relationships between pairs or groups of variables.

Data visualization is very useful for this purpose - in the form of a variety of charts. As it turns out, humans in the course of evolution have developed a great sense of visual pattern identification. This is why most of us believe to be "visual learners". That's why charts and graphs are so helpful. Didn't we already see this in the video with Hans Rosling?

It is during data exploration that we usually pose the first serious research questions and *hypotheses*, which we'll verify on the basis of the data and statistical elements we have. We will explore relationships between data fragments, *correlations* or cause-and-effect relationships. If acquiring new data and making changes to the source systems under study is easy, we can also design experiments that will help verify our hypotheses in the system.

It is often the case that observations already made during data exploration are of great value to our stakeholders. Therefore, it is worth sharing them with the interdisciplinary project team formed at the beginning of the process, which should support us with the domain knowledge surrounding the issue we're working on. This way we'll collect all possible observations from the very beginning.

***Example:***
We drew up a chart segmenting business customers by order value. In this chart, we read that business customers are fairly evenly distributed across the order value ranges:

- $0 - $1.000,
- $1.001 - $5.000,
- $5.001 - $10.000,
- $10.001 - $15.000
- $15.001+.

From our point of view, we didn't discover anything special on this chart except that the data looks *"OK"*. However, when we showed this data to the sales manager for business customers, she was very surprised and moved by this graph. It turned out that the company required business customers to have a minimum order value of $2000, so customers received preferential purchase and delivery terms. The sales manager's previous reports did not include data of this kind, only aggregate monthly summaries. After a brief conversation with the manager, we verified that despite not reaching $2000, most deliveries below the minimum order value were also being made on preferential terms. This is because it turned out that the implemented change in contracts with business customers was not reflected in the sales system. Thanks to this discovery, the sales manager took care to make the appropriate changes to the system. Better enforcement of contractual terms helped reduce logistics costs by $90000 per year and, according to the manager's estimates, will improve net margin for this customer segment by 5%. Thus, the manager will fulfill the target set by management for the business customer segment.

![B2B orders](/presentations/DTL/en/4.9/W/M_00_S_03/982fb032-d39c-4390-a4ff-0d46080bf0db/student_content/92f918c9-89c6-4e7e-8d4c-64c1a7afb02b/images/Order_numbers.PNG)

### Knowledge

Knowledge of chart typologies, their scope of use, and typical errors in chart creation and comparison will be crucial. We will devote an important part of the *prework* and the course to this topic. Data visualization is such a broad topic that it is safe to say that it functions as an independent domain. At Coders Lab, this issue is deepened by a dedicated course ***Data Visualization***.

Having knowledge of the basics of mathematics, statistics and its measures, and statistical inference is now becoming increasingly important. With such knowledge, we will be able to identify which data significantly deviate from the majority of cases, even if they're not very far on the scale; or, on the contrary, despite increasing intervals, we will be able to conclude that the data correspond to a known exponential progression. Sometimes it is useful to transform variables to another form. The process of transforming variables can be very complex and involve many variables at once. A common term for the transformation of variables in the industry is: ***feature engineering***.

### Skills

For data exploration, our innate sense of looking for visual patterns and curiosity is often enough. Even though we have cleaned the data of obvious errors at an earlier stage, we should still expect that most of the outliers, odd or obvious *patterns* are precisely due to errors or deficiencies in the data, which are difficult to grasp without a good visualization of the entire dataset.

After a few steps back to fix and update the data again, the correlations we will observe are going to be more subtle. And this is where the ability to critically question the data becomes crucial. It turns out that without the rigor and apparatus of statistical inference, it is very difficult to formulate the right questions. And without properly posed questions, it will almost always be the case that the answers we formulate are going to be wrong.
Proficiency with analytical tools such as Excel or specialized programming languages and libraries is what makes us successful and gives us fun!

Did you know that before the era of computers, charts and graphs were made by hand, plotting point by point on a piece of paper using a pencil, ruler, compass or other, more sophisticated, drawing aids? Perhaps you remember such tasks from math or physics lessons at school? Now, without much effort with the help of computers and dedicated software, you can create charts composed of millions of data in a few clicks or with a few lines of code.

***Example:***
Comparing the value of sales between city A and B, we discovered that the average value of sales in A is 3000, while in B it is 3500. Is this difference significant? Maybe.

Looking at the outliers, we discovered that there were two very large transactions of 50000 and 100000 in City B. These were not *typical* purchases and we decided to eliminate them from the collection. Now the average sale in City B is 2800. Is the difference still significant? It still can't be clearly determined.

We hope that when you complete this course you'll have not only the basic knowledge and tools for data visualization, but also the statistical intuition to help you pinpoint the *probable* answer to this kind of questions.

It is useful to conclude your data exploration with a presentation of intermediate results. Besides, questions and expectations often arise to find out more, in greater detail or certainty. So it's worth setting further directions for analysis with your team and stakeholders.

Now, we will probably focus on a slice of data or a specific type of analysis. Very often, at this stage of analysis, we also decide on a strategy for dividing our data into subsets that will later help us verify the validity of our conclusions or the effectiveness of the statistical model we built.

## 5. In-depth data analysis

We are already very experienced in working on the problem entrusted to us:

- we know the business context of the problem,
- we have a good understanding of the purpose of our work and what is expected from it,
- we're very familiar with the conditions under which the data we're analyzing was created, and we know its flaws and limitations,
- we have a very good understanding of the picture presented by the data we're analyzing.

In a word, we have identified almost everything that could have disturbed the true state of affairs, and we know very well what is hiding on the surface of the data we analyze.

Now, based on the data we have, we want to build a ***model*** that will be useful in business practice and influence the decisions company makes or change the performance of one of its products. In a nutshell, this is done in 2 steps:

1. creating the model,
2. evaluating its efficiency

In practice, it is very common to perform these steps repeatedly in a loop:

- we choose the most promising one or several types of data models,
- we select the key variables to be included in the model on the basis of previously gathered knowledge or very simplified measures of dependence,
- we pick the best model fitting parameters on a ***training*** subset,
- we check whether the model so fitted still meets the fitting parameters on another ***(test)*** subset,
- if we are testing several models, we select from them the one that we think best represents the data and meets the criteria and measures of success established with the key decision makers at the early stage of problem definition,

The last step is very important because in the current state of the art we can actually test millions of different data models.

Nowadays increasingly, the volumes, the speed of data processing and the very phenomena we want to capture are ultra-fast. Therefore, the efficiency of a model or proposed changes to applications are evaluated almost in real time or in the form of A/B testing, where a selected sample of users is presented with a changed version of the product and their behavior is observed.

### Knowledge and skills

A solid knowledge of mathematics, statistics and probability is often necessary to deepen and verify the information gained in the data exploration stage.
Today, programs such as Excel are able to fit simple data models to graphs with a few clicks. They do not offer a simple implementation of the described modeling process, but they give all the tools to carry out such a process, if we have adequate knowledge of statistics and data modeling.

Being advanced data programmers in Python, we can take advantage of very good, sophisticated, yet simple (for a programmer) to use, machine learning libraries that perform the entire process of fitting the model to data, testing and validation. However, they carry a lot of risk for inexperienced analysts and data scientists. These libraries are often unable to assess the quality and validity of the analyzed data we focused on in the first steps of the Data Science process. That's why these first steps are so important and can't be skipped - libraries won't do this part of the job for us.

The business knowledge we gain, combined with our knowledge of data modeling and assessing the model's efficiency and reliability, will also be key to determining the value that our proposed solution brings. For example, by analyzing banner display data on websites, we discovered that changing the grouping of banners will improve the click-through rate of our company's positioned ads by 1% per 100 views. This increase is likely to translate into as much as a 10% increase in the company's revenue from this ad segment. We confirmed the model's results on historical data from randomly placed banners and in a test targeting a small sample of a few percent of users over the past few days. Both tests yielded similar results.

## 6. Communicating results

As we finish our work with data analysis, we're most likely already well acquainted with the problem, the data and the solution we have developed. While the solution may already seem obvious to you, it most likely is not so to others. That's why it's important, when finishing your work, to document the results you've obtained and communicate them extensively in a way that can be understood by those not involved in data analysis.

First, we clearly and comprehensibly communicate the value of the analysis performed and the patterns discovered in the data to those who are expected to use our results. Again, we find that graphic expressive language is very effective here and engaging for the audience - if used well.

We then arrange the collected information and results into a vivid story that has a beginning, development and conclusion. This mode of communication is another evolutionary adaptation. People evolved as social travelers. With the ability and imagination to recreate journeys based on a fellow traveler's story, we found it easier to evade dangers and find food. That's why we still enjoy and value stories: whether it's Homer's *Odyssey*, *King Arthur's Knights* or *Star Wars*.

Remember that by sharing your results in the form of a visual story, you're tapping into deeply ingrained natural mechanisms in humans. They help us effectively assimilate information at multiple levels of consciousness.

The skill of storytelling is currently experiencing a renaissance and is being applied in many areas of life. Data-driven storytelling has also become easier than ever thanks to the insights of scientists and anthropologists in the 20th century. We now know that it is crucial in communicating the results of analysis.

## Summary

The ***Process of Data Science*** or the process of investigating data has much in common with the journey and transformation of an epic hero.

First we hear the call of adventure: **problem** that needs solving. It quickly becomes apparent that it is mysterious. We set out to understand what it is and assemble a team of heroes with whom we'll face it.

**Defining the problem** we quickly arrive at the gateway to an unknown and dangerous land, after which nothing will be the same again. We know that there is no other way to complete our noble mission. We defeat or sneak past the guards of the gates of the unknown realm. We gain access to **serious data** where we hope to find the magical artifact necessary to complete the mission.

Stepping into a new world, we discover many obstacles and the temptations of illusory rewards. We befriend one of the guardians of the new world - a database programmer, who becomes our mentor as we **process and clean the data**. Together, we discover the many dangers and pitfalls of the new world, such as erroneous and missing data. Sometimes the programmer helps us open the gates to a locked chamber with an important but often overlooked set of data.

We overcome problems thanks to courageous friends, supporting us in exposing the illusory temptations of outliers, negligible correlations and false cause-and-effect relationships. They remind us of the true purpose of the expedition during **data exploration** - their variables and interrelationships. We are heading for a final life-and-death confrontation, the outcome of which is unknown. We know that many daredevils before us have tried and fallen. However, this doesn't deter us from another attempt - we fiercely **analyze the data**.

We use the weapons of knowledge we acquired earlier about the meaning of variables, the distribution of traps of empty and erroneous data. We harness all the cleverness and talent of posing questions and hypotheses with which we hope to get to the heart of the land and there, find the Holy Grail - a statistical model of the data or valuable information hidden in the data, which will become the key to solving the problem. It will become the Excalibur or the answer to the riddle of the Sphinx.

The treasures discovered, the journey traveled and the experiences gained change us irrevocably. When we return to the world we knew before, we find that it too has changed. Returning, we face one last challenge: **communicating the results** we have gained. The stories of the road we have traveled and the adversity we have overcome convince the ruler of our native land that the weapons we have acquired will offer a chance to win the battle against the evil sorcerer of the market standing at the borders. We have fulfilled the task entrusted to us.

The next task (to do on your own) will be to solve a quiz on the Data Science process.

### Good luck!
