# 02-DataVis-5ways

Assignment 2 - Data Visualization, 5 Ways  
===

Standards
---

- Data positioning: it should be a downward-trending scatterplot as shown.  Weight should be on the x-axis and MPG on the y-axis.
- Scales: Note the scales do not start at 0.
- Axis ticks and labels: both axes are labeled and there are tick marks at 10, 20, 30, etcetera.
- Color mapping to Manufacturer.
- Size mapping to Weight.
- Opacity of circles set to 0.5 or 50%.

# Flourish

![ggplot2](img/flourishvisualization.png)

Flourish is an extremely easy method of data visualization that relies on a visual interface.

To use it, I uploaded the data file, selected which columns held data I wanted to show, and customized it to my needs (with legends, colors, opacity, gridlines, etc). The axis minimum and maximum were customized, and while premade color palettes exist for the mapping, an easy override option allowed me to handpick colors for each grouping (which is why the colors pretty much match the sample graph). Lastly, the size mapping of the dots was a bit of a struggle. The smallest dot for 5 is very close in size to the largest dot for 405. I ended up realizing that they scaled the dots based on the maximum and minimum, so keeping those numbers close to the actual scale would basically allow for the biggest difference. Although the font is a little different, the closest free option is what I selected (the rest were all serified).

Overall, this tool was extremely easy to use with extremely satisfactory results.

# R + ggplot2

![ggplot2](img/Rplot.png)

R is a language I am wholly unfamiliar with that is typically used for statistical computing, while ggplot2 is a common library to help make data visualizations in R.

I utilized a ggplot bubble plot to map weight to X, MPG to y, and weight to size. ggplot's `geom_point` was also useful in customizing aesthetics - in particular, the 50% opacity and using color to separate manufacturers.

While this tool combination required a lot of time and effort to understand the syntax, read through the documentation, and find the right commands, it came out with a highly satisfactory result. I believe it will take less time to create similar plots in the future.

Libraries, Tools, Languages
---

You are required to use 5 different tools or libraries.
Of the 5 tools, you must use at least 3 libraries (libraries require code of some kind).
This could be `Python, R, Javascript`, or `Java, Javascript, Matlab` or any other combination.
Dedicated tools (i.e. Excel) do not count towards the language requirement.

Otherwise, you should seek tools and libraries to fill out your 5.

Below are a few ideas. Do not limit yourself to this list!
Some may be difficult choices, like Matlab or SPSS, which require large installations, licenses, and occasionally difficult UIs.

I have marked a few that are strongly suggested.

- R + ggplot2 `<- definitely worth trying`
- Excel
- d3 `<- since the rest of the class uses this, we're requiring it`
- Matplotlib
- three.js `<- well, it's a 3d library. not really recommended, but could be "interesting"`
- p5js `<- good for playing around. not really a chart lib`
- Tableau
- Java 2d
- GNUplot
- Vega-lite <- `<- recently much better. look for the high level js implementations`
- Flourish <- `<- popular last year`
- PowerBI
- SPSS

You may write everything from scratch, or start with demo programs from books or the web.
If you do start with code that you found, please identify the source of the code in your README and, most importantly, make non-trivial changes to the code to make it your own so you really learn what you're doing.

Tips
---

- If you're using d3, key to this assignment is knowing how to load data.
You will likely use the [`d3.json` or `d3.csv` functions](https://github.com/mbostock/d3/wiki/Requests) to load the data you found.
Beware that these functions are *asynchronous*, meaning it's possible to "build" an empty visualization before the data actually loads.

- *For web languages like d3* Don't forget to run a local webserver when you're debugging.
See this [ebook](http://chimera.labs.oreilly.com/books/1230000000345/ch04.html#_setting_up_a_web_server) if you're stuck.


Readme Requirements
---

A good readme with screenshots and structured documentation is required for this project.
It should be possible to scroll through your readme to get an overview of all the tools and visualizations you produced.

- Each visualization should start with a top-level heading (e.g. `# d3`)
- Each visualization should include a screenshot. Put these in an `img` folder and link through the readme (markdown command: `![caption](img/<imgname>)`.
- Write a paragraph for each visualization tool you use. What was easy? Difficult? Where could you see the tool being useful in the future? Did you have to use any hacks or data manipulation to get the right chart?

Other Requirements
---

0. Your code should be forked from the GitHub repo.
1. Place all code, Excel sheets, etcetera in a named folder. For example, `r-ggplot, matlab, mathematica, excel` and so on.
2. Your writeup (readme.md in the repo) should also contain the following:

- Description of the Technical achievements you attempted with this visualization.
  - Some ideas include interaction, such as mousing over to see more detail about the point selected.
- Description of the Design achievements you attempted with this visualization.
  - Some ideas include consistent color choice, font choice, element size (e.g. the size of the circles).
