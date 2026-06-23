# Introduction to programming

Type: Article

![Introduction to programming](/presentations/DTL/en/4.9/W/M_04_S_02/9df45195-8994-4331-aafb-3655850f9a5c/student_content/e7e85bb4-0df1-469e-8681-2b0dec1a2a9c/images/wprowadzenie_do_programowania.jpg)

## Introduction

In this article we will explain a few basic concepts of programming. Among others,
we will try to explain:

- what a computer is
- what we call source code
- what a computer program is
- what a compiler and interpreter are
- what distinguishes a markup language from a programming language
- what an algorithm is and how to represent it as a flowchart
- what pseudo-code is

---

## What do we call a computer?

**Computer** (formerly: electronic brain, electronic digital machine, mathematical machine)

- an electronic machine designed to process information that can be stored as a sequence of digits or
  a continuous signal

Although mechanical calculating machines have existed for many centuries, computers in the modern sense did not appear until
mid-20th century, when the first electronic computers were built. They were the size of large rooms
and consumed several hundred times more energy than modern personal computers (PC).
At the same time, they had billions of times less computing power.

Today, small computers can even fit in a watch and are powered by a battery.
Personal computers have become a symbol of the computing age, and most identify them with "computers".
The most numerous calculating machines are embedded systems that control a wide variety of devices - from MP3 players
and toys to industrial robots.

What distinguishes modern computers from all other machines is that they can be **programmed**,
which means that a list of instructions can be entered into the computer's memory, and those instructions can be executed at another time.

##### Source: [https://en.wikipedia.org/wiki/Computer](https://en.wikipedia.org/wiki/Computer)

![First computer](/presentations/DTL/en/4.9/W/M_04_S_02/9df45195-8994-4331-aafb-3655850f9a5c/student_content/e7e85bb4-0df1-469e-8681-2b0dec1a2a9c/images/eniac.jpg)

##### One of the first computers - "Eniac" from 1946. You can read about it here:: [https://en.wikipedia.org/wiki/ENIAC](https://en.wikipedia.org/wiki/ENIAC)

---

## What is a programming language?

By definition:
**Programming language** - a set of rules that define when a sequence of symbols forms a computer program
and what computations it describes.

##### Source: [https://en.wikipedia.org/wiki/Programming_language](https://en.wikipedia.org/wiki/Programming_language)

How to understand it?

- A programming language is a set of rules that describe how instructions should be constructed so that a computer understands them.
- It is distinguished from natural language by such features as precision and lack of ambiguity.

**For example**: When we speak, we sometimes make various linguistic errors. Nevertheless, the other person is able to understand us.
This is not possible when communicating with a computer.

![Programming language](/presentations/DTL/en/4.9/W/M_04_S_02/9df45195-8994-4331-aafb-3655850f9a5c/student_content/e7e85bb4-0df1-469e-8681-2b0dec1a2a9c/images/jezyk_programowania_en.png)

---

## Source code

**Source code**  is a record of a computer program using a specific programming language. It describes the operations
a computer should perform on the collected or received data. Source code is the result of the programmer's work
and allows to express the structure and operation of a computer program in a human-readable form.
It is usually saved in a text file, but it may also occur in the form of code fragments published
in newspaper articles or books.

Before execution, source code must be translated into the resulting code in a process called compilation.
It consists in converting the code into the resulting code, usually machine code, which is the only possible version
to be executed by the processor. Another method is the real-time execution ("on the fly") of a program written in
source code using an interpreter or compiler which compiles code fragments on the fly.
The term "executing source code" is equivalent to executing a program created from that code.

##### Source: [https://en.wikipedia.org/wiki/Source_code](https://en.wikipedia.org/wiki/Source_code)

![Source code](/presentations/DTL/en/4.9/W/M_04_S_02/9df45195-8994-4331-aafb-3655850f9a5c/student_content/e7e85bb4-0df1-469e-8681-2b0dec1a2a9c/images/kod_zrodlowy.jpg)

##### **Margaret Hamilton**, lead software engineer in the Apollo project. Next to her is the printed source code for the **AGC** (Apollo Guidance Computer), the digital computer installed in the modules aboard Apollo.

In other words, source code is a record of the solution to a problem using a programming language.
Source code is both human-readable and understandable for a computer.

#### Example:

``` python
def add(a, b):
    return a + b

print(add(2, 2))
```

##### A code snippet written in Python that adds two numbers.

---

## Computer program

![Computer program](/presentations/DTL/en/4.9/W/M_04_S_02/9df45195-8994-4331-aafb-3655850f9a5c/student_content/e7e85bb4-0df1-469e-8681-2b0dec1a2a9c/images/program_komputerowy.jpg)

A computer program (also called computer software or application) is a set of commands
that have been written by a programmer (specialist) in a programming language.
It includes an ordered sequence of characters – an order of operations that the computer should perform.
The program must be loaded into the computer's RAM before it can be run.

##### Source: [https://en.wikipedia.org/wiki/Source_code](https://en.wikipedia.org/wiki/Source_code)

