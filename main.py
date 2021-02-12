import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("CS4802Project2 - cars-sample.csv")
plt.figure(figsize=(5, 5))
plt.scatter(df.Weight, df.MPG, s=df.Weight/10, c=df.ManufacturerNumber, alpha=0.5)
plt.xlabel("Weight")
plt.ylabel("MPG")
plt.ion()
plt.grid(b=True, which='major', color='#666666', linestyle='-')

plt.show()
