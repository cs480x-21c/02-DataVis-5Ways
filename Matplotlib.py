import pandas
import numpy as np
import matplotlib.pyplot as plt

manufacturers = {"bmw": "#F3B6B3", "ford": "#CCCD8E", "honda": "#93D8BA", "mercedes": "#93D2F4", "toyota": "#EDB0F2"}
data = pandas.read_csv("cars-sample.csv")
data.drop(data.loc[data["MPG"] == "NA"].index, inplace=True)
data.drop(data.loc[data["Weight"] == "NA"].index, inplace=True)
data["size"] = data["Weight"] / 10
data["color"] = data["Manufacturer"].map(manufacturers)
print(data.head(5))
plt.scatter("Weight", "MPG", data=data, s="size", alpha=0.5, c="color")
plt.xlabel("Weight")
plt.ylabel("MPG")
plt.savefig("img/matplotlib.png")
plt.show()
