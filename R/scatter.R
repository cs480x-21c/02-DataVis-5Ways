library(ggplot2)
setwd(".")
data <- read.csv(file= "../cars-sample.csv")
scatter <- ggplot(data=data, mapping = aes(x=Weight, y=MPG, color = Manufacturer)) + geom_point(aes(size = Weight), alpha = 0.5)
print(scatter)



