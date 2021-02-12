install.packages("ggplot2")
library("ggplot2")

cars-sample <- read.csv(file = '/cars-sample.csv')

ggplot(cars_sample, aes(x=Weight, y=MPG)) + geom_point()
ggplot(cars_sample, aes(x=Weight, y=MPG)) + geom_point(aes(size=Weight))

(cars_sample, aes(x=Weight, y=MPG)) + geom_point(aes(size=Weight,color=Manufacturer))
cars_sample, aes(x=Weight, y=MPG)) + geom_point(aes(size=Weight,color=Manufacturer))

geom_point(aes(size=Weight,color=Manufacturer))+geom_smooth(method=lm)
