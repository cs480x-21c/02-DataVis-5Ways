
library(ggplot2)

data <- read.csv("cars-sample.csv",header = TRUE, sep =",")

ggplot(data, aes(x = Weight, y = MPG)) + geom_point(aes(colour = Manufacturer, size = Weight), alpha = 0.5)



