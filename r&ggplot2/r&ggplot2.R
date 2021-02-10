library(ggplot2)
csvdata = read.csv("./GitHub/02-DataVis-5Ways/cars-sample.csv")
attach(csvdata)

ggplot(data=csvdata, mapping=aes(x=Weight, y=MPG, colour=Manufacturer, size=Weight))+geom_point()+scale_color_manual(values=c("#648FFF7F", "#785EF07F", "#DC267F7F", "#FE61007F", "#FFB0007F"))
