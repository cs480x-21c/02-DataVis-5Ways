install.packages("ggplot2")
library(ggplot2)

cars <- read.csv("./cars-sample.csv")

ggplot(cars, aes(y=MPG, x=Weight, size=Weight)) +
    geom_point()

#ggsave("../img/ggplotcarsvisualization.png")
