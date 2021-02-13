clc
clear all

load car-sample.mat

Weight = carssample.Weight;
MPG = carssample.MPG;

categories = unique(carssample.Manufacturer);
scatter(Weight, MPG);



for i = 1:length(categories)
    category = carssample(carssample.Manufacturer==categories(i),:);
    
    size = category.Weight.^2*0.00001;
    scatter(category.Weight, category.MPG, size, 'filled', 'MarkerFaceAlpha',.5,'MarkerEdgeAlpha',.5)

    hold on
    
end

legend(cellstr(categories))

ylim([8,48]);
set(gca,'YTick',[10 : 10 : 50]);

xlim([1200,5200]);
set(gca,'XTick',[2000 : 1000 : 5000]);

xtickangle(10)
ytickangle(10)
title('5 Ways')
xlabel('Weight')
ylabel('MPG')

grid minor
grid on
