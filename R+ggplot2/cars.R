#Install necessary package
install.packages("ggplot2")

#https://jcoliver.github.io/learn-r/004-intro-ggplot.html <-- Very helpful link
library("ggplot2")
cars <- read.csv("../cars-sample.csv")
ggplot(data=cars, mapping=aes(x=Weight, y=MPG, color=Manufacturer)) + geom_point(aes(size=Weight), alpha=0.5)
