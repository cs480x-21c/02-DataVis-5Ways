# d3, HTML, Javascript

<img src="img/CarsPlotD3.png" width="500">

Resources:

https://www.d3-graph-gallery.com/graph/scatter_basic.html

https://www.d3-graph-gallery.com/graph/custom_theme.html

https://www.d3-graph-gallery.com/graph/scatter_tooltip.html

https://www.digitalocean.com/community/tutorials/js-filter-array-method

After the introduction of d3 last week, I think that really helped me get a hang of things this week to make more progress and become more familiar with the toolset. The resources I used listed above were mostly starter code that were very helpful in formatting and learning about the specific plot we were required to make. It was very helpful in getting me to understand good coding practices when making visualizations with d3. Compared to the other methods of showing visualizations, I really liked how d3 had more of a separative approach when adding filters and other attributes such as the weighted plot points, categorical coloring, and the axis limitations. I thought this library was very good in organizing the different attributes and filters and the code seemed to be more readable than other libraries. Overall, I thought that this method of creating a visualization was really straightforward. This method seemed to work for a variety of datasets as we can specify very clearly what we want in a visualization.

# Excel

<img src="img/CarsExcel.png" width="500">

Using Excel was surprisingly one of the more difficult methods that I chose this week out of the five ways of replicating the graph. It took much longer than I expected to figure out the Excel tool. The data importing functionality in Excel was very useful for users that aren't as keen on coding. With this, I found it took a good amount of time to figure out that the Excel tool did not process that the "MPG" column has numerical data instead of text or "general" data. If I had more experience with this tool, I think that would be clearer from the beginning, however, it took quite a long time to figure this out. I think that with more use, the filter option on the Excel tool turned out to be very useful especially when it was time to filter out the rows with MPGs of "NA" value. I found it to be somewhat pretty obnoxious when trying to graph all the different colors and linking these categorically with the manufacturer of each car. This took awhile to get used to since we had to create a "series" and basically plot the datasets, after we filter them by manufacturer, on top of one another. I think this method of visualization would be very more useful for smaller datasets since it doesn't have a lot of complex capabilities. While I did try, I was not able to figure out how to plot the points with respect to the weights and the color of each manufacturer was pre loaded from already existing themes and those seemed to be more difficult to deviate from. Excel was, however, more user friendly when trying to add a legend after creating all the separate series. 

# MATLAB

<img src="img/CarsMatlab.png" width="500">

Resources:

https://www.mathworks.com/matlabcentral/answers/72545-how-to-import-csv-file-in-matlab

My MATLAB expereince was pretty simple. After taking a course using and coding in MATLAB, I thought this was a pretty simple task to plot a loaded dataset. With simple if and else statements along with the strcmp (string compare) function, I thought that it was a very easy process in trying to categorize each manufacturer and graphing the data that way. This did make it more difficult to create a legend in order to specify each manufacturer, which is more of a trade off depending on what is more important to the user. MATLAB also has many different functions for all different kinds of plots and it had one for scatter plots as well which was very useful in our case here. It was also very simple to set the x and y limits as those are also built in functions to specify the range of the axis. I think this method of visualization would be very useful for datasets like this one or simpler ones. I don't think the MATLAB library would be very useful in complex datasets especially with its difficulties in fulfilling simple tasks such as creating legends. 

# R+ggplot2

<img src="img/CarsPlotR.png" width="500">

Resources:

https://jcoliver.github.io/learn-r/004-intro-ggplot.html

By far, I thought that this method was the most simplistic and concise method in plotting this type of data. While the plot we were trying to replicate was done in this library, I was able to recreate the plot in mere seconds with very few lines. The resources online that I've listed played such a big role in helping me understand the R language and recreating this plot. The geom_point() stated in the example was very useful in adding the weighted points attribute to the plots as well as stylistic and aesthetic uses to make the points 50% opacity. This library was great for this dataset and very useful for statistical analysis and creating charts and graphs such as these at a very low and minimal effort. 

# Flourish

https://public.flourish.studio/visualisation/5283874/ (This is the link to the public flourish data)

<img src="img/CarsFourish.png" width="500">

This was a very new software for me and just being a beginner creating visualizations, I thought that this was amazing! Flourish was so simple to use and it would be an amazing tool to create quick and easy visualizations with very limited experience. This software is very user friendly and requires no coding whatsoever. I also really like the visualization aspect in which when the user hovers over the points, it gives all the data that I've specified to show in a pop up box. I thought the user experience was superb and this was such an amazing tool overall. With the basic account, however, it may have limitations on some capabilities but with this assignment, I thought recreating the scatterplot was perfect for this software and it was done with ease. 

# Technical / Design Achievements

<img src="img/CarsPlotD3TechAchievement.png" width="500">

For my technical design achievement this week, I chose to add a hover and mouseover event in my d3 implementation. This was done with some help online since last week I struggled with mouseover events. The technical design achievement is done in which when the user hovers their mouse over a point, it would display in a textbox, as seen in the screen capture above, the exact MPG value. This could also be done with other data specifications. I wanted to try something like this to have an interaction between user and visualization as to me, it seems to be a useful tool for different visualizations. Additionally, I thought that with a couple of my other methods of implementation, it comes with this sort of capability for the user so it was really nice to see that I could replicate this in d3 as well.

As for the design achievements, in all of my plots, other than two, I was able to replicate almost the exact color scheme that was shown on the example plot. This was done using several tools online to figure out the hex values of the color specified in the example plot. I tried to get it as close as possible in this way to the original colors and for the plots that I didn't succeed in doing this for, that's how I gauged the difficulty in changing the color markers for a typical visualization. Additionally, in my MATLAB plot, I was also able to mimick the tick marks done in the original plot and the spacing and numbering. This was done with help of online resources in order to accurately replicate the original plot as much as possible. 
