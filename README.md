# d3

d3 Is of course the library we use in this class and as such it needs no more introduction.
What I can say about d3 is that it is easily the most in depth tool I used in this project.
d3 allowed me the most flexibility to control every aspect of my visualization.
That being said it made it very difficult for me to get it to look just right, as I had to do all the work.
Compared to other tools like ggplot or Tableau a lot more work went into making my d3 visualization.
With this control though I can see far more creative applications being possible than with the other tools I used.

![d3 Visulisation](img/d3.png)

## Technical Achievements - d3
While the task itself was relively straight forward, the difficulty with this library was understanding the differences between
using d3 v4 (the version used in the guides I found) and d3 v6 (The version used in class) and how to overcome their subtle differences

## Design Achievements - d3
In order to make the legend I needed to create a new object, similar assignment 1 and place it next to the chart.

## Resources - d3

[d3 Graph Gallery](https://www.d3-graph-gallery.com/graph/bubble_color.html) - This resource
was extremely helpful as a starting point on how to begin my graph. However, it's primary challange
was understanding the difference between d3 v4 and d3 v6.

[sgratzl's d3 Tutorial](https://github.com/sgratzl/d3tutorial) - This resource helped me with cleaning up my visualisation
inorder to get it to look closer to how the given visualisation appears.

# R + ggplot2

R is a powerful language commonly used in computing and statistical manipulation or display. Combined with ggplot2
it allows for extremely simple and elegant plotting with R. Of all the tools used here I think that dispite requiring
coding rather than drag and drop this was the easiest tool to use.
This tool would be extremely useful if I am ever working with a lot of data in R and I want to display my data
without using an external tool.

The only difficulty I faced to create this visualisation was for R to be able to locate the dataset without needing to 
provide the absolute path, however that was not a necessary addition.  

![ggplot2 Visualisation](img/ggplot2.png)

## Technical Achievements - ggplot2

I am most proud of figuring out how to dynamically get R to locate the csv file using the current working directory.
The idea behind this is that if the csv is ever updated on a different machine you do not need to change any code for the 
visualization to be able to update itself.

This visualisation was generated using 'geom_point()' and 'aes()'

## Design Achivements - ggplot2

It looks pretty much exactly like the target visualisation. 

## Resources - ggplot2

[R Graph Gallery](https://www.r-graph-gallery.com/320-the-basis-of-bubble-plot.html) - As with d3 this resource gave me 
an excellent starting point to create my visualisation

[Quick R: Importing Data](https://www.statmethods.net/input/importingdata.html) - This is where I was able to figure out how
to get the csv file to read from the working directory rather than the absolute path

# Python + Matplotlib + Pandas

Python is one of, if not the, most widely used development language. 
One of its most notible applications is machine learning and ai.
Combined with Matplotlib and Pandas you get a very powerful data handling and visualisation toolkit.
That being said, there is a learning curve to understanding how Pandas and Dataframes work together. 
The biggest difficulty I had here was all the possible ways to do the same thing. 
I fell down multiple rabbit holes of how to create my visualisation, only to reach a dead end when I 
could not find a tutorial that allowed me to finish my work.

That being said when I finally got to the solution the code was quite simple and elegant. 
Similarly to R and ggplot2 I would imagine these libraries would be very useful if I was 
working on data with python and did not want to use and external tool to have to display my work.

![Python + Mathplotlib + Pandas](img/matplotlib.png)

## Technical Achievements - Matplotlib

While not the most impressive achievement, I do believe my use of the group_by function
along with dictionaries to store my manufacturers and their respective colors allowed for a 
pretty elegant solution. 

## Design Achievements - Matplotlib

Design wise, I do not think there is much stunning about this visualisation. 
The ration applied to the data points is good at replicating the target visualisation,
however I do not think that I did a very good job with the color matching. 

## Resources - Matplotlib

[Dataviz with Python and R](https://datavizpyr.com/make-bubble-plot-in-python-with-matplotlib/) - As with my other
visualisations this resource gave me the starting point that I used to create my visualisation 

[kite](https://www.kite.com/python/answers/how-to-split-a-pandas-dataframe-into-multiple-dataframes-by-column-value-in-python) - 
This resource pointed me on how to separate my data frame by manufacturer. 

## Tableau

Tableau is a desktop application that allows for very intuitive data visualisation with data
from almost any source. When working with large databases that did not require any manipulation to 
be displayed this would be the perfect tool.
The biggest downside of this tool is that it requires payment to keep using it, making it ideal for a large company setting.
The hardest part of using this tool is understanding that you need to use the navigation arrows to get started.

![Tableau](img/Tableau.png)

## Design Achievements - Tableau

Design wise I think I did a good job matching my visualisation to the target vis, however given the 
intuitiveness of Tableau, I would not call that my achievement but rather theirs.

## Technical Achievement - Tableau

I would have to agree with myself from design achievements for this one as well.

## Resources - Tableau

[Tableau - Build a Scatterplot](https://help.tableau.com/current/pro/desktop/en-us/buildexamples_scatter.htm) - 
This site showed my how to get started with Tableau and how everything is built off of a drag and drop system

# Flourish

This resource is a completely web biased version of Tableau. However, I do not think that it does as good of a job.
While it is easier to get into it does not have the same finite control over your visualisation, and you cannot import 
as wide of a variety of data. 
I would see this as a good option if you wanted the ease of Tableau, but did not want as many features and complexity.

![Flourish](img/Flourish.png)

## Design Achievements - Flourish

I think given the limited control that Flourish provides I did a good job replicating the given visualisation. 
Although, again, I do not think my color pallet was quite right.

## Technical Achievements - Flourish
Similarly to Tableau I do not think I have much to pat myself on the back about since most of the heavy lifting was
already done for my by the Flourish developers.
