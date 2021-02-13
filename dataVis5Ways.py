import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


fig, ax = plt.subplots(figsize=(16,8))

# Read from CSV
df = pd.read_csv('cars-sample.csv', usecols=['Weight','MPG','Manufacturer'])

# Name the columns accordingly so the bubble plot can read it
df.rename(columns={'Manufacturer':'color','Weight':'X', 'MPG':'Y'}, inplace=True)

# Adjust bubble size by normalizing data
df['bubble_size'] = df['X']/df['X'].max() * 200

# Map manufacturers to color
df['color'] = df['color'].map({'ford':'red', 'toyota':'blue', 'bmw':'green', 'honda':'black', 'mercedes':'orange'})

weights = np.array(df['X'].values)
mpgs = np.array(df['Y'].values)
colorDict = {
    'ford':'red',
    'toyota':'blue',
    'bmw':'green',
    'honda':'black',
    'mercedes':'orange'
}

# Define bubble plot
bubblePlot = ax.scatter('X',
            'Y',
            s='bubble_size',
            c='color',
            alpha=0.5,
            data=df,
           label="ford")

# Set axis limits
ax.set_xlim([1400, 5100])
ax.set_ylim([8, 48])

# Show grid lines and define ticks
ax.grid(b=True, which='major', axis='both', color='#BBBBBB')
ax.grid(b=True, which='minor', axis='both', color='#DDDDDD')
ax.set_xticks([2000, 3000, 4000, 5000])
ax.set_xticks([1500, 2500, 3500, 4500], minor=True)
ax.set_yticks([10, 20, 30, 40])
ax.set_yticks([15, 25, 35, 45], minor=True)

ax.set_axisbelow(True)

# Edit axis labels and graph title
ax.set_xlabel("Weight", size=16)
ax.set_ylabel("MPG", size=16)
ax.set_title("MPG vs. Weight", size=18)

# Draw the plot on a GUI
plt.show()