# Other ways to create charts with Python

Type: Article

In class, we learned about the Matplotlib library as the most popular solution for creating charts in Python. In this article, we will discuss what other possibilities this library gives us and what alternatives there are for it.

## Matplotlib - what else can it do?

So far we have learned how to create the most popular charts and how to add extra elements to them, such as annotations, captions or data tables. However, Matplotlib gives us more possibilities than what we have learned. That is why we recommend getting familiar with the full scope of this library: it is very well illustrated with examples you can find on the [website](https://matplotlib.org/stable/gallery/index.html). It is also a good idea to check the [tutorials](https://matplotlib.org/stable/tutorials/index.html), prepared by the creators of Matplotlib.

### 3D charts

The Matplotlib library gives us the ability to create charts in 3D. It allows us to create graphs that show relationships of more than 2 values.

Sample code:

``` python
import random
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,15))
ax = fig.add_subplot(111, projection='3d')
n = 100

for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
    xs = [random.randint(0, 100) for _ in range(n)]
    ys = [random.randint(0, 100) for _ in range(n)]
    zs = [random.randint(zlow, zhigh) for _ in range(n)]
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
```

You can find more examples (including really complex ones) [here](https://matplotlib.org/stable/gallery/index.html#d-plotting).

### Animations

Matplotlib library gives us the ability to animate our charts. This is a very useful feature if we want to observe the change of values over time. However, creating such examples requires very good knowledge of the library and Jupyter Notebook (running animations in Jupyter Notebook is not easy and can vary depending on the operating system, Jupyter version and version of the library itself).

You will find more examples [here](https://matplotlib.org/stable/gallery/index.html#animation).

## Pandas

Interestingly, [Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html) has a built-in module responsible for generating charts. Underneath, it simply creates graphs using Matplotlib, but gives you the ability to create them faster and easier. However, it doesn't give you such editing and customization options.

We didn't specifically show these capabilities during the class - we assume that after getting to know Matplotlib, learning make charts with Pandas should be simple.

Example:

``` Python
import pandas as pd

df = pd.read_csv(
    'Meteo data.csv',
    sep=';',
    decimal='.'
)

df.plot(subplots=True, figsize=(10, 12))
```

## Seaborn

Another often used library is [Seaborn](https://seaborn.pydata.org/index.html). It is a sort of overlay on Matplotlib. It is considered by many to be easier to use, but it does not yet have a stable version (at the time of writing this article, the latest version is 0.11.1).

Sample code:

``` Python
import seaborn as sns
sns.set_theme(style="darkgrid")

# Load an example dataset with long-form data
fmri = sns.load_dataset("fmri")

# Plot the responses for different events and regions
sns.lineplot(x="timepoint", y="signal",
             hue="region", style="event",
             data=fmri)
```

## Bokeh

[Bokeh](https://docs.bokeh.org/en/latest/index.html) is a library specializing in interactive charts. By default, it creates charts as HTML files, which can then be attached to, for example, a web page (it creates JavaScript code that is responsible for displaying the chart).

In the case of Bokeh, we are not able to post a simple code to run in Jupyter, which would show the capabilities of this library.
