library(ggplot2)
dat <- read.csv("https://raw.githubusercontent.com/cs480x-21c/02-DataVis-5Ways/main/cars-sample.csv", header = TRUE)
ggplot(dat, aes(x = Weight, y = MPG)) + geom_point(aes(color = Manufacturer,size=Weight,alpha = 0.5)) + guides(alpha=FALSE)
ggsave("ggplot+R_Chart.png")
