import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

w = 4
h = 4
d = 300
plt.figure(figsize=(w, h), dpi=d)
cardata = pd.read_csv("cars-sample.csv")

s = [n * 0.03 for n in cardata["Weight"]]

mans = []

for man in cardata["Manufacturer"]:
    if man not in mans:
        mans.append(man)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
colorMapping = []
for man in cardata["Manufacturer"]:
    colorMapping.append(colors[mans.index(man)])

cardata['ColorMappingMan'] = colorMapping

plt.scatter(cardata["Weight"], cardata["MPG"], s=s, alpha=0.5, c=cardata['ColorMappingMan'])

plt.xlabel('Weight')
plt.xticks([2000, 3000, 4000, 5000])
plt.ylabel('MPG')
plt.yticks([10,20,30,40])
plt.savefig("out.png")