# 02-DataVis-5ways

General Description
===
The general format of the markdown includes a heading of the visualization tool used followed by a description of the visualization tool, design achievement done for that particular visualization tool and a technical achievement done for that particular visualization tool. Pictures will, of course, be included as well. Once the whole have been examined, the specific design and technical achievements will be listed that encompass the whole of the assignment. A section on references will be added at the end. I do not know why some of the images are not appearing. Please see the image folder for the results - thank you! Some folders may not have really anything besides the original file in there and a file in all caps. Please read the all caps file for some detail/direction of where to find the produced scatterplot.


# Excel

Description
===
  Displayed is the desired graph of MPG vs Weight that is displayed in the original assignment description. There is a legend that shows the association between the color and the manufacturer.

  Excel was not the easiest of the data visualization tools used, but my familairity with it made the creation of the scatterplot go by much faster. My previous experience with Excel made creating the scatterplot easy. Selecting the data, axes creation, and legend creation were easy enough as well. Associating the size of the data points with the weight was more difficult, and the association is not as ideal as one would hope as there is no feature to change individual data point sizes. Some changes were made to address this nevertheless, as one can note the different data point sizes. I could see using excel for making basic graphs from data collected in an excel/csv file, but otherwise there are better options to use for making graphs and displaying data. Overall, excel feels too constricted compared to other data visualization tools. I do not have any new tips/tricks given my fimilarity with Excel, and its ease of use.

Pictures
===
![caption](img/ExcelIMAGE.1)
Above is the image of the completed scatterplot within Excel.

Design Achievement
===
There are two design achievements associated with this data visualization tool that I implemented. They are listed below:
 -The graph was labeled with text
 -There is a legend that notes the association of the data point colors and manufacturers. 
Technical Achievement
There was no real technical challenge when making this scatterplot, and there are no technical acheivments for this data visualization tool.
===


# d3

Description
===
  Displayed is the desired graph of MPG vs Weight that is displayed in the original assignment description. There are legends that show the association between color and manufacturer as well as data point size and weight. When mousing over a data point, the data point becomes more pronounced. Also, the MPG and Weight values for that datapoint are displayed. When mousing over, the data point reverts to its original appearnaces and the associated text disappeares as well.
  
  Using d3 was not as easy as the other data visualization tools that were done in conjunction to this project. The pizza meme regarding d3 that was sent into the slack was not wrong at all. Out of all those tools mentioned, this one was the hardest to do for two main reasons. The first being that I am new to d3 and, as such, do not know all the intricacies despite the experience I gained from the previous assignment. As the reference section indicates, I had to look up many of the functions to understand what they do, and how to properly implement them. The second reason rested on being able to plot the data points in the plot. Although the fix was quick, many hours were spent trying to figure out how to go about drawing points onto and within the scatterplot. Using d3 does have its beenfits though! There is ample room to make interactive elements that other visualization tools for the data do not let you. The ability to customize these interactive elements will be important for any future work as well - lending d3 more optimal for crafting interesting infrographics for target audiences. Once major questions were addressed, however, programming with d3 was rather intuitive. Future tips that I gained from working with d3 are listed here below:
    - When using d3.csv(), enter one paramter to access the csv file followed by a .then(function(data) {}) that contains all the code that one wants to run
    -Plan out and understand the margins of a graph as it is helpful when planning and crafting the final product
    -Elements, like text, can have ID attributes set to them that make removing and including said elements very easy
    -Be aware of what each parameter of a function is responsible for. In conjunction, I gained a greater insight as to what data each parameter in my function calls hold.

Pictures
===
![caption](img/d3IMAGE.1)
Above is the image of the base scatterplot in d3.

![caption](img/d3IMAGE.2)
Above is the image of the scatterplot when one of the points is moused over in d3.

Design Achievement
===
There are four design achievements associated with this data visualization tool that I implemented. They are listed below:
  -I used a text element to add a title to the graph. 
  -If the circle size was mapped directly to the weight of the car, the data points would be too large to see anything but a solid color. Thus, to better visualize the whole plot, the size of the data point was mapped to the particular weight diveded by 500 so that the scatterplot was visible and legible.
  -I was able to add a legend that associated the color of the dots with the manufacturers and the size of the dots to the weight of the cars
  -When one mouse overs a particular point, the point becomes more pronounced and visible so the user can see which datapoint is being hovered over

