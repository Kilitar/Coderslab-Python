# DataGrip

Type: Article

During the course, we recommend using the DataGrip editor. It gives you a lot of possibilities, and at the same time it is easy to use - so you will be focusing on the code and not "fighting" with the editor. To begin with, DataGrip can be installed in a 30-day trial version. Before the course starts, you will get a free license for 7 months, which must be activated after the trial period expires.

## DataGrip Installation — Windows

1. Download the newest version of the program from [this website](https://www.jetbrains.com/datagrip/download/#section=windows) and run the downloaded file.
2. Follow the information that appears on the screen.

## DataGrip Installation — Linux

1. Download the newest version of the program from [this website](https://www.jetbrains.com/datagrip/download/#section=linux). Unzip the downloaded archive to your home directory.
2. Open terminal (Ctrl+Alt+T) and use the command:
  
  
  
  ``` 
  cd path/to/directory
  ```
  
  
  
  to navigate to the directory where the archive was unzipped.
3. Using the command:
  
  
  
  ``` 
  cd bin
  ```
  
  
  
  go to the `bin` directory.
4. Execute the command:
  
  
  
  ``` 
  ./datagrip.sh
  ```
  
  
  
  **DataGrip** will be launched.

## For all OS versions

Activate the free 30-day version, at the end of the trial period you will receive a code from the mentor to extend the license.

## DataGrip basics

### How to create a new project?

- To set up a new empty project open the tab: `**File > New > Project...**`.
- Choose project location and name — by default the projects are saved in the home directory subfolder: `**DatagripProjects**`.
- Click the `**Create**` button.
- We have just created a new project.

### How to open an existing project?

- To open an existing project go to `**File > Open > Project...**`.
- We choose the location of the project.
- Click the `**OK**` button.

### How to create new query files?

- Start from creating the necessary files (if you are working on a new project). To do so we first right-click an empty field of our project and select `**New**`.
- We can choose the type of file to create by selecting the appropriate position from the list or create any type of file by clicking `**New > File**` and adding an appropriate extension to its name.

### How to view the database structure?

- After connecting to the database correctly (explained in a separate article), you should see only one *information_schema* (in a nutshell, it contains information about the objects in the database). To display additional information, such as for example where our data is, next to our database icon click `**all schemas**` or just the one we are interested in.

![schema selection](/presentations/DTL/en/4.9/W/M_02_S_01/b000d210-04ad-428c-97c2-8c1b1f4ac13c/student_content/1fc8cbde-de41-447a-b484-51831579ae45/./images/schema_view.png)

![schema selection after](/presentations/DTL/en/4.9/W/M_02_S_01/b000d210-04ad-428c-97c2-8c1b1f4ac13c/student_content/1fc8cbde-de41-447a-b484-51831579ae45/./images/schema_view_after_selection.png)

### How to start autosaving files?

DataGrip can automatically save your files after a certain period of inactivity - with this option you minimize the likelihood of losing your work. The auto-save feature can be very useful.
To enable it, you need to:

- Open DataGrip settings: `**File > Settings**` and the `**System Settings**` tab.
- select `**"Save files automatically if application is idle for N sec."**`
- set the appropriate number of seconds - default: **15**.

### Documentation

DataGrip has extensive documentation and a quick tutorial *For Beginners*, which is worth reading: [https://www.jetbrains.com/help/datagrip/meet-the-product.html](https://www.jetbrains.com/help/datagrip/meet-the-product.html)

On the YouTube channel of JetBrainsTV (creators of DataGrip) you can find many useful tutorials (not only for beginners):

[https://www.youtube.com/watch?v=Xb9K8IAdZNg&feature=youtu.be](https://www.youtube.com/watch?v=Xb9K8IAdZNg&feature=youtu.be)

### IDE - why do we need a specialized text editor?

In fact, you can write code in any text editor. Even the ordinary notepad is suitable for this.

However, a good editor will color the syntax, allow you to easily switch between files and speed up your work. Some editors are also capable of inserting ready-made pieces of code (called snippets) or autocomplete as we type (although the autocomplete results cannot always be relied upon).

## Summary

We learned about the query editor, which will be used throughout the course. We encourage you to do the subsequent exercises included in the prework using it, so that you become accustomed to it before the course begins.

Next, we will connect to our database.
