# Libraries
library(ggplot2)

cs = read.csv("C://Users//Hauptfeld//Documents//GitHub//02-DataVis-5Ways//cars-sample.csv", header = TRUE)


ggplot(cs, aes(x=Weight, y=MPG, size=Weight, color=Manufacturer)) +
geom_point(alpha=0.7)
