# 02-DataVis-5ways

Assignment 2 - Data Visualization, 5 Ways  
===
In this assignment I used three librareis and two graphing tools.
1. Python Matplotlib
2. JavaScript d3 HTML CSS
3. R ggplot2
4. Matlab
5. Flourish

Python Matplotlib
---
![5 Ways Python Matplotlib](https://user-images.githubusercontent.com/59973823/107841052-825ad180-6d85-11eb-945d-b6af04e60319.png)

This is the python implimentation with matplotlib.
The users can clearly see the different between each Manufacturer, and background color is comfortable.
## Technical Achievements
The circle size of the legend is related to the average weight of all the correspond Manufacturer.
I add the minor ticks and major ticks to the axis which is same as the example.
### Design Achievements
Perfect lol.

JavaScript d3 HTML CSS
---
![5 Ways d3](https://user-images.githubusercontent.com/59973823/107840994-41fb5380-6d85-11eb-9d0b-276af9c4470c.PNG)
This plot is created from d3 library.
This plot might be the hardest one in this homework. We have to create every single component in this plot manully, including the axis, font size, tick size.....
The graph is on a SVG component with all its dimension specified. There are many anonymous function in this section. 
## Technical Achievements
Besides the JavaScript and d3, I used some CSS to modify the font size and grid color.
### Design Achievements
None

R ggplot2
---
![5 Ways ggplot2](https://user-images.githubusercontent.com/59973823/107841016-62c3a900-6d85-11eb-9a46-8bbba2684aff.png)
The plot from ggplot2 + R is identical to the example.
After reading the CSV file, we specify the files we want to plot and the size and color as two extra feature in the plot.
We can add different component objects in the ggplot.

## Technical Achievements
I added the major and minor grid ticks.
### Design Achievements
It shows all the legends for Weight and Manufactuerers.

Matlab
---
![5 Ways Matlab](https://user-images.githubusercontent.com/59973823/107841017-65be9980-6d85-11eb-9e32-65a5cced5a36.png)
The legend is shown on the top right, and users can clearly distinguish all the samples from their size and color.
The implementation is matlab is very simple.

## Technical Achievements
One of the triky part in the plot is square the Weight before we map them to circle size. If we linearly map the Weight to circle size, we cannot see too much difference between each circle :)
### Design Achievements
Users can click on each circle and see the actual value for each sample.

![5 Ways Matlab Demo](https://user-images.githubusercontent.com/59973823/107841564-c7810280-6d89-11eb-8a6a-aa92ff69e5c8.png)


Flourish
---
![5 Ways Flourish](https://user-images.githubusercontent.com/59973823/107840999-49baf800-6d85-11eb-8be6-e481a219d20a.png)

![5 Ways Flourish demo](https://user-images.githubusercontent.com/59973823/107840997-46277100-6d85-11eb-886d-7b00b4ab40a3.PNG)
This is the plot from Flourish tool. Similar as the previous plots, we can see the color coded and size coded samples.
This tool is very simple to use. We can import out data to that website and select the rows or column we want to plot and the columns that we want to use as the extra features, such as size, color.
## Technical Achievements
### Design Achievements
Users can use the slider on the top to see the data in a specific year.



