install.packages("ggplot2")
library("ggplot2")

dat <- read.csv("/Users/danyabaron/Desktop/CS480x/02-DataVis-5Ways/cars-sample.csv")

print(dat)

# Create plot object
scatterGraph.plot <- ggplot(data = dat, 
                       mapping = aes(x = Weight, y = MPG)) +

geom_point(aes(size=Weight), color=Manufacturer, alpha=0.5) +
scale_color_manual(values = c("red", "orange", "forestgreen", "darkblue", "violet"))


# Draw plot
print(scatterGraph.plot)







