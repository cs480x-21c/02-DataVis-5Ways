library(ggplot2)
cars <- read.csv("cars-sample.csv")
ggplot(cars, aes(y=MPG, x=Weight, size=Weight, color=Manufacturer)) + 
  geom_point(alpha=0.5)

