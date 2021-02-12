import pandas as pd
import matplotlib.pyplot as plt
import csv
import seaborn as sns

cars  = pd.read_csv("/Users/Pooja Patel/Documents/cars/cars-sample.csv")

fig = plt.gcf()
fig.set_size_inches( 12, 8)
ax=sns.scatterplot(x="Weight",y="MPG",hue="Manufacturer",size="Weight",sizes=(20,220),alpha=0.5,data=cars)
