import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print('hello')
data  = pd.read_csv("cars-sample.csv")

# df.plot()
# df.plot(kind='scatter',x='Weight',y='MPG')

colors = {'ford': '#a6e39f', 'bmw': 'red', 'honda': 'green', 'mercedes': '#92e0f0', 'toyota': '#f092ce'}

plt.xlabel("Weight")
plt.ylabel("MPG")
plt.scatter(data["Weight"], data["MPG"], s=(data["Weight"] / 25), alpha=0.5, c=data["Manufacturer"].map(colors))

plt.show()






















