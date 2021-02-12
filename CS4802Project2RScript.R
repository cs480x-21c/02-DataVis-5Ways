library("ggplot2")
d <- read.csv("D:\\GitProjects\\02-DataVis-5Ways\\cars-sample.csv")
sp <- ggplot(d,aes(y=MPG,x=Weight,size=Weight,color=Manufacturer)) + geom_point(alpha = 0.5) + scale_color_manual(values = c("#4e79a7","#f28e2c","#e15759","#76b7b2","#59a14f"))
sp
