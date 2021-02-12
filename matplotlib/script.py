import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#https://towardsdatascience.com/customizing-plots-with-python-matplotlib-bcf02691931f
#https://matplotlib.org/3.1.0/gallery/lines_bars_and_markers/scatter_with_legend.html
df = pd.read_csv("../cars-sample.csv")
df.reset_index(drop=True, inplace=True)
df.columns = [" ","Car","Manufacturer","MPG","Cylinders","Displacement","Horsepower","Weight","Acceleration","Model.Year","Origin"]
colors={
  "bmw" : "tab:blue",
  "ford" : "tab:orange",
  "honda" : "tab:green",
  "mercedes" : "tab:red",
  "toyota" : "tab:purple"
}

def scatterplot(df, x_dim, y_dim, colorKey):
  x = df[x_dim]
  y = df[y_dim]
  cr = df[colorKey]
  fig, ax = plt.subplots(figsize=(15, 15))
  scatter = ax.scatter(x, y, s=x*(x/70000), alpha=0.5, c=cr.map(colors), edgecolors="black")

  for key in colors:
    plt.scatter([], [], c=colors[key], alpha=0.7, s=200, label=str(key))
  legend1 = plt.legend(bbox_to_anchor=(1.01,1), borderaxespad=0, scatterpoints=1, frameon=True, labelspacing=1, title='Manufacturer', loc="upper left")
  ax.add_artist(legend1)

  kw = dict(prop="sizes", num=4, color=scatter.cmap(0), fmt="{x:.0f}",
            func=lambda s: np.sqrt(s*70000))
  legend2 = ax.legend(*scatter.legend_elements(**kw),bbox_to_anchor=(1.01,0), borderaxespad=0, labelspacing=1, loc="lower left", title="Weight")


  #adds a title and axes labels
  ax.set_title('')
  ax.set_xlabel('Weight')
  ax.set_ylabel('MPG')
  ax.grid(True)
  plt.show()
scatterplot(df, "Weight", "MPG", "Manufacturer")
