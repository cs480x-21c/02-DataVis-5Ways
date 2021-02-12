import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/vygrasso/02-DataVis-5Ways/main/cars-sample.csv')

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x = df['Weight'], y = df['MPG'])
plt.xlabel("Weight")
plt.ylabel("MPG")

plt.show()
