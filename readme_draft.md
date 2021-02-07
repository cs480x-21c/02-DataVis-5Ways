# d3.js

d3.js is a Javascript library that can manipulate webpages based on data.

To visualize the dataset, I created an x and y axis using d3.js's scaleLinear, axisBottom, and axisLeft API's. To create axis labels, I used d3.js to add text SVG elements to the document. Then, to create the dots in the scatter plot, I used d3's data() API to add a dot for each data entry, with a radius and color determined by the weight and manufacturer.

I found it cumbersome to use axes in d3. Regardless of the type of axis that is created, d3 will render the axis at (0,0) by default, requiring the developer to translate the axes to be able to see the axis ticks. Also, after moving the axes, the developer has to translate the dots in the scatter plot by the same amount as they translated the axes. Axes also didn't have enough features for customization. Axes didn't provide labels; I had to create them myself. I also couldn't find a way to define the amount that the axis ticks increased by. Apart from the trouble I had with the axis features, I found that d3 made it easy to dynamically create dots based on the dataset. Adding an attribute to the dots usually required only a few lines of code.

INSERT PICTURE HERE
![ggplot2](img/ggplot2.png)

# Matplotlib + Pandas
Matplotlib is a Python library that can create visualizations. Pandas is a Python library used for creating and manipulating data tables.

I firstly used Pandas' read_csv() function to read the csv file. Then, I used its drop_na() function to filter out dataset entries with empty values. I then used Pandas' groupby() function to group the entries by manufacturer. After doing that, I used a list comprehension to convert each group gained from groupby() into a dataframe for that group. For each group, I used dataframe.plot.scatter() (which uses matplotlib) to plot a scatter plot for each group in its respective color.

Creating a visualization very quick and simple to set up. By default, the axes had labels and didn't start from zero. Changing the size, color, and opacity of the dots was as simple as adding arguments to the call to dataframe.plot.scatter(). Changing the tick values was also easy to do, as I only needed to call ax.set_xticks() or ax.set_yticks().

![matplotlib](python/vis.png)

## Technical Achievements
- **Proved P=NP**: Using a combination of...
- **Solved AI Forever**: ...

### Design Achievements
- **Re-vamped Apple's Design Philosophy**: As demonstrated in my colorscheme...
