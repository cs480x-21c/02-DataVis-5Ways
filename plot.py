import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

df = pd.read_csv("cars-sample.csv")

size = []
for weight in df['Weight']:
    size.append(math.floor(weight/1000.0))

# colors = ['b', 'g', 'r', 'c', 'm']

data = pd.DataFrame({"Weight":df['Weight'], "MPG": df['MPG'], "Size": size, "Manufacturer": df['Manufacturer']})
groups = data.groupby("Manufacturer")

# def getColor(manu):
#     if(manu == "honda"):
#         return colors[0]
#     elif(manu == "ford"):
#         return colors[1]
#     elif(manu == "mercedes"):
#         return colors[2]
#     elif(manu == "toyota"):
#         return colors[3]
#     else:
#         return colors[4]

# counter = 0
# for weight in data['Weight']:
#     print(weight)
#     plt.plot(weight, data['MPG'][counter], marker="o", linestyle="", label=data['Manufacturer'][counter], markersize=data['Size'][counter], markerfacecolor=getColor(data['Manufacturer'][counter]))
#     counter += 1


for name, group in groups:
    plt.plot(group['Weight'], group['MPG'], marker="o", linestyle="", label=name)

plt.legend()
plt.show()