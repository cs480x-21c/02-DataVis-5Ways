library(ggplot2)

car_data <- read.csv(file = "../cars-sample.csv",
                     stringsAsFactors = TRUE)

cars.plot <- ggplot(data=car_data,
                    mapping=aes(x=Weight, y=MPG)) +
      geom_point(aes(size = Weight, 
                     fill = Manufacturer), 
                 pch = 21,
                 alpha = 0.5)

print(cars.plot)