# CSV files

Type: Article

**.csv** files can be created by virtually any spreadsheet: Microsoft Office Excel, LibreOffice Calc, etc. Their advantage (sometimes a disadvantage) is simplicity: a **.csv** file read by an ordinary word processor looks like this:

``` 
John,Doe,120 jefferson st.,Riverside, NJ, 08075
Jack,McGinnis,220 hobo Av.,Phila, PA,09119
"John ""Da Man""",Repici,120 Jefferson St.,Riverside, NJ,08075
Stephen,Tyler,"7452 Terrace ""At the Plaza"" road",SomeTown,SD, 91234
,Blankman,,SomeTown, SD, 00298
"Joan ""the bone"", Anne",Jet,"9th, at Terrace plc",Desert City,CO,00123
```

One line is one spreadsheet row, individual cells are separated by commas, and where necessary, cells are surrounded by quotation marks.

Python has an entire module dedicated to such files, called: `csv`.

It should also be said, that Python can iterate a file (read it line by line, e.g. in the `for` loop); `open()` function can also be passed a `newline` argument: its value will be used as the character of the new line at the end of each line in the file. A requirement of the `csv` module it pass an empty string as a `newline` argument when opening files:

``` python
with open('my_csv_file.csv', newline='') as my_file:
    # ...
```

## Reading .csv files

The easiest way is to use the `reader` function from the `csv` module. This function requires an argument in the form of an open file, and returns an object that can be queried for subsequent lines - lists of strings will be returned - each list is one row, and the strings are the cells in that row:

``` python
import csv

with open('addresses.csv', newline='') as my_file:
    addresses = csv.reader(my_file)
    for line in addresses:
        print('Line from file:', line)
```

Result:

``` 
Line from file: ['John', 'Doe', '120 jefferson st.', 'Riverside', ' NJ', ' 08075']
Line from file: ['Jack', 'McGinnis', '220 hobo Av.', 'Phila', ' PA', '09119']
Line from file: ['John "Da Man"', 'Repici', '120 Jefferson St.', 'Riverside', ' NJ', '08075']
Line from file: ['Stephen', 'Tyler', '7452 Terrace "At the Plaza" road', 'SomeTown', 'SD', ' 91234']
Line from file: ['', 'Blankman', '', 'SomeTown', ' SD', ' 00298']
Line from file: ['Joan "the bone", Anne', 'Jet', '9th, at Terrace plc', 'Desert City', 'CO', '00123']
```

## Writing to file

Writing to a csv file is equally simple: the `csv` module provides a `writer` function. Similarly to reading, the `writer` function expects an open file: this time in the `write` mode:

``` python
import csv

with open('users.csv', 'w', newline='') as my_file:
    writer = csv.writer(my_file)
    writer.writerow(['John', 'Connor', 'jconnor@mywebsite.org'])
    writer.writerow(['Anna', 'Newman', 'anewman@mywebsite.org'])
```

Such a file, when saved, has content understandable for all spreadsheets:

``` 
John,Connor,jconnor@mywebsite.org
Anna,Newman,anewman@mywebsite.org
```
