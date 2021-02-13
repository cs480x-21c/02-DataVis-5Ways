#https://ggplot2.tidyverse.org/
library(ggplot2)
cars <- read.csv("cars-sample.csv")

ggplot(data = cars, aes(x=Weight, y=MPG, size=Weight, alpha=0.5, color=Manufacturer)) + geom_point()

ggsave("img/myGGplot.png")