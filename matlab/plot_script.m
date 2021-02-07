a= readtable('cars-sample.csv');
toDelete = isnan(a.MPG);
a(toDelete,:) = [];
colorgroup = zeros(length(a.MPG),1);
for i = 1:length(a.MPG)
    if strcmp(a.Manufacturer(i),'ford')
          colorgroup(i)=1;  
    elseif strcmp(a.Manufacturer(i),'bmw')
          colorgroup(i)=2;  
    elseif strcmp(a.Manufacturer(i),'toyota')
          colorgroup(i)=3;  
    elseif strcmp(a.Manufacturer(i),'honda')
          colorgroup(i)=4;   
    elseif strcmp(a.Manufacturer(i),'mercedes')
          colorgroup(i)=5;  
    end
end
bubblechart(a.Weight,a.MPG,a.Weight,colorgroup);
xlabel('Weight');ylabel('MPG (Miles/Gallon)');xlim([1500 5100]);ylim([5 52]);
bubblesize([5 15]);

