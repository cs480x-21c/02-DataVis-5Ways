# Loading ggplot2 Libary
library('ggplot2')

# Importing CSV file into R Studio
sample_car <- read.csv('cars-sample.csv')

ggplot(sample_car, aes(x=Weight, y=MPG, size=Weight, color=Manufacturer)) + geom_point(alpha= .5);
