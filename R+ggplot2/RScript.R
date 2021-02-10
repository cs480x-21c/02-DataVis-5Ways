library("ggplot2")
data <- read.csv(file = "data/cars-sample.csv")
ggplot(data, aes(y=MPG, x=Weight, size=Weight, color=Manufacturer)) + geom_point(alpha = 0.5)
ggsave('R+ggplot2.png')
