import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing

data = pd.read_csv('D:/EclipseWorkspace/02-DataVis-5Ways/Python/cars-sample.csv')
colors = {'bmw':'#f09f9e', 'ford':'c4c677', 'honda':'#90d5b8', 'mercedes':'#7accf5', 'toyota':'#ec9df2'}

x = data[['Weight']]
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
data['Bubble Size'] = (x_scaled * 200) + 10

data['Color'] = data['Manufacturer'].map(colors)

graph = data.plot.scatter(x='Weight', y='MPG', c='Color', s='Bubble Size', alpha=0.5)

markers = [plt.Line2D([0],[0], color=color, marker='o', linestyle='', alpha=0.5) for color in colors.values()]

graph.matplotlib.pyplot.show()

fig.savefig('/img/python.png')
