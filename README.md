# 02-DataVis-5ways

Assignment 2 - Data Visualization, 5 Ways  
===

# R + ggplot2 
My first implementation uses R and ggplot2 to  create the visualization of the car data. You can view a screenshot of the visualization:

![here](https://github.com/HHauptfeld/02-DataVis-5Ways/blob/main/img/r%2Bggplot2.png).

An easy part of using R and ggplot2 is that it took very few lines of code to actually create the visualization. A difficult part of using R and ggplot2 was setting up the R environment on my computer because I've never used R before. It took time for me to research how R works and how to set up the correct environment. I could see this tool being useful in the future with more bubble charts. I didn't have to use any hacks or data manipulation to get the right chart.

Sources:
* https://flowingdata.com/2010/11/23/how-to-make-bubble-charts/
* https://www.r-graph-gallery.com/320-the-basis-of-bubble-plot.html


# Python + matplotlib + pandas
My second implementation uses Python, matplotlib, and pandas to create the visualization of the car data. You can view a screenshot of the visualization:

![here](https://github.com/HHauptfeld/02-DataVis-5Ways/blob/main/img/python%2Bmatplotlib.PNG).

An easy part of using Python, matplotlib, and pandas was accessing columns of data using dataframe from pandas. A difficult part of using Python, matplotlib, and pandas was implementing the color dimension of the data, separated by the manufacturer. I could see this tool being useful in the future when I need to manipulate entire columns of data. I used data manipulation to implement the color dimension in this chart. I wrote a function (using the resources below), to create a new column in the dataframe that essentially assigns one color to each type of manufacturer. Then, I used this new column to plot the car data by color.

Sources:
* https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html
* https://www.tutorialspoint.com/python_data_science/python_bubble_charts.htm
* https://glowingpython.blogspot.com/2011/11/how-to-make-bubble-charts-with.html
* https://python-graph-gallery.com/270-basic-bubble-plot/

# D3JS
My third implementation uses D3 and JavaScript to create the visualization of the car data. You can view a screenshot of the visualization: 

![here](https://github.com/HHauptfeld/02-DataVis-5Ways/blob/main/img/d3js.PNG).

An easy aspect of d3js was the accessibility to tutorials online that taught me how to use d3js. Their documentation is very detailed and includes some great examples of how to implement what you need to do. A difficul aspect of d3js is how complicated the code can become. It took me a really long time to fiddle around with the color aspect of the chart and visually display the manufacturers. I didn't have to use any hacks or data manipulation to get the right chart. In order to view the D3JS implementation in your browser in real time, do the following two commands in a terminal in which your current working directory is this repo:

`npm install http-server`

`npx http-server`

Sources:
* https://www.d3-graph-gallery.com/graph/bubble_basic.html
* https://www.d3-graph-gallery.com/graph/bubble_template.html

# Excel
My fourth implementation uses Excel to create the visualization of the car data. You can view a screenshot of the visualization: 

![here](https://github.com/HHauptfeld/02-DataVis-5Ways/blob/main/img/excel.PNG).

Steps I took to import data: Data -> Get Data -> Get File -> From_Text/CSV

I created 10 more columns (in groups of 2) after importing the original CSV file into Excel. Each group of columns that I created had an 'MPG' column and a 'Weight' column.
I copy and pasted the information for each of the 5 manufacturers into their appropriate columns. I then inserted a blank bubble chart, and added a data series for each of the MPG/WEight columns groupings for each manufacturer. I used 'Format Chart Area' to incorporate the following features:

* changing the scale of the x-axis and y-axis
* adding a legend
* adding labels on the x-axis and y-axis

An easy aspect of Excel was that there was no programming involved. A difficul aspect of Excel is that their UI is not very intuitive. It took me a while to find out how to incorporate the size of bubbles and the color dimension in my data visualization. I didn't have to use any hacks or data manipulation to get the right chart.

# Flourish 

My fifth implementation uses Flourish to create the visualization of the car data. You can view a screenshot of the visualization: 

![here](https://github.com/HHauptfeld/02-DataVis-5Ways/blob/main/img/flourish.png). 

Flourish is a data visualization software that has a really great UI for users to implement data visualizations. I used their site (flourish.studio) in order to create my visualization, I selected to create a bubble chart, and imported the cars-sample.csv file into the visulaization. Then, I adjusted the appropriate attributes using Flourish's intuitive UI. An easy aspect of Flourish is their UI. Flourish's site made it very easy to select hat and how I wanted to feature my data in the visualization. A difficult aspect of Flourish is not much, but getting used to learning how exactly to use the UI took a little bit of time. I didn't have to use any hacks or data manipulation to get the right chart.


### Technical Achievements
In my d3js implementation, I added an extra feature. Users can hover over a bubble, and it displays the manufacturer that the car is associated with. I completed this by following [this tutorial](https://www.d3-graph-gallery.com/graph/bubble_template.html).
