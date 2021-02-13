install.packages(ggplot2)
library(ggplot2)

# Read CSV File
csvdata = read.csv("./cars-sample.csv")
attach(csvdata)

# Plot
ggplot(data=csvdata, mapping = aes(x = Weight, y = MPG, color = Manufacturer, size = Weight)) + geom_point() + scale_color_manual(values = c("red", "blue", "green", "orange", "purple"))




