install.packages("ggplot2")
library(ggplot2)

cars <- read.csv("../cars-sample.csv")

ggplot(diabetes, aes(y=glyhb, x=age, size=weight, color=frame)) +
    geom_point()

ggsave("../img/ggplotcarsvisualization.png")
