# 02-DataVis-5ways

Assignment 2 - Data Visualization, 5 Ways  
===
Original Visualization:

![original](img/original.png)

# R & ggplot2

R is a programming language designed for use in statistics and managing datasets. Ggplot2 is a library for R that makes it easier to create better looking graphs. Given that the original visualization was made in R, using ggplot2, it was fairly straightforward to recreate almost perfectly.

![r&ggplot2](img/r&ggplot2.png)

# Google Sheets

Google sheets is very similar to excel in terms of functionality, but I find it easier to use since it's browser based and free. Google sheets has built in methods fpr generating graphs from datasets, with the caveat that will often default to the wrong type of chart, and will require some tweaking.

The bubble chart layout works well for the original image we're trying to replicate, so I used that. I had to tweak and label the axes, and disable the labels on the individual bubbles, but after that, it was pretty much done.

![googlesheets](img/googlesheets.png)

## Technical Achievements


### Design Achievements
- Made use of colorblind-friendly colors for points across all visualizations, courtesy of this interactive site:
	- https://davidmathlogic.com/colorblind/#%23D81B60-%231E88E5-%23FFC107-%23004D40