Technical Achievement
===
There are two technical achievements associated with this data visualization tool that I implemented. They are listed below:
 -Though the mouseover feature with the data points is a design achievement, this mouseover feature and its implementation are also a technical acheivement. Likewise, the appearance of the datapoint information upon mousing over a data point and its disappearnce when no longer mousing over a data point countas as a technical achievement
 -The data was cleaned to remove the presence of any NA information so as to remove any outliers that would otherwise disrupt the appearance of the graph.


# Flourish

Description
===
 Displayed is the desired graph of MPG vs Weight that is displayed in the original assignment description. There is a legend that indicates the association between the data point colors and manufacturers. When mousing over a data point, the information associated with that data point is shown. The size of the data points is, of course, mapped to weight. However, the weigh made the points too large and where transformed for visual appeal. The size of data points is mapped to the weight divided by 500.

 This data visualization tool was by far the easiest one to use. Once a dataset was uploaded, the Flourish tool was able to easily denote the header from the rest of the data. With this done, selecting the x and y values for the scatterplot was simple as was mapping color to manufacturers. Likewise, the size mapping was just as simple. Displaying the legend for the color was done with a click of a button. I could see this tool being used over Excel as many of the details are able to be easily edited, and are displayed outright so the user does not have to search for them. There is a large variety of other possible visualizations that can be made with the same ease provided a user has a data set. While there is a lack of customizability besides what is outright presented, this tool makes graphing and visualizing data easy and not a hassle. I would reccommend this tool for creaitng many graph varieties. The one real downside is that full features requiere the purchase of a premium version. There are no fun tips or tricks that were gained from this data visualization tool due mainly to its ease of use. I would put a link out, but it requires the premium version to do so. We could meet over Zoom to show off this data visualization if need be.

Pictures
===
![caption](img/FlourishIMAGE.1)
Above is the data visualization of the graph produced via Flourish.

![caption](img/FlourishIMAGE.2)
Above is an image that displays the mouseover feature of the data points.

![caption](img/FlourishIMAGE.3)
Above is the csv dataset that was used, and how each particular type is factored into the scatterplot. Weight was set as the x-values. MPG was set as the y-values. Color was based on manufacturer data. Size was based on the Weight/500 for visual appeal and designation - similarly to d3.

Design Achievement
===
There are four design achievements associated with this data visualization tool that I implemented. They are listed below:
 -The presence of a legend to explain the mapping between color and manufacturer. It was relatively simple, since it was with a click of a button, but adds to the design of the graph and understanding of the use.
 -The sizes of the data points are mapped to a transformed aspect of size. This transformation is the weight / 500. Without this transformation, the data points would overlap and become hard to completely distinguish, especially when hovering over a data point. Thus, mapping size to a transformed version of size is beenficial for the design of the scatterplot. One can see this change in the first and third image. 

Technical Achievement
===
There are not technical acheivements for this data visulaization tool. It is pretty straight forward to accomplish, and no real technical skill is needed. 


# R + ggplot

Description
===
Displayed is the desired graph of MPG vs Weight that is displayed in the original assignment description. It is actually quite similar to the one show in the original project description. There are two legends associated with this scatterplot: one that describes the mapping between the colors and the manufacturers and another that describes the data point sizes and the associated weight value realtively (increasing data point size with weight value). The data point sizes are mapped to the weight.

This data visualization tool was my personal favorite of the five used in this assignment. The r markdown file format in R studio is very appealing and useful to me. My previous experience with using R was very helpful in doing this visualization. R + ggplot is very easy to complete a data visualization with, basically. The ability to take in data from a csv file was easy. The use of the geom() and ggplot() function made accounting for outliers and making a well-detailed scatterplot also very easy. The most difficult part would have to be understanding which functions to use. R + ggplot has great use with statistical data and any imported data. Without any imported data, R + ggplot is less effective as it is geared for creating graphs and statistical analysis. One good trick that I learned from coding in this assignment was the importance of separating the R coded regions in the R markdown file. It helps in testing out the code which I hadn't done previously.

Pictures
===
![caption](img/RGGPlotImage.1)
Above is the plot from R + ggplot that I created from the R code.

Design Achievement
===
There are no design achievements associated with this data visualization tool. Much of the design features implemented are a result of the ggplot() and geom() functions from the ggplot library.

Technical Achievement
===
There are no technical acheivements associated with this data visualization tool. Much of the technical features are limited by R studio.


