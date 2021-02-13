
library(ggplot2)

data <- read.csv("/Users/icalvaradoblanco/Desktop/datavis/02-DataVis-5Ways/cars-sample.csv",header = TRUE, sep =",")

ggplot(data, aes(x = Weight, y = MPG)) + geom_point(aes(colour = Manufacturer, size = Weight), alpha = 0.5)



