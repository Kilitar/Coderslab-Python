# Running code outside Jupyter

Type: Article

Jupyter is an ideal tool for data analysts - it allows you to mix code, nicely formatted text and code output as well only run selected lines. Sometimes, however, we'll want to run code outside of Jupyter - somewhere on a server as an hourly to-do task, or even on a laptop, in the background, while we're having our morning cup of coffee.

To run Python code outside of Jupyter, you need to save it in a file with the `.py` extension. But it is not enough to simply change the extension of the Jupyter file from `.ipynb` to `.py` - these files are not written in the format that normal Python can execute.

`.py` files can be created in any text editor – `PyCharm`, `Atom`, `VS Code`, `Notepad++`, and even in the standard, Windows Notepad (the least comfortable, but still viable option).

To run such a script, issue a command in the console (command line):

``` 
python script_name.py
```

(less commonly `python3 script_name.py` – depends on the system).

If the script is in a folder other than the one currently indicated on the command line, specify its path:

``` 
python folder1/folder2/folder3/script_name.py
```

or go to the folder with the script first, and then run it:

``` 
cd folder1
cd folder2
cd folder3
python script_name.py
```
