library(ggplot2)

cars = na.omit(read.csv("../cars-sample.csv", header=TRUE))

carplot <- ggplot( data = cars, aes( Weight, MPG) ) + geom_point( aes( size=cars$Weight, color=cars$Manufacturer, alpha=0.5) )

png('visualization_R.png')
print(carplot)
dev.off()
