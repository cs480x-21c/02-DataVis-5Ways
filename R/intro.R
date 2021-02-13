library(tidyverse)
cars <- read_csv("../cars-sample.csv")
head(cars)
ggplot(cars, aes(x = Weight, y = MPG, color= Manufacturer, size=Weight)) + geom_point(alpha = 0.5)

#source("intro.r", echo = TRUE)
