
#install.packages("ggplot2");
library("ggplot2");

# creates the scatter plot
{
# read in the CSV
carSample <- read.csv(file.path("../cars-sample.csv"));

# filter out the NA MPGs
carSample <- carSample[!is.na(carSample$MPG), ];

carSamplePlot <- ggplot(carSample, aes(Weight, MPG));
# adds the color, size, and alpha
carSamplePlot + geom_point(aes(colour = Manufacturer, size = Weight), alpha = 0.5);
}
