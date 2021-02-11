% Read in CSV
T = readtable('../cars-sample.csv');

% Remove irrelevant column containing extra NANs
T.Horsepower = [];

% Remove rows containing NAN 
T = rmmissing(T);

% Initalize tables
bmwTable = T;
fordTable = T;
hondaTable = T;
mercedesTable = T;
toyotaTable = T;

% Extract data per manufacturer to customize colors
bmwTable = separateData(bmwTable, "bmw", T);
fordTable = separateData(fordTable, "ford", T);
hondaTable = separateData(hondaTable, "honda", T);
mercedesTable = separateData(mercedesTable, "mercedes", T);
toyotaTable = separateData(toyotaTable, "toyota", T);

% Plot each manufacturer data
bmw = scatter(bmwTable.Weight, bmwTable.MPG, scaleSize(bmwTable.Weight), [1 0 0], "filled");
hold on
ford = scatter(fordTable.Weight, fordTable.MPG, scaleSize(fordTable.Weight), [0 1 0], "filled");
hold on
honda = scatter(hondaTable.Weight, hondaTable.MPG, scaleSize(hondaTable.Weight), [0 1 1], "filled");
hold on
mercedes = scatter(mercedesTable.Weight, mercedesTable.MPG, scaleSize(mercedesTable.Weight), [0 0 1], "filled");
hold on
toyota = scatter(toyotaTable.Weight, toyotaTable.MPG, scaleSize(toyotaTable.Weight), [1 1 0], "filled");
hold off 

% Opacity
bmw.MarkerFaceAlpha = 0.5;
ford.MarkerFaceAlpha = 0.5;
honda.MarkerFaceAlpha = 0.5;
mercedes.MarkerFaceAlpha = 0.5;
toyota.MarkerFaceAlpha = 0.5;

% Color
bmw.MarkerFaceColor = '#E46962';
ford.MarkerFaceColor = '#A9AA4B';
honda.MarkerFaceColor = '#4EBC8C';
mercedes.MarkerFaceColor = '#33ADEB';
toyota.MarkerFaceColor = '#DC78E3';

% Plot customization
xlabel('Weight');
ylabel('MPG');
xticks([2000, 3000, 4000, 5000]);
yticks([10, 20, 30, 40]);
set(gca, 'Color', '#ececec');

% Grid
ax = gca;
grid on;
ax.GridColor = 'w';
ax.GridAlpha = 1;

% Extract data of a specific manufacturer
function [table] = separateData (~, manufacturer, T)
    table = T;
    table(~ismember(table.Manufacturer, manufacturer),:)=[];
end

% Scale marker size in porportion to weight
function [size] = scaleSize (weight)
    size = (weight.^2)/50000;
end
