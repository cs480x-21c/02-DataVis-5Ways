#install.packages("ggplot2", repos = "http://cran.us.r-project.org") # if not already installed
#install.packages("ggrepel", repos = "http://cran.us.r-project.org") # if not already installed

library(ggplot2)
library(ggrepel)

pdf(NULL)

data <- read.csv('./cars-sample.csv')

ggplot(data, aes(x=Weight, y=MPG, label=Car)) + geom_point(alpha=0.5, aes(size=Weight, color=Manufacturer)) + geom_label_repel(mapping=aes(label=Car, color=Manufacturer), size=2, label.size=NA, fill=NA, alpha=0.5, min.segment.length=0, force=5, max.overlaps=Inf)

# ref: http://www.sthda.com/english/wiki/ggplot2-scatter-plots-quick-start-guide-r-software-and-data-visualization
# ref: https://ggrepel.slowkow.com/articles/examples.html
# wow, that was easy

ggsave('./img/ggplot.png')
