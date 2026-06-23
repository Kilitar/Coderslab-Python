# Introduction to Python

Type: Article

![Introduction to Python](/presentations/DTL/en/4.9/W/M_04_S_02/424b6cb0-052d-481a-a9da-55d8d5ede09d/student_content/813410f1-5b9a-4f1d-82fe-ac63f6990b98/images/wprowadzenie_do_jezyka_python.jpg)

## Introduction

In this article we will discuss Python programming basics,
Among other things, you will learn:

- how the Python language was created and what are its main uses,
- how you can run code written in Python,
- what an interactive shell is and how to use it.

You will learn basic instructions responsible for input/output operations
(retrieving data from the user and displaying it on the screen).
In addition, we will create and run our first Python program together.

---

## How was Python created?

![Monty Python](/presentations/DTL/en/4.9/W/M_04_S_02/424b6cb0-052d-481a-a9da-55d8d5ede09d/student_content/813410f1-5b9a-4f1d-82fe-ac63f6990b98/images/monty_python.jpeg)

#### History:

Let's go back to 1991 for a moment.
The Soviet Union has just collapsed, Metallica released an album known as the Black Album, Linus Torvalds announced the creation of Linux, Ed Sheeran (the singer) was born, and the film "Dances with Wolves" starring Kevin Costner won an Academy Award.

In the same year, the **Python** language, whose main creator was **Guido van Rossum**, saw the light of day. It was created as a successor to the **ABC** language developed at the **CWI** (Centre for Mathematics and Computer Science in Amsterdam). Van Rossum is the leading creator of Python, although significant contributions to its development have come from others. Because of the key role van Rossum has played in making important design decisions, he is often referred to as the "Benevolent Dictator for Life" (BDFL).

##### Source: [https://en.wikipedia.org/wiki/Python](https://en.wikipedia.org/wiki/Python)

> Benevolent Dictator for Life (BDFL) - an informal title given to people
> involved in the Open Source movement, who are widely respected by the community and have made significant contributions to the development of
> specific fields. The dictator gives, by the power of their unquestionable authority, the general directions of action
> and makes key decisions when consensus is difficult or impossible to achieve.
> 
> 
> 
> 
> ##### source: [https://en.wikipedia.org/wiki/Benevolent_Dictator_for_Life](https://en.wikipedia.org/wiki/Benevolent_Dictator_for_Life)

#### Name:

The name of the Python language has nothing to do with a snake. It comes from a comedy program aired in the
1970s: "Monty Python's Flying Circus". The creator of Python, who was a fan of the show, was looking for a name that was short, unique and somewhat mysterious, and thought this one was great.

Python is a **high-level** language. It is a type of language whose syntax and keywords are designed to make it as easy as possible to
facilitate human understanding of the program's source code, thereby increasing the level of abstraction and distancing itself
from hardware nuances. This distancing allows the programmer to focus on solving complex problems, without focusing on hardware issues.
This is done at the expense of speed or increased compilation time in the case of compiled languages.
The term that a language is a high-level language, is relative.
For example: C language, compared with assembler, can be considered a **high-level** language.
In comparison with Python, it will be considered  a **low-level** language. For a more comprehensive explanation,
see: [https://www.webopedia.com/definitions/high-level-language/](https://www.webopedia.com/definitions/high-level-language/) and  [https://www.geeksforgeeks.org/difference-between-high-level-and-low-level-languages/](https://www.geeksforgeeks.org/difference-between-high-level-and-low-level-languages/).

#### Basic information about Python:

- developed under an open source license by the Python Software Foundation,
- at the moment version 3.x is used in projects (the last version 2.7 lost support at the end of 2020 and is on the verge of extinction),
- used in web application development, scientific, big data, machine learning, test writing, automation
  and many others.

#### Examples of websites and companies using Python:

- Wikipedia
- Google
- Yahoo!
- CERN
- NASA
- Facebook
- Amazon
- Instagram
- Spotify
- Reddit (mostly written in Python).

These are just some examples of the biggest players. Python is currently one of the most popular programming languages.
According to a report from GitHub analyzing open source repositories (data from Q4 2019), code written in Python accounts for 17.93% of the entire codebase.
This puts Python in the 1st place in terms of popularity.
You can see here how the popularity of different programming languages changes: [https://madnight.github.io/githut/#/pull_requests/2021/4](https://madnight.github.io/githut/#/pull_requests/2021/4).

---

## Running Python code

At the outset, it should be said again that Python is a programming language. This means that it is nothing more than a set of rules that let us write what exactly the computer should do for us. To run a program written in Python, we need to use an **interpreter**. This is a special program that will read our code, and execute it. At the moment, there are many interpreters, or ways in which we can run our Python code. They are:

1. Running with an installed interpreter through a system command,
2. Running the code in an interactive Python shell,
3. Running the code from within Jupyter Notebook.

During the course we will only use `Jupyter Notebook`, which is considered the most convenient for data analysts. However, it is worth mentioning that the most common way is the first one. It is usually used to run console programs.

The second one: interactive Python shell is the basic method that lets us enter Python command directly in the terminal [or on some websites](https://replit.com/languages/python3) – type: print('Hello, Python!') and run the code) and to immediately see the result of the line of code. It is a very convenient tool to quickly check the correctness of the code or its exact behavior. Unfortunately, it is not convenient for writing larger solutions, because it does not allow you to easily modify code once it has been run.

The last of the methods we described, Jupyter Notebook, is considered the most convenient for data analysts to work with. It is a combination of a development environment with a built-in interactive shell. It combines the ability to create code line by line, like an interactive shell - with the ability to create larger, more complex projects. It also gives you the ability to easily interweave the code you create with notes, written in normal text. This lets you create a program that is interlaced with data, analysis and observations.

If you want to learn more about why Jupyter Notebook is so popular, we recommend the article on the subject in [Nature](https://www.nature.com/articles/d41586-018-07196-1).
