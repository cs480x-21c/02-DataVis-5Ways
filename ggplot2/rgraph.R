library(ggplot2)

cars <- read.csv("cars-sample.csv")
carsClean <- filter (cars, !is.na(Weight) & !is.na(MPG))
notableCars <- filter (carsClean, Weight == max(Weight) | MPG == max(MPG))
ggplot(carsClean, aes(y=MPG, x=Weight, size=Weight, color=Manufacturer, shape=Origin)) + 
  geom_point(alpha=0.5) + geom_text(data = notableCars, aes(label = Car), vjust= 'inward', hjust='inward')
