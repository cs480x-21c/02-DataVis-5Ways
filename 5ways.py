import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing

data = pd.read_csv('cars-sample.csv')

x = data[['Weight']] #ref: https://chrisalbon.com/python/data_wrangling/pandas_normalize_column/
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
data['Bubble Size'] = (x_scaled * 200) + 10

colors = {
	'ford': "#4e79a7",
	'toyota': "#f28e2c",
	'bmw': "#e15759",
	'honda': "#76b7b2",
	'mercedes': "#59a14f"
}

data['Color'] = data['Manufacturer'].map(colors)

ax = data.plot.scatter(
	x='Weight',
	y='MPG',
	c='Color',
	s='Bubble Size',
	alpha=0.5)

fig = ax.get_figure()

markers = [plt.Line2D([0],[0], color=color, marker='o', linestyle='', alpha=0.5) for color in colors.values()] #ref: https://stackoverflow.com/questions/31303912/matplotlib-pyplot-scatterplot-legend-from-color-dictionary
plt.legend(markers, colors.keys(), title="Manufacturer")

fig.savefig('img/matplotlib.png')
