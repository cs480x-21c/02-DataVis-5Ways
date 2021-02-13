import matplotlib.pyplot as plt
import pandas as pd

# Read in carsSample CSV using pandas
df = pd.DataFrame(pd.read_csv(r'cars-sample.csv'))

manuColors = {"bmw": "b", "ford": "#ABFF4F", "honda": "#08BDBD", "mercedes": "#F21B3F", "toyota": "#FF9914"}
manufacturers = {"bmw", "ford", "honda", "mercedes", "toyota"}
scatter = plt.scatter(x=df.Weight, y=df.MPG, s=df.Weight/16, c=df.Manufacturer.map(manuColors),
                      label=df.Manufacturer, alpha=0.5)
plt.xlabel("Weight")
plt.ylabel("MPG")
plt.grid(True)
plt.show()