library(ggplot2)

source("rscript.R")
setwd("C:/Users/PJ-Mara/Desktop/College\ Files/Senior\ Year/C\ Term/Data\ Vis/02-DataVis-5Ways/r-ggplot")
carData <- read.csv("./cars-sample.csv")

View(carData)

ggplot(data=carData, mapping = aes(x=Weight, y=MPG, colour=Manufacturer, cex=Weight))+geom_point(alpha=0.4)

       