library(ggplot2)
library(dplyr)

# Get and import the data
data_path <- file.path(getwd(), 'cars-sample.csv')
data <- read.table(data_path, header=TRUE, sep=",", stringsAsFactors = FALSE)

# Basic plot
ggplot(data, aes(x=Weight, y=MPG, size=Weight, color=Manufacturer)) + geom_point(alpha=0.5)

