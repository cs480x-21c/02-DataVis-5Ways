library(ggplot2)
library(tidyverse)
library(datasets)

cars_csv <- read.csv(file= "C:/Users/rin/Desktop/02-DataVis-5Ways-1/cars-sample.csv")
ggplot(cars_csv, aes(Weight, MPG, color=Manufacturer)) + geom_point(aes(size=Weight), alpha=0.5)