What is the difference between **source code** and a **computer program**?
Source code is just a record of a program in a particular programming language. You can print it out on a piece of paper
and nothing will happen. A program is something more. It is source code that can be run on a computer using
a compiler or interpreter.

---

## Compiler and interpreter

These concepts have appeared several times before. What are they?

A **compiler** is a program that translates the source code of a given programming language into the resulting code
(i.e. equivalent code in another programming language). This process is called compilation. In programming,
compilation is most commonly understood as translation of source code (created by a programmer) into machine code
(ready to be run by a computer).

An **interpreter** analyzes the source code and immediately runs the analyzed fragments. This has certain consequences.
The execution of the program using the interpreter is slower and takes more memory than running the compiled code.
On the other hand, the time-consuming process of compilation is omitted here.

During this course you will learn the **Python** language, which is an interpreted language.

---

## What is an algorithm?

![Algorithm](/presentations/DTL/en/4.9/W/M_04_S_02/9df45195-8994-4331-aafb-3655850f9a5c/student_content/e7e85bb4-0df1-469e-8681-2b0dec1a2a9c/images/algorytm.png)

An algorithm is a kind of instruction. It is a finite sequence of clearly defined steps necessary to perform a certain type of task.
In other words, it is a course of action leading to the solution of a problem.

##### Source: [https://en.wikipedia.org/wiki/Algorithm](https://en.wikipedia.org/wiki/Algorithm)

Where do we encounter algorithms in everyday life?
For example, an algorithm might be:

- a recipe,
- instructions for assembling Ikea furniture,
- the way to tie a tie
- an instruction to sort a list of numbers.

---

## Flowchart

A flowchart is a tool used to represent successive steps in a designed algorithm - i.e. a graphical representation of instructions.
It is a diagram in which a procedure, system or computer program is represented by described
geometric shapes connected by vectors (arrows) according to the order of the activities
based on the chosen algorithm of solving the problem.

##### Source: [https://en.wikipedia.org/wiki/Flowchart](https://en.wikipedia.org/wiki/Flowchart)

![Flowchart](/presentations/DTL/en/4.9/W/M_04_S_02/9df45195-8994-4331-aafb-3655850f9a5c/student_content/e7e85bb4-0df1-469e-8681-2b0dec1a2a9c/images/schemat_blokowy_en.png)

##### A flowchart for the mathematical operation of factorial.

The following elements can be distinguished in the diagram (see image above):

- **rounded rectangle** − indicates the beginning or end of the diagram,
- **arrow** − indicates relations and their direction unambiguously,
- **rhomboid** − describes input/output operations,
- **diamond** − represents selection instructions,
- **rectangle** − contains all other operations.

## Pseudocode

**Pseudo-code** is a way of writing an algorithm, which retains the structure characteristic of the code
written in a programming language code, and resigns from strict syntax rules in favour of simplicity and readability.
Pseudocode does not contain implementation details (such as variable initialization, memory allocation, etc.),
It also often omits a description of the operation of subprocedures (if it should be obvious to the reader),
on the other hand, non-trivial steps of the algorithm are described with the help of mathematical formulas or natural language sentences.

There are currently no widely accepted standards for writing pseudocode.
Most authors use an ad hoc adopted syntax, often relying on the syntax of existing programming languages
(Pascal, ALGOL, C).

##### Source: [https://en.wikipedia.org/wiki/Pseudocode](https://en.wikipedia.org/wiki/Pseudocode)

In other words, **pseudocode** is another way to describe an algorithm. It has no rigid rules.
It is mostly a combination of:

- mathematical operations,
- control instructions,
- variable assignment instructions,
- natural language.

#### Example:

``` 
function factorial(n):
  i = 1
  result = 1
  as long as i <= n:
    result = result * i
    i = i + 1
  return result
```

##### A function that calculates factorial described using pseudocode.

---

## Algorithms are independent of a programming language!

- An algorithm is a way to solve a particular problem.
- Any algorithm can be written in pseudo-code.
- The pseudo-code of an algorithm can be translated into virtually any programming language.

## Comparison of programming languages

Below you can see how basic commands differ in popular programming languages.

| Python | PHP | C++ | What does it do? |
| --- | --- | --- | --- |
| print("hello") | print("hello"); | printf("%s", "hello"); | Prints "hello" to the screen |
| arr = [3,2,1] | $arr = array(3,2,1); | int arr[ ] = {3,2,1}; | Creates an array (list) of data: 3,2,1 |
| arr.sort() | sort($arr); | std::sort (arr, arr + 3); | Sorts the given array (list) with data |
| if condition:    operation | if (condition) {    operation;  } | if (condition) {    operation;  } | Performs the given operation if the condition is met |

## Summary

After reading the article you know the basic concepts of programming. Now you know now what the difference
between code and pseudo-code is. Terms like compiler and interpreter are no longer strange to you.

If you didn't understand something, relax and read the paragraph about it again, looking at the attached links
with sources.
