# Introduction to generating charts

Type: Article

Creating information-rich visualizations (also referred to as charts) is one of the most important tasks of an analyst. They can be generated during data visualization to, for example, help identify outliers and the need for data transformation. In addition, they come in handy when planning models. Sometimes the main purpose of an analyst's work is to create an interactive visualization to share on the web. Before we move on to the ones used in Python, let's discuss the types of charts.

## Graphical forms of data presentation

Many types of statistical graphs are used in practice. The use of a particular one is determined by the nature of the collective and the specifics of the phenomenon being analyzed. The selection also depends on the type of data in which the information is recorded and the nature of the regularities that the graph is intended to show.

Among the most commonly used graphical forms of data presentation are charts:

- surface, including bar and column charts,
- linear,
- map,
- pictorial,
- complex (combined) including stratified, balance and cartodiagrams.

### Area charts

They take the form of plane figures such as rectangles (columns), squares, circles. In charts, we mostly use the area of these figures. Most often they are used to describe changes in abundance by means of some quantitative or qualitative characteristic. We choose the graph to give the viewer the best illustration of the presented phenomenon.

Here we touched on two new issues - quantitative and qualitative characteristics. By Quantitative we mean measurable characteristics such as height, weight, age, for example, while a qualitative characteristic would be, for example, eye color or gender.

![Bar charts](/presentations/DTL/en/4.9/W/M_05_S_12/ec7b18ca-040a-43c6-a158-1e86324217fc/student_content/e9e93b4f-b462-416c-a336-524df23853ce/./images/image14_en.png)

### Bar and column charts

The most common use of such charts will be to present the structure of the collective in percentages. For a bar chart, we treat the entire area of a given bar as 100%, and the structure indicator determines the adequate part of its area.

![Bar and column chart](/presentations/DTL/en/4.9/W/M_05_S_12/ec7b18ca-040a-43c6-a158-1e86324217fc/student_content/e9e93b4f-b462-416c-a336-524df23853ce/./images/image11.png)

In the charts above, the area (or length or height) of each bar represents the number of units in each category, and all bars together - the entire size of the collective. The order in which the bars are presented can be arbitrary. As a rule, the chart is a form of a certain generalization of a table or series and that's why on the chart we should use an ordering criterion, such as from the most frequent category to the least numerous one or vice versa.

### Pie charts

Not unlike rectangular charts, they are used to present the structure of the collective. "Start" of the chart begins at 12 o'clock. Each subsequent slice is placed clockwise.

![Pie chart](/presentations/DTL/en/4.9/W/M_05_S_12/ec7b18ca-040a-43c6-a158-1e86324217fc/student_content/e9e93b4f-b462-416c-a336-524df23853ce/./images/image6_en.png)

### 3-D charts

Sometimes we can meet with a variation of rectangular graphs in three dimensions, that is, instead of a rectangle a cuboid is plotted, and instead of a circle a cylinder.

![3-D chart](/presentations/DTL/en/4.9/W/M_05_S_12/ec7b18ca-040a-43c6-a158-1e86324217fc/student_content/e9e93b4f-b462-416c-a336-524df23853ce/./images/image6_en.png)

### Age pyramid

Used to graphically present the demographic structure of the population. With it, we can present the population of measurable and non-measurable characteristics, for example, sex and age.

![Age pyramid](/presentations/DTL/en/4.9/W/M_05_S_12/ec7b18ca-040a-43c6-a158-1e86324217fc/student_content/e9e93b4f-b462-416c-a336-524df23853ce/./images/image4_en.png)

### Line chart

It has the character of a line plotted in a coordinate system. Most often used to present changes over time for a single phenomenon, e.g. coal mining, car production.

![Line chart](/presentations/DTL/en/4.9/W/M_05_S_12/ec7b18ca-040a-43c6-a158-1e86324217fc/student_content/e9e93b4f-b462-416c-a336-524df23853ce/./images/image8.png)

### Map chart

Increasingly popular, often used in management panels and reports. Thanks to the range of colors we are able to show the variation of the analyzed phenomena. They are commonly called cartograms. An example of an intensity indicator can be: unemployment rate, GDP per capita, etc.

![Map chart](/presentations/DTL/en/4.9/W/M_05_S_12/ec7b18ca-040a-43c6-a158-1e86324217fc/student_content/e9e93b4f-b462-416c-a336-524df23853ce/./images/image2_en.png)

### Combo chart

It comes in various forms combining, for example, Cartogram and bar chart. Allows you to show the structure of phenomena over time (stratified), or the effect of overlapping phenomena (balance)

![Combo chart 1](/presentations/DTL/en/4.9/W/M_05_S_12/ec7b18ca-040a-43c6-a158-1e86324217fc/student_content/e9e93b4f-b462-416c-a336-524df23853ce/./images/image12.png)
![Combo chart 2](/presentations/DTL/en/4.9/W/M_05_S_12/ec7b18ca-040a-43c6-a158-1e86324217fc/student_content/e9e93b4f-b462-416c-a336-524df23853ce/./images/image3.png)

### Radar chart

Line chart type. It can be replaced by a column chart, but in some cases, it may be more readable. (change of some values in two moments; to compare several equally significant variables simultaneously). Second example below

![Radar chart](/presentations/DTL/en/4.9/W/M_05_S_12/ec7b18ca-040a-43c6-a158-1e86324217fc/student_content/e9e93b4f-b462-416c-a336-524df23853ce/./images/image15_en.png)

## The most common mistakes when creating charts

Below we can see the results of an annual poll for the worst chart of the year....

![Chart anti-example](/presentations/DTL/en/4.9/W/M_05_S_12/ec7b18ca-040a-43c6-a158-1e86324217fc/student_content/e9e93b4f-b462-416c-a336-524df23853ce/./images/image1.png)

At first glance a very pleasant chart illustrating recruitment results for different university faculties and cites, but.... notice the doubled legend for the colors. Cities in the lower-right (see yellow and red dot for Białystok and Radom) share colors with types of studies in the upper-left (see dots number 3 and 5). The pie chart does not represent shares - there are more full-time study programmes at the university that created this infographic than those 6 listed in the circle slices, besides, the number of seats per candidate (rather than candidates per seat) is a better association when discussing shares. This proves that not every collection of numbers can be used in a pie chart!

## Prettiest charts

To pleasantly conclude our introduction to charts is something quite different, that is, a few links (the charts are too big) that can serve as a template for building your own charts:

1. https://www.informationisbeautifulawards.com/news/485-information-is-beautiful-awards-2019-the-winners
2. https://flowingdata.com/2019/12/19/best-data-visualization-projects-of-2019/
