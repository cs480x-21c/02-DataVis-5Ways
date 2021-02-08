import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('../cars-sample.csv')
df = df.dropna()

group_by = df.groupby('Manufacturer')
groups = [group_by.get_group(x) for x in group_by.groups]
colors = ['red','yellow', 'green', 'blue', 'violet']
ax = None

for group, color in zip(groups, colors):
    if ax is None:
        ax = group.plot.scatter(x='Weight', y='MPG', s=pow((group['Weight'] / 750 )* 2, 2), color=color, alpha=0.5)
    else:
        ax = group.plot.scatter(x='Weight', y='MPG', s=pow((group['Weight'] / 750 )* 2, 2), ax=ax, color=color, alpha=0.5)

ax.set_xticks([2000,3000,4000,5000])
ax.set_yticks([10,20,30,40])

#plot = df.plot.scatter(x='Weight', y='MPG', s=pow((df['Weight'] / 750 )* 2, 2))
plt.show()
