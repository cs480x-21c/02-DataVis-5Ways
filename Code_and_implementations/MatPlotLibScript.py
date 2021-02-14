import matplotlib.pyplot as plt
import numpy as np

w = 4
h = 4
d = 300
plt.figure(figsize=(w, h), dpi=d)
cardata = np.genfromtxt(
    "cars-sample.csv", names=True,
    dtype="float", delimiter=",")

s = [n * 0.03 for n in cardata["Weight"]]
colors = ["#00008B",
          "#003EFF",
          "#00611C",
          "#00AF33",
          "#00CD00",
          "#00CED1",
          "#659D32",
          "#660198",
          "#68228B",
          "#687E5A",
          "#68838B",
          "#691F01",
          "#964514"]

mans = []

for man in cardata["Manufacturer"]:
    if str(man) != 'nan':
        if mans.index(man) != -1:
            mans.append(man)

plt.scatter(cardata["Weight"], cardata["MPG"], s=s, alpha=0.5)

plt.xlabel('Weight')
plt.xticks([2000,3000,4000,5000])
plt.ylabel('MPG')
plt.yticks([10,20,30,40,50])
plt.savefig("out.png")