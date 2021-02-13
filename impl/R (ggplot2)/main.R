# Created based off of tutorial found here:
# http://r-statistics.co/Complete-Ggplot2-Tutorial-Part2-Customizing-Theme-With-R-Code.html

# Setup
library(ggplot2)
cars <- read.csv("cars-sample.csv")

# Add plot components
gg <- ggplot(cars, aes(x=Weight, y=MPG)) + 
  geom_point(alpha=0.5, aes(col=Manufacturer, size=Weight)) +
  labs(y="MPG", x="Weight")

# Call plot
plot(gg)
