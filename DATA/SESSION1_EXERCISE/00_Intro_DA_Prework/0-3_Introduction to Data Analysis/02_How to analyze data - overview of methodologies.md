# How to analyze data - overview of methodologies

Type: Article

Data can be analyzed according to different methodologies. We will compare three popular data analysis processes that are used by companies and in the community of data analysts and researchers:

- **CRISP-DM**, proposed in 1999 by a consortium implementing the European Union's strategic information technology initiative,
- **OSEMN**, presented in 2010 by Hilary Mason and Chris Wiggins in 2010.
- **Data Science**, described by AJ Goldstein in [this Medium post in 2017 roku](https://medium.com/the-mission/deconstructing-data-science-breaking-the-complex-craft-into-its-simplest-parts-15b15420df21), is the standard used throughout the **Introduction to Data Analysis** course.

We will outline the general assumptions of the above processes and summarize the differences between them. There will also be some historical background.

Before we go any further - a quick note. There is an important distinction between data analysts and data scientists. Our course will provide you with the basic skills to get on the path of **data analyst**. The role of a data scientist requires a good knowledge of statistics, databases and programming languages such as Python.

## Data Science process

The *Data Science* process is a modern take on the data analysis process that is being implemented in many companies, corporations and start-ups thanks to the revolution in data collection and processing brought about by the Internet and the digitization of many industry processes. The process consists of 6 steps that, by design, take place in iterations. Introduction of iterations stems from the challenges posed by data analysis; they're now supported by agile management methodologies that have become standard in IT companies.

Stages of Data Science process:

1. Framing the problem,
2. Collecting raw data,
3. Processing and cleaning data,
4. Exploring data,
5. In-depth data analysis,
6. Communicating results.

Simplifying even further, we can say that the first step is to understand the problem we have to solve. The importance of this step is illustrated by the following quote attributed to Albert Einstein:

> *"If I had 20 days to solve a problem, I would take 19 days to define it."*.
> — Albert Einstein

The next steps are acquiring and working with data, and finally presenting and communicating the results of the analysis. We will devote the largest part of the course to mastering these steps. But all the while, let's remember the importance of understanding and defining the problem before proceeding to solve it.

By framing the data analysis process in this way, we will also have the ability to map technical skills and competencies to each step of the process.

![dsp](/presentations/DTL/en/4.9/W/M_00_S_03/982fb032-d39c-4390-a4ff-0d46080bf0db/student_content/7165aa19-2011-475a-b2ff-bed69c482761/images/Data_Science_Deconstructed_loop.png)

## CRISP-DM

CRISP-DM is a process that was initially developed with the support of the European Union by a consortium of companies from various industries. The universality of the process is also reflected in its name: **Cross-industry standard process for data mining**. **Data Mining** was a popular term until the first decade of the 21st century. Even today, in many surveys among analysts and data scientists, this process is cited as frequently used.

There are 6 steps in this process as well:

1. Business understanding of the problem,
2. Understanding data,
3. Preparing the data,
4. Modeling (data),
5. Evaluation,
6. Implementation.

Also in this process, the first step is to define the problem, here viewed as a mutual understanding of the problem between the *business (**client**)* reporting the need and the analytical team that will develop the solution based on the available data. In the process illustration, this step is depicted as arrows in both directions - a stage of intensive dialogue to both understand the problem and understand the available data in the business context.

The next steps, which take place in a similar iterative loop, are data preparation and data modeling. By data preparation we mean formatting the data, correcting obvious errors and combining it with additional information that can add value to the modeling process. The data modeling step is most often understood as building statistical models or models based on machine learning, artificial intelligence or operations research methods.

> A *statistical model* of data is usually a very **simplified** mathematical representation of a data set that captures the statistical properties of the data set and is not an accurate description of it. However, statistical models are useful for both building an understanding of reality and making decisions. A linear regression (simple function) can be an example of a statistical model.
> 
> 
> 
> 
> ![Linear regression](/presentations/DTL/en/4.9/W/M_00_S_03/982fb032-d39c-4390-a4ff-0d46080bf0db/student_content/7165aa19-2011-475a-b2ff-bed69c482761/images/Data_model_simple_example.png)
> 
> 
> 
> 
> *A simple data model explaining the dependence of subjective happiness of a country's residents on the state of the economy (GDP per capita). The *linear* model explains about 62% of the variation in the data with the dependence of happiness on GDP. The happiness index here increases by 2.1 for each unit of GDP growth. Note, that there are countries with the same GDP whose happiness indices differ as much as twice, e.g. 3 and 6.*.

Evaluation is the step in which the model is verified with business area partners in regards to value delivery. If the value is confirmed, the model moves to the implementation stage.

It is also often said that the quality of the model is monitored after implementation. It turns out that as the process goes on, business conditions can change so much that they stop delivering value over time.

![Diagram of the CRISP-DM process](/presentations/DTL/en/4.9/W/M_00_S_03/982fb032-d39c-4390-a4ff-0d46080bf0db/student_content/7165aa19-2011-475a-b2ff-bed69c482761/images/CRISP-DM_Process_Diagram.png)

*Source:* [Wikipedia: CRISP-DM](https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining)

## OSEMN

The [OSEMN](https://towardsdatascience.com/5-steps-of-a-data-science-project-lifecycle-26c50372b492) process was proposed in 2010 on the wave of rapidly developing artificial intelligence and machine learning methods and the proliferation of big data in booming start-ups and maturing Silicon Valley internet giants such as Google and Facebook, where there was a decidedly less formal atmosphere of collaboration. This atmosphere is reflected in the name itself, which, despite being an acronym, is meant to sound similar to the English word *awesome*.

OSEMN is a five-stage data analysis process:

1. **O**btain — Acquiring data,
2. **S**crub — Cleaning data,
3. **E**xplore — Exploring data,
4. **M**odel — Modeling data,
5. i**N**terpret — Interpreting (results).

In this process, we don't actually address the aspect of understanding the problem or the business need. According to the Coders Lab team, this is its biggest shortcoming.

By interpreting the results, this process means using and applying the results in the context of the domain that the data came from (e.g., images published on the Internet) or the problem they it wants to solve (e.g., recognizing automatic images with pets in the photos).

This process is still useful for many adepts of data analysis. Although it doesn't include key elements from the perspective of delivering value to the business, it illustrates the key elements of working with data, showing that it is very difficult to simply "throw" data into an automation and get meaningful results. In its time, however, it was a process description that significantly brought the outline of the process of working with data to the broader community. This process was the first attempt at mapping the steps of data analysis with a variety of technical skills and emerging specialties.

## Comparison

Time for a brief summary of the processes mentioned. Look at the table below. Which steps of the analysis overlap in the various processes? An empty cell means that a particular process doesn't implement that stage. Before reading our brief summary of the differences, carefully examine the table:

![Process comparison](/presentations/DTL/en/4.9/W/M_00_S_03/982fb032-d39c-4390-a4ff-0d46080bf0db/student_content/7165aa19-2011-475a-b2ff-bed69c482761/images/Process_comparison_en.PNG)

The 3 processes described largely coincide and differ in details of how they describe the stages of working with data. The  authors of this course see the key differences in describing the data analysis process in:

- the importance of defining and understanding the problem under development,
- the meaning of communicating the results to stakeholders,
- less emphasis on the implementation stage due to greater integration of new technologies.

In addition, one can see how the processes presented reflect the nature of the environments in which they were created:

- CRISP-DM — formalized corporations before the popularization of agile management methods,
- OSEMN — Silicon Valley start-ups with several employees looking for a market niche.

The process we chose - *Data Science* - in our opinion best illustrates a good pattern of working with data in modern organizations - both small and large. It is also easy to translate it into the skills and competencies found in typical job postings for positions handling elements of or the entire data analysis process.
