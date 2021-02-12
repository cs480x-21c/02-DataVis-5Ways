
library(ggplot2)

cars <- read.csv("https://raw.githubusercontent.com/vygrasso/02-DataVis-5Ways/main/cars-sample.csv")

sp<-ggplot(cars, aes(y=MPG, x=Weight, size=Weight, color=Manufacturer)) +
    geom_point(alpha=0.5)

sp + scale_color_manual(values=c("#F79EE7", "#FF9333", "#20CD24", "#AF26AA", "#2131E7"))

