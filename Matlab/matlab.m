Array=csvread('cars-sample.csv');
col1 = Array(:, 1);
col2 = Array(:, 2);
scatter(col1, col2)
xlabel('Weight')
ylabel('MPG')
