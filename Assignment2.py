from matplotlib import pyplot as plt
import pandas as pd


# getting the data from the forked github content
cars = pd.read_csv('https://raw.githubusercontent.com/scvoltmer/02-DataVis-5Ways/main/cars-sample.csv')

# assigning  colors to the different car companies
colors = {'ford': 'red', 'bmw': 'green', 'honda': 'blue', 'mercedes': 'yellow', 'toyota': 'purple'}

#assigning variables
x = cars['Weight']
y = cars['MPG']

# creating scatterplot
# color mapping is done using viridis, which is the built in color map for the new-ish matplotlib
plt.scatter(x, y, s=(x/25), alpha=0.3, c=cars['Manufacturer'].map(colors), cmap='viridis')
plt.xlabel("Weight")
plt.ylabel("MPG")
plt.title("Car Weight vs. Car MPG")
# showing the scatterplot
plt.show()
