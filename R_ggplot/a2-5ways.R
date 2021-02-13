#Import data
library(ggplot2)

#Take in the data
cars <- read.csv("cars-sample")

#Make the graph and plot points
ggplot(cars, aes(y=MPG, x=Weight, color=Manufacturer)) + geom_point(aes(size = Weight), alpha = 0.5)
