cars = read.csv("C:\\WPI\\CS 480X\\Assignments\\Assignment 2\\02-DataVis-5Ways\\cars-sample.csv", header = TRUE)

# import library
library (ggplot2)

# building plot
ggplot(cars, aes(x=Weight, y=MPG)) + geom_point(aes(size=Weight, color=Manufacturer), alpha=0.5)