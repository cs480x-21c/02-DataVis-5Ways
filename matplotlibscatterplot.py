from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/romanwicky/02-DataVis-5Ways/main/cars-sample.csv')

# dictionary for colors
colors = {'ford': '#f7d434', 'bmw': '#e82c2c', 'honda': '#21de57', 'mercedes': '#21bfde', 'toyota': '#be21de'}


# creating scatterplot
plt.scatter(data['Weight'], data['MPG'], s=(data['Weight'] / 30), alpha=0.5, c=data['Manufacturer'].map(colors))
plt.xlabel("Weight")
plt.ylabel("Height")
plt.title("Weight vs. MPG")
# showing scatterplot
plt.show()

