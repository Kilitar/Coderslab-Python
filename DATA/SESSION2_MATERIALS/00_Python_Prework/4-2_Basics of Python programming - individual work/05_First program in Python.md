# First program in Python

Type: Article

After learning about the interactive shell, which is the simplest way we can run Python code, it's time to write a more complicated program.

In this article, we will show the code of a working program and discuss it in detail. We'll explain what comments are and why we should use them to describe our code.

The program to be shown may seem complicated. Especially if this is your first encounter with programming - it may seem incomprehensible. However, the entire logic of how the program works will be discussed in detail here. In the following sections of the prework, all the used syntax elements will also be thoroughly discussed and practiced. Over time, you will find it easier and easier to work with Python code.

## The problem

Recently, we were approached by a friend of ours - a school English teacher. He spends a great deal of time evaluating the tests he gives in his classes. He came up with the idea that some of the tests, which have multiple choice questions, could possibly be graded automatically. So he asked us to help him implement this idea.

We will receive the following data for our program:

- A list with the correct answers,
- A list with the answers of one of the students.

Our friend expects the program to show him information about how many answers the student has given correctly.

## Problem solution

The problem presented here does not seem too difficult. If we were working with a human it would be enough to tell them to see how many items in both lists (the one with the correct answers and the one with the student's answers) are the same. In the case of explaining how to solve the problem to a computer, the situation is more complex. So, let's work out the problem of comparing two lists - step by step:

1. We need to store a list with correct answers and a list with student's answers in computer memory;
2. We have to create a space in the computer memory where we will store the number of correct answers;
3. We need to take the elements in the first position of both lists and compare them with each other. If:
  a. elements are identical we increase the number of correct answers by one,
  b. elements are different we do not do anything;
4. We repeat point 3 for the elements in position 2, 3, 4, .... until the end of the lists.

Such a description is suitable for presentation to a human, but the computer will have problems with it. Especially with the last point, that is, repeating the steps until the end of the list. We must therefore extend our solution:

1. We need to store a list with correct answers and a list with student's answers in computer memory;
2. We have to create a space in the computer memory where we will store the number of correct answers;
3. We must find out how many elements does the list with correct answers have and store this information in computer memory;
4. For each integer in the range from 0 to the length of our list, let's do the following:
  
  1. let's save the number we are currently working on as `i` in computer memory,
  2. let's take the elements from the n-th position of both lists and compare them to each other. If:
    a. elements are identical we increase the number of correct answers by one,
    b. elements are different we do not do anything,

Now the description will be more understandable for the computer. The only thing that may be unintuitive is the fact that in the case of going through the list, we count from 0. In programming, it is accepted that the first element of the list is at the number 0 - this should be remembered and assumed that it is simply so.

## Program code

Below is the code with the solution to the problem. In the zip file with the exercises there is also a Jupyter Notebook file with the solution.

``` python
# Variables initialization with data
key_answers = ['a', 'b', 'a', 'c', 'd', 'a', 'c', 'a', 'b']
student_answers = ['b', 'b', 'a', 'a', 'd', 'a', 'd', 'a', 'b']

# Variables needed for program logic
good_answers = 0;
answers_length = len(key_answers)

# for loop iterating through both lists
for i in range(answers_length):
    # We check if elements on i-th position are the same
    if(key_answers[i] == student_answers[i]):
        # If they are the same we increment good_answers
        good_answers = good_answers + 1

# We add 1 here because computer indexes from 0.
print(f"Checked {i+1} question")

print(f"Student got {good_answers} answers right out of {answers_length} questions")
```

Run this program and see if the result matches. Change a few values in the answer lists (remembering not to remove any commas or apostrophes - the program won't run correctly without them) and run it again. See if the result has changed as expected.

Let's discuss the operation of this program line by line:

1. All lines of code starting from the `#` character are *comments* — Python does not read them. These are used only to leave notes for ourselves or others who will work with our code. You will find out more about the comments later in the article.
2. In lines 2-3 we *define variables that hold* the correct answers and the student's answers, respectively. In a normal program, we would take such information from the user, from a file or from other data sources. We simplify the program a bit and enter the necessary information manually.
3. In lines 6-7 *we create the variables needed for the correct operation* of our program. `good_answers` variable is going to contain the number of correct answers and `answers_length` the total number of answers to tasks. `good_answers` gets the starting value of `0` – at the moment we don't know anything about correct answers yet. To `answers_length` we assign the length of the list — we get it using `len(answers_length)`. What if we entered the length of the list manually as well? It would work now, but it would cause the program to malfunction when the number of questions on the exam changes.
4. Lines of code from 10 to 15 are a *loop*. This is a special syntax that allows us to repeat certain actions - a certain number of times. This loop will count down from 0 to n, where n is the length of the list minus 1. Additionally, inside the loop (that is in lines 11-14) we will have access to the `i` variable that holds the number of the iteration (on first iteration `i` equals 0, then `i` equals 1, etc.).
5. Line 12 is a *conditional check*. With it, a piece of code will run only if an assumption is met. The assumption is to compare the i-th element of the list with the correct answers with the i-th element of the list with the student's answers. If answers are identical (checked with `==`), we go to the next line of code. If not, we will jump to line 17 of the code.
6. In line 14 (runs only when the student's answer is correct) we increase the number of `good_answers` by 1.
7. Line 17 is a simple display of text with information about checking the answers to the question. What's interesting, in the text we print, we also use the `i` variable to know which question we are dealing with.
8. In line 19, we display the student's final score on the screen.

> In the text above, you may find the statement "i-th element of the list". It is a very popular expression that defines the list element on the `i`-th position, where the value of `i` is updated with every iteration of the loop.

Note that in Python it is very easy to see which line a loop or conditional statement goes to. This is determined by readable "indentation" in the code - that is, moving the beginning of the line by a given number of spaces. Code readability is one of the reasons Python is so easy to learn.

If you're having trouble understanding exactly how the code works, copy the code above and use the [website](http://www.pythontutor.com/visualize.html), that will guide you step by step through how the program is executed.. Concentrate on understanding what the stages of program execution are.

## Comments

In every programming language we have the ability to comment on our code. Comments are short pieces of text
that help other programmers understand our code. They are ignored by the interpreter and do not affect the execution of the
program.
We should not overuse comments. Our code should be as readable as possible without them.
In Python, we also have the ability to write documentation (a document with description) for variables, functions and classes, which is a better practice than writing
comments because it does not reduce code readability. We will discuss documentation in more detail later in this course.

Comments in Python start with the `#` character. A comment can start at the beginning of a line,
or it can be placed after a code fragment.

##### Example:

``` python
# This is a comment.

print("Hello World!") # This is a comment for instruction.
```

Comments that are placed after the code should be separated from it by **two spaces**.
If you use one space, the code will work, but this is considered bad practice (it contradicts PEP8 convention).

In case of multi-line comments, start each line with a `#` character.

##### Example:

``` python
# This is
# a multiline
# comment.
```

---

## Summary:

We managed to run our first code in Python (and it's more complicated than displaying "Hello world"!) and immediately automated some of our friend's work. This is a nice start to continue learning programming. Additionally:

- We went from solving a problem understandable to a human, to a solution understandable to a computer - which has to be much more detailed.
- We showed how a loop (it repeats execution of the same code several times) and a conditional expression (it runs or bypasses the code depending on the result of the comparison) work.
- We showed the importance of indentation in Python (it shows how far a loop or conditional expression goes).

If any part of our program is not clear to you - don't worry. All the elements used here will still be explained in detail in later parts of the prework.
