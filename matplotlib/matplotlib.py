import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Color dictionary
colors = {
    'bmw': '#E46962', 
    'ford': '#A9AA4B', 
    'honda': '#4EBC8C', 
    'mercedes': '#33ADEB', 
    'toyota': '#DC78E3'
    }

# Read in csv
data = pd.read_csv('cars-sample.csv')

# Plot points
plt.scatter(data.Weight, data.MPG, s=(data.Weight/400)**2, c=data.Manufacturer.map(colors), alpha=0.5)

# Axis labels
plt.xlabel("Weight")
plt.ylabel("MPG")

# Customize ticks
plt.xticks(np.arange(2000, 6000, 1000))
plt.yticks(np.arange(10, 50, 10))

plt.show()