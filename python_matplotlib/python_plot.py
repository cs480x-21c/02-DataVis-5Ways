import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)




df = pd.read_csv('cars-sample.csv')
manufactures = df['Manufacturer'].unique()

plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(10, 8))

for category in manufactures:
    data = df.loc[df['Manufacturer'] == category]
    print(data)
    size = data['Weight']**2 * 0.00004
    print(size)
    plt.scatter(data['Weight'], data['MPG'], s=size, alpha=0.5)

#https://stackoverflow.com/questions/24943991/change-grid-interval-and-specify-tick-labels-in-matplotlib
# the grid setting is from this website
ax.xaxis.set_major_locator(MultipleLocator(1000))
ax.yaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(AutoMinorLocator(4))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
ax.grid(which='major', color='#CCCCCC', linestyle='-')
ax.grid(which='minor', color='#CCCCCC', linestyle=':')
plt.legend(manufactures, title="Manufacturer", prop={"size": 20})

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel('Weight', fontsize=20)
plt.ylabel('MPG', fontsize=20)
plt.grid(True)

plt.show()
