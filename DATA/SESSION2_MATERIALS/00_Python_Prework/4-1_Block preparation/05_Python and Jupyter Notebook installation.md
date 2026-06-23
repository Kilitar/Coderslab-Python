# Python and Jupyter Notebook installation

Type: Article

For further work on the course you are going to need a configured computer. In this article we will go through the installation of the necessary software. From this article you'll learn:

- How to install and configure **Jupyter Notebook** in the `Anaconda` environment, which is going to be our default tool.
- How to use **Jupyter Notebook** in your daily work.

This part of the prework should take you about three hours (the installation time also depends on the parameters of your hardware).

This is a very important step: without it you will not be able to proceed with the rest of the course. **Do it as soon as possible to be able to carry out further tasks.

## Python

The Python programming language has been a standard in the work of a data analyst for some time. `Python` slowly supplants `R`: another language often used by data analysts. A great many add-ons have been developed for `Python` to support the work of analysts. We will learn the most popular ones during the course.

In the course we are going to use `Python` version `3.9`, that is installed together with the `Anaconda` environment.

## Anaconda

To simplify the configuration of our working environment we are going to use `Anaconda` – it is a distribution of the `Python` and `R` languages, used for scientific calculations and programming.

Together with the installation of `Acaconda` we will get not only `Python`, but also most of the additional libraries required for the course (you can find more on what libraries are and how to install additional ones in the: *Session 1 preparation -> Libraries*), and `Jupyter Notebook` – thanks to this, we can start learning at once!

## Installing Anaconda

The installation of `Anaconda` is nice and easy: it's nothing more than downloading and clicking your way through the installer:

### Download

1. Go to https://www.anaconda.com/
  ![anaconda](/presentations/DTL/en/4.9/W/M_04_S_01/09354648-ce48-453a-aa20-098d13238c84/student_content/5038a495-385e-4b72-b90f-5fdb28d04483/images/jupyter/anaconda.png)
