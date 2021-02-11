import pandas as pd
import matplotlib.pyplot as plt

# Reading in the CSV file
dataframe = pd.read_csv(r'cars-sample-python.csv')

# Acquire the min and max for the X and Y axis
maxMPG = dataframe.max(axis=0)['MPG']
minMPG = dataframe.min(axis=0)['MPG']

minWeight = dataframe.min(axis=0)['Weight']
maxWeight = dataframe.max(axis=0)['Weight']

# Using Weight and MPG to create Axis for the graph
xAxis = dataframe.Weight;
yAxis = dataframe.MPG;

# Setting Title of the Axis
plt.xlabel(dataframe.columns[7])
plt.ylabel(dataframe.columns[3])
plt.title("Data Viz 3: Matplotlib and Panda")

# Storing Manufacturer variable to aquire color
company = dataframe.Manufacturer;

# Getting color based on the manuf
color_dict = {'ford': 'red', 'bmw': 'blue', 'mercedes': 'orange', 'toyota': 'black', 'honda': 'green'}

plt.scatter(xAxis, yAxis, s=dataframe.Weight / 10, c=[color_dict[i] for i in company], alpha=.5)
plt.figure(figsize=(8, 8))
plt.show()
