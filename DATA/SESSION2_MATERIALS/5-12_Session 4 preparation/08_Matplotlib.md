# Matplotlib

Type: Article

## Matplotlib package

There are many additional Python libraries used to create static and dynamic visualizations, but our main focus in the next class is going to be the [Matplotlib](http://matplotlib.org/) package and tools that work with it.

Matplotlib was developed to create mostly two-dimensional graphs suitable for publication. This project was launched in 2002 by John Hunter. He wanted to create a pythonic interface for creating graphs that resembled the interface known from the MATLAB environment. The Matplotlib and IPython developer environments worked together to make interactive charting as simple as possible from the IPython shell, and now the Jupyter Notebook. The Matplotlib package supports a variety of graphical user interface back-ends for all operating systems, in addition to the ability to export visualizations to all popular vector and raster graphics formats (PDF, SVG, JPG, PNG, BMP, GIF, etc.).

## Matplotlib package – installation and first plot

The Matplotlib package should already be installed with the installation of Jupyter Notebook. But if it isn't, we can install it easily using `anaconda-navigator`. We install this library like all the libraries we have used so far in the Environments tab.

To generate a graph, for batch data, we really only need an array of numbers.

Example:

``` python
import matplotlib.pyplot as plt

plt.plot([0, 2, 4, 6])
plt.show()
```

First, we import a part of the Matplotlib library called `pyplot` responsible for generating plots (charts). For ease of use later, let's just call it `plt`.
In the next step we are going to use the `plot()` method passing as a parameter the list of numbers we want to plot on the chart; they will be automatically assigned to the arguments in the order of: `0, 1, 2..` on the plot we generate. Next, we call the `show()` method.

## Ways to display graphs

The Matplotlib library provides us with many different ways to display the prepared graphs. This is related to the so-called backends. In the case of Matplotlib, a backend is a part of the library that is responsible for all the tedious operations responsible for drawing the graph. The types of backends implemented in Matplotlib are many, for example:

- Responsible for displaying charts in GUI (graphic user interface) applications,
- Responsible for displaying charts on websites,
- Responsible for displaying in Jupyter Notebook (interactive),
- Responsible for displaying in Jupyter Notebook (static),

and many, many others.

Backends will not be part of the course, as they are advanced and the ability to create them is unlikely to be useful in an analyst's work. We mention them here, as the last two may be useful.

> Note: Once a chart is displayed, it is usually impossible to change the backend anymore. If you see the message `Cannot change to a different GUI toolkit: xxx. Using yyy instead.`, it means that the backend has not been changed.
> It is then best to close the Jupyter notebook (via "File -> Close and Halt") and open it again.

### Non-interactive plots

The simplest way (automatically used in Jupyter Notebook) causes the chart to be displayed in a non-interactive form. That is, we simply display a graphic with our chart under the cell with our code:

``` python
import matplotlib.pyplot as plt

x = [0,1,2,3,4,5]
y1 = [0,1,2,3,4,5]
y2 = [0,1,4,9,16,25]

plt.plot(x, y1, label='Plot 1')
plt.plot(x, y2, label='Plot 2')  
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
```

Result:
![Non-interactive plot](/presentations/DTL/en/4.9/W/M_05_S_12/ec7b18ca-040a-43c6-a158-1e86324217fc/student_content/4046e52d-8e27-4805-a166-7f1345da201e/./images/wykres-nie-interaktywny_en.png)

### Interactive plots

In Jupyter notebook we also have the ability to create interactive charts. They allow us to move the chart, zoom in and out. Additionally, they give us the ability to easily save the chart to a file in PNG format.

To display interactive charts, we need to enter the following command before executing the script:

``` 
%matplotlib ipympl
```

Commands starting from `%` are so-called magic Jupyter commands. You can find out more about them from the  [documentation](https://ipython.readthedocs.io/en/stable/interactive/magics.html).

> **Note:**
> 
> Sometimes it may happen that `ipympl` is not installed in our Jupyter. In this case, you need to install this library like any other before.

So the whole example will look as follows:

``` python
%matplotlib ipympl

import matplotlib.pyplot as plt

x = [0,1,2,3,4,5]
y1 = [0,1,2,3,4,5]
y2 = [0,1,4,9,16,25]

plt.plot(x, y1, label='Plot 1')
plt.plot(x, y2, label='Plot 2')  
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
```

## Two methods of creating plots

Matplotlib provides two methods of creating plots:

- using `pyplot` interface,
- using object-oriented interface,

In the course we are only going to discuss `pyplot`, as the preferred interface to be used in Jupyter Notebooks .

## Documentation

The library documentation is [here](https://matplotlib.org/stable/contents.html).