# Python + matplotlib

Description
===
Displayed is the desired graph of MPG vs Weight that is displayed in the original assignment description. The legend appearing alongside the scatterplot shows the association between the colors and the manufacturers. The data point sizes are mapped to the transformed weight data. In other words, the size of the data point is mapped to the weight / 15. Within Python, visualizing this scatterplot lets one zoom in on a particular area. Alongside that, Python lets one examine the exact x and y values for a data point.

The data visualization was not completely easy, but somewhat hard. Finding the exact function to properly take in the data and form the legend was somewhat time consuming. Once those were sorted, creating the scatterplot and plotting points was easy given my familiarity with Python. I truly understand why this language is popular. Cleaning the data to remove the 'NA' data was a lot easier than it was in d3 when it had to be done. This can also be attributed to my familiarity with the programming langauge, and that I took in the data in rows (another aspect I am very familiar with in comparision to method taken in d3). I did learn about the mpatches library for legend creation that I previously did not know. This will be useful moving forward when coding in Python.

Pictures
===
![caption](img/PythonMatplotlibIMAGE.1)
Above is pictured the scatterplot visualized using Python and matplotlib.

Design Achievement
===
There is one design achievement associated with this data visualization tool that I implemented. It is listed below:
 -The inclusion of a legend was completed using mpathces adds to the design of the scatterplot. One can more easily note the association between color and the manufacturers from the data set.

Technical Achievement
===
There are two technical achievements associated with this data visualization tool that I implemented. They are listed below:
 -The mpathces library was implemented and utilized, adding to my repetoire of programming knowledge.
 -The data was cleaned to remove the outliers that included data that is reported as NA. This makes forming the scatterplot visualization easier and adhere to the trend being shown.

# References

Excel sources
---
None.

d3 sources
---
1.[This source was used to set up a terminal because I wasn't sure entirely how to](https://github.com/ghickman/classify/issues/16)
2.[This source was used to consult when creating the plot](http://bl.ocks.org/weiglemc/6185069)
3.[This is the API for d3.js v6](https://github.com/d3/d3/blob/master/API.md)
4.[A source to learn how to take in csv data with d3](https://www.js-tutorials.com/javascript-tutorial/reading-csv-file-using-javascript-html5/)
5.[This source was used for some basis on the graph and axes formation of the scatter plot](https://www.d3-graph-gallery.com/graph/scatter_basic.html)
6.[This source elaborated details on the scale and scale linear aspects needed for graph creation](https://www.d3indepth.com/scales/)
7.[This source was used for some basis on the graph and axes formation of the scatterplot](https://www.d3-graph-gallery.com/graph/connectedscatter_legend.html)
8.[This source was used to get the opacity attribute related function](https://bl.ocks.org/EfratVil/2bcc4bf35e28ae789de238926ee1ef05)
9.[This source was used to understand how to give svg elements ids and how to remove the attributes based upon these ids](https://stackoverflow.com/questions/22075680/removing-text-on-mouseout-event)

Flourish sources
---
None.

R + ggplot
---
1.[This source was used to consult the ggplot plot related functions](http://www.sthda.com/english/wikiggplot2-scatter-plots-quick-start-guide-r-software-and-data-visualization)
2.[This sources was used to consult the ggplot related functions](http://monashbioinformaticsplatform.github.io/2015-11-30-intro-r/ggplot.html)
3.[This source was used to get info on taking in data using a csv file](https://swcarpentry.github.io/r-novice-inflammation/11-supp-read-write-csv/)
4.[This source was used to get info on how to get colors on the scatterplot with ggplot](http://www.sthda.com/english/wiki/ggplot2-colors-how-to-change-colors-automatically-and-manually)

Python source
---
1.[This source was used to determine how to set specific tick marks in Python with matplotlib](https://www.tutorialspoint.com/matplotlib/matplotlib_setting_ticks_and_tick_labels.htm)
2.[This source was used to get a background on how to read csv data into Python](https://code.tutsplus.com/tutorials/how-to-read-and-write-csv-files-in-python--cms-29907)
3.[This source was used to identify the parameters of the plot function from matplotlib](https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.scatter.html)
4.[This source was used to get more background on reading csv data in with Python](https://docs.python.org/3/library/csv.html)
5.[This source was used as a basis to get a custom legend](https://matplotlib.org/3.3.3/tutorials/intermediate/legend_guide.html)