2. The site should detect the operating system, so clicking on the **Download** highlighted above should be enough. Otherwise we can go the this website: [click](https://www.anaconda.com/products/distribution#Downloads) and choose the installer version (Windows, MacOS, Linux) manually.

### Installation

As we mentioned, the installation as a rule is simple and hassle-free, however, it is worth highlighting one step that may cause doubts:

![env_variable](/presentations/DTL/en/4.9/W/M_04_S_01/09354648-ce48-453a-aa20-098d13238c84/student_content/5038a495-385e-4b72-b90f-5fdb28d04483/images/jupyter/installer_env_path_selection.png)

**Here, we keep the default settings (see picture) and just click `Install`**. The details of these settings are not important to us at this point and we will not discuss them.

When the process is finished, we are ready to run `Jupyter Notebook`.

## Jupyter Notebook

This is a scientific editor that supports calculations in Python. Working with `Jupyter Notebook` is not unlike using any other text editor; one difference is that here we can take advantage of the organization of `cells`.

### First run

In order to run `Jupyter Notebook` we will use the following steps:

1. We open the installed anaconda as follows:
  
  
  
  - `Windows`: press the "Windows" key and type `anaconda`; program name is `Anaconda navigator`.
  - `MacOS`: press Command-space and type `anaconda`.
  - `Linux`: open the terminal and type the command: `anaconda-navigator`.
2. We should see the following window, where the tile with we are interested in, with a link to `Jupyter notebook` is marked:
  ![navigator](/presentations/DTL/en/4.9/W/M_04_S_01/09354648-ce48-453a-aa20-098d13238c84/student_content/5038a495-385e-4b72-b90f-5fdb28d04483/images/jupyter/anaconda_navigator.png)
3. In the tile we click the `Launch` button and moments later the window of the default browser opens with file explorer:
  ![welcome_screen](/presentations/DTL/en/4.9/W/M_04_S_01/09354648-ce48-453a-aa20-098d13238c84/student_content/5038a495-385e-4b72-b90f-5fdb28d04483/images/jupyter/jupyter_notebook_welcome_screen.png)

**Note**:

The browser by default shows the folder: `C:\Users\YOUR_USERNAME`. To open the notebook, navigate to the appropriate folder using the open window.

For example – if our notebook is on the Desktop, we click the `Desktop` link (see the picture above) and from there, select the notebook we want to use.

### Creating a notebook

Let's say we want to create a directory for the course in `Jupyter's` default view. We don't need to use the file browser at all for this, as it is also available here. To do so:

1. Click the `New` button on the right,
2. Click the `Folder` button in the drop-down list (as shown in the picture below)
  ![jupyter_new_folder_creation](/presentations/DTL/en/4.9/W/M_04_S_01/09354648-ce48-453a-aa20-098d13238c84/student_content/5038a495-385e-4b72-b90f-5fdb28d04483/images/jupyter/jupyter_new_folder_creation.png)

Depending on the language version of the system the folder may have a different name; for us it is `untitled folder`. Since the name is not very descriptive let's change it to, for example, `CodersLab-Course-Python-Data-Analysis`. To do this, you need to:

1. *Tick* the folder to change its name,
2. Click the `rename` button:
  ![folder_rename_01](/presentations/DTL/en/4.9/W/M_04_S_01/09354648-ce48-453a-aa20-098d13238c84/student_content/5038a495-385e-4b72-b90f-5fdb28d04483/images/jupyter/jupyter_notebook_rename_folder_01.png)
3. After that, a dialog box opens, where we enter the new name of the folder:
  ![folder_rename_02](/presentations/DTL/en/4.9/W/M_04_S_01/09354648-ce48-453a-aa20-098d13238c84/student_content/5038a495-385e-4b72-b90f-5fdb28d04483/images/jupyter/jupyter_notebook_rename_folder_02_en.png)
4. We confirm by clicking `rename` to complete the operation and then navigate in the browser to our working directory `CodersLab-Course-Python-Data-Analysis`. Here we are going to create our first notebook, just like we created the folder earlier: first click `New`, then `Python 3 (ipykernel)`, from the `Notebook:` section.
  ![new_file](/presentations/DTL/en/4.9/W/M_04_S_01/09354648-ce48-453a-aa20-098d13238c84/student_content/5038a495-385e-4b72-b90f-5fdb28d04483/images/jupyter/jupyter_notebook_new_file_en.png)
5. Now a new browser window is going to open with a notebook, and a notebook file: `Untitled.ipynb` is created in the working directory.
  ![first_glance](/presentations/DTL/en/4.9/W/M_04_S_01/09354648-ce48-453a-aa20-098d13238c84/student_content/5038a495-385e-4b72-b90f-5fdb28d04483/images/jupyter/jupyter_notebook_first_glance.png)
6. Congratulations! We have just created the first notebook! Now we are ready to learn how to use it and write our first program.

### Working with Jupyter Notebook

The most important element is the editing area. In this area, at the beginning, there is one cell. If you want to add another, click the icon with a plus sign.

Cells can have several types, we will be interested in two of them:

- `Code`, where `Python` code will be stored.
- `Markdown`, where you can write text, add lists, headings, etc. All this with the help of special syntax.

> You can find out more about Markdown from [Wikipedia](https://en.wikipedia.org/wiki/Markdown), or go through a quick tutorial on [this](https://www.markdowntutorial.com/) website.

The default type of a new cell is `Code`. To change its type, select it and choose another type from the drop-down list. Let's change the first cell and write a message there: `Welcome to the world of python!`

![jupyter_change_cell_type](/presentations/DTL/en/4.9/W/M_04_S_01/09354648-ce48-453a-aa20-098d13238c84/student_content/5038a495-385e-4b72-b90f-5fdb28d04483/images/jupyter/jupyter_notebook_change_cell_type.png)
![jupyter_markdown_01](/presentations/DTL/en/4.9/W/M_04_S_01/09354648-ce48-453a-aa20-098d13238c84/student_content/5038a495-385e-4b72-b90f-5fdb28d04483/images/jupyter/jupyter_notebook_markdown_cell_en.png)

Click the `Run` button (or press `Ctrl+Enter`) to *run* the cell:

![jupyter_markdown_02](/presentations/DTL/en/4.9/W/M_04_S_01/09354648-ce48-453a-aa20-098d13238c84/student_content/5038a495-385e-4b72-b90f-5fdb28d04483/images/jupyter/jupyter_notebook_markdown_cell_02_en.png)

At this point, another cell is automatically created. Its type is `Code`; in our case it is Python code. So let's enter there the simplest possible program written in Python:

``` 
print('Hello world!')
```

After running it, we should have notebook looking like this:

![jupyter_final](/presentations/DTL/en/4.9/W/M_04_S_01/09354648-ce48-453a-aa20-098d13238c84/student_content/5038a495-385e-4b72-b90f-5fdb28d04483/images/jupyter/jupyter_notebook_final_en.png)

Let's now save our notebook:

![jupyter_save](/presentations/DTL/en/4.9/W/M_04_S_01/09354648-ce48-453a-aa20-098d13238c84/student_content/5038a495-385e-4b72-b90f-5fdb28d04483/images/jupyter/jupyter_save_file_01.png)

A dialog box now opens, where we enter the name of the notebook:

![jupyter_save2](/presentations/DTL/en/4.9/W/M_04_S_01/09354648-ce48-453a-aa20-098d13238c84/student_content/5038a495-385e-4b72-b90f-5fdb28d04483/images/jupyter/jupyter_save_file_02_en.png)

> Note: At this stage of learning, we do not recommend deleting the name of the working directory, because later we may not be able to find the notebook.

### Jupyter Notebook interface structure

We have already learned about some of the notebook elements. Now, in the image below, we will show the most important elements of the user interface and their descriptions:

![jupyter_gui](/presentations/DTL/en/4.9/W/M_04_S_01/09354648-ce48-453a-aa20-098d13238c84/student_content/5038a495-385e-4b72-b90f-5fdb28d04483/images/jupyter/jupyter_notebook_gui_en.png)

## Additional information

- Jupyter Notebook is an easy and friendly work environment, especially at the beginning of learning Python. It is also possible to use other working environments such as `PyCharm` or`VSCode` but this is beyond the scope of this course. If you want to set up a different working environment, please contact your course mentor.
- We may notice that the notebook is opened in a browser. Using Jupyter Notebook, we don't have the option to automatically open files with the traditional *double-click*.

**We would like to remind you that if you have a problem with the installation or feel like you can't handle it on your own - don't be discouraged!** You can always reach out to your groupmates and mentor on Slack and ask for help.
