import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'cars-sample.csv')


def func(a):
    if "bmw" in a.lower():
        return "red"
    elif "ford" in a.lower():
        return "orange"
    elif "honda" in a.lower():
        return "yellow"
    elif "mercedes" in a.lower():
        return "green"
    elif "toyota" in a.lower():
        return "blue"
    else:
        return "gray"


df['Manufacturer-Colors'] = df.Manufacturer.apply(lambda x: func(x))


# create data
x = df['Weight']
y = df['MPG']
z = df['Weight']
colors = df['Manufacturer-Colors']

plt.scatter(x, y, s=z*0.1, c=colors, alpha=0.5)
plt.show()
