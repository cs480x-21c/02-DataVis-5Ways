library(ggplot2)

# Run in the directory of this script

cars <- read.csv(file="../cars-sample.csv",head=TRUE,sep=",")

p <- ggplot(data=cars, mapping=aes(x=Weight, y=MPG, color=Manufacturer)) + 
    geom_point(aes(size=Weight), alpha=0.5)

print(p)