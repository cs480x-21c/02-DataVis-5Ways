import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

df = pd.read_csv('data/cars-sample.csv')
df = df.replace(to_replace =["bmw"],  value ="#ff0000")
df = df.replace(to_replace =["ford"],  value ="#ffff00")
df = df.replace(to_replace =["honda"],  value ="#00ff00")
df = df.replace(to_replace =["mercedes"],  value ="#0000ff")
df = df.replace(to_replace =["toyota"],  value ="#ff00ff")

bmw_patch = mpatches.Patch(color='#ff0000', label='bmw')
ford_patch = mpatches.Patch(color='#ffff00', label='ford')
honda_patch = mpatches.Patch(color='#00ff00', label='honda')
mercedes_patch = mpatches.Patch(color='#0000ff', label='mercedes')
toyota_patch = mpatches.Patch(color='#ff00ff', label='toyota')

scale = 0.1
df['Size'] = df["Weight"] * scale

plt.figure().set_facecolor("#b8c7cc")
plt.grid(which='major', axis='both', color='#b5b5b5', linestyle='-', linewidth=0.1)
scatter = plt.scatter(x='Weight', y='MPG', s='Size', c='Manufacturer', alpha=0.5, data=df)

plt.gca().set_facecolor("#636363")
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.legend(handles=[bmw_patch, ford_patch, honda_patch, mercedes_patch, toyota_patch])

plt.show()
