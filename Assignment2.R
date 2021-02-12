#note that ggplot2 had been previously installed, so the install is not present in this code
library(ggplot2)

#sets the csv to a new variable d, gets the csv from the github file
d <- read.csv("https://raw.githubusercontent.com/scvoltmer/02-DataVis-5Ways/main/cars-sample.csv")
#color maping and graph creation
sp <- ggplot(d,aes(y=MPG,x=Weight,size=Weight,color=Manufacturer)) + geom_point(alpha = 0.5) + scale_color_manual(values = c("#e1cdeb","#cacc93","#96d3bb","#90d2ef","#eabaef"))
#outputs the graph
print(sp)
