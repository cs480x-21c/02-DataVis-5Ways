import matplotlib.pyplot as plt
plt.switch_backend('WXAgg')
import csv
import pandas as pd

Manufacturer = []
MPG = []
Weight = []
with open('cars-sample.csv', 'r') as csv_file:
	data = csv.reader(csv_file, delimiter = ',')
	for row in data:
		Manufacturer.append(row[2])
		MPG.append(row[3])
		Weight.append(row[7])

	Manufacturer.pop(0)
	MPG.pop(0)
	Weight.pop(0)

	df = pd.DataFrame({
		'Manufacturer' : Manufacturer,
		'MPG' : MPG,
		'Weight' : Weight})

	plt.scatter(Weight, MPG, data=df)
	plt.xlabel('Weight', size=16)
	plt.ylabel('MPG', size=16)
