library(ggplot2)
library(ggrepel)

car_data <- read.csv(file = "D:/EclipseWorkspace/02-DataVis-5Ways/cars-sample.csv",
                     stringsAsFactors = TRUE)

cars.plot <- ggplot(data=car_data,
                    mapping=aes(x=Weight, y=MPG, size=Weight)) +
    geom_point(alpha=0.5, aes(size=Weight, color=Manufacturer))

print(cars.plot)
