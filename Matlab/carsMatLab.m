% https://www.mathworks.com/matlabcentral/answers/72545-how-to-import-csv-file-in-matlab
data = readtable("../cars-sample.csv");
delete = isnan(data.MPG);
data(delete,:) = [];
manufacturer = zeros(length(data.MPG),1);
for i = 1:length(manufacturer)
    if strcmp(data.Manufacturer(i), "bmw")
        manufacturer(i) = 1;
    elseif strcmp(data.Manufacturer(i), "ford")
        manufacturer(i) = 2;
    elseif strcmp(data.Manufacturer(i), "honda")
        manufacturer(i) = 3;
    elseif strcmp(data.Manufacturer(i), "mercedes")
        manufacturer(i) = 4;
    else
        manufacturer(i) = 5;
    end
end

s = scatter(data.Weight, data.MPG, .05*(data.Weight), manufacturer, "filled");
s.MarkerFaceAlpha = 0.5;
xlabel('Weight');
ylabel('MPG');
xlim([1250 5200]);
ylim([5 48]);
xticks(2000:1000:5000);
yticks(10:10:40);        