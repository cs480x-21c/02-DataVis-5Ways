import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../cars-sample.csv')

colordict = {'bmw':'pink', 'ford':'orange', 'honda':'green', 'mercedes':'purple', 'toyota':'blue'}

fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(x = df['Weight'], y = df['MPG'], s = df['Weight']/10, c = df['Manufacturer'].map(colordict), alpha=0.5)
plt.xlabel("Weight")
plt.ylabel("MPG")

#Added legend for weight size
handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6)
legend2 = plt.legend(handles, labels, loc="upper right", title="Weight")

plt.show()
