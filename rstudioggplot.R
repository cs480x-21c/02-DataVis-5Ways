install.packages("ggplot2")
library(ggplot2)

##Read the CSV File
cardata <- read.csv("https://raw.githubusercontent.com/romanwicky/02-DataVis-5Ways/main/cars-sample.csv")

## Create the graph, guides(alpha=FALSE) turns off the alpha legend, not needed
graph <- ggplot(cardata, aes(y=MPG, x=Weight, size=Weight, color=Manufacturer, alpha=0.5)) + geom_point() +
  guides(alpha=FALSE)


graph