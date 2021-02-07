import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



data = pd.read_csv('../cars-sample.csv')

data = data.dropna(axis='index')
data



colors = {'ford': 'orange', 'bmw': 'red', 'honda': 'green', 'mercedes': 'blue', 'toyota': 'purple'}


plt.xlabel("Weight")
plt.ylabel("MPG")

plt.scatter(data['Weight'], data['MPG'], s=data['Weight']*0.02,alpha=0.5, c=data['Manufacturer'].map(colors))


plt.show()



