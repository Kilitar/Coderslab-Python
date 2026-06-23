# Virtual environment configuration

Type: Article

> **Note:**
> 
> This element is optional, but it is intended to emphasize the possibility of easy separation of the project from the global python environment.

## Introduction

Imagine a situation where you create a report using Python, everything works and refreshes periodically, but you go on a three-week vacation and during your time off you don't really want to think about work, especially the fact that you have to revise the report for 10 am on Friday.

You come up with the idea that you will give the source code to a person on your team and everything will work, after all, everyone works using Python. You go on vacation and at 9 o'clock on Friday you get a phone call - *It doesn't work!* (The author of this article had exactly this problem at the beginning of their work with Python ;) )

How could this problem have been avoided?

## We create a virtual environment

Probably after analyzing the problem you will find that it is a small thing - a version of the library, but wasted time on a Friday is not a laughing matter. This type of problem can be easily avoided by creating a virtual environment (i.e. *venv*) where we create a new instance of python, which is to be isolated and serve only this one task.

As it turns out, the matter can be reduced to 3 lines of code, and it saves a ton of problems.

### Environment folder for the project

To create a new Python environment, just use the following command:

``` 
python -m venv virtualenv
```

So we tell Python that it needs to use the venv module (built in from version 3.6) and create a new environment in a folder such as `virtualenv`.

> **Note:**
> 
> The environment created this way is going to be clean. i.e. there will be no libraries installed in it. If we need some. we should install them or use a file with information on what is needed (most commonly it would be `requirements.txt`).

### Creating requirements.txt file

This file contains information about libraries and their versions.
Sample content of the file:

``` 
SQLAlchemy==1.3.19
pandas==1.2.1
```

As you can see, here we have a list of libraries along with the information on which version we are using - for example, the SQLAlchemy library is version 1.3.19.

To generate the creation of such a file, just type the console command:

``` 
python -m pip freeze > requirements.txt
```

Then, the `requirements.txt` file will be created in the working directory.

### Recreating environment

Having a `requirements.txt` file, we can load its contents using the following command:

``` 
python -m pip install -r requirements.txt
```

Of course, if there is a file in the working directory of the console.

### Activate the virtual environment and work with it.

When we use `python` command, we are in fact using the global environment, that was - maybe even without us knowing about it - added to system variables. To activate the virtual environment, just enter the path to the Python file from the environment:

On Windows

``` 
project_path/virtual_env/Scripts/activate
```

On Linux / MacOS

``` 
source project_path/virtual_env/bin/activate
```

When we have an active environment, we will see a corresponding comment in the console:

``` 
(virtualenv) working/directory
```

We can simply type `pip install -r requirements.txt` and the project-wide required components get installed :)

### Jupyter installation

To use Jupyter Notebooks within the environment, you will need to additionally install additional modules:

``` 
(virtualenv) pip install jupyter
```

``` 
(virtualenv) ipython kernel install --name "CodersLab-Workshop" --user
```

This makes it possible to use the `CodersLab-Workshop` environment in the Notebook

![Kernel](/presentations/DTL/en/4.9/W/M_05_S_19/565fde0e-c939-4527-b240-819c317cac0b/student_content/f30cdf00-9904-440c-8558-2f23ba51cb48/./images/KernelSelection.png)
