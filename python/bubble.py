from pylab import *
from scipy import *
import pandas as pd
import numpy
import plotly.express as px

df = pd.read_csv(r'cars-sample.csv')

""" fig = px.scatter(df, x="Weight", y="MPG",
                 color="Manufacturer",
                 size='Weight',
                 hover_data=['Weight'])

fig.show() """


x = []
y = []
color = []
area = []
counter = zeros(97)

for i in counter:
    x.append(df['Weight'])  # weight
    y.append(df['MPG'])  # mpg
   # color.append(df['Manufacturer'])  # menufacturer
    area.append(df['Weight']*0.1)  # weight

# making the scatter plot
sct = scatter(x, y, s=area, linewidths=2, edgecolor='w')
sct.set_alpha(0.75)

axis([1500, 5000, 10, 45])
xlabel('Weight')
ylabel('MPG')
show()

_manufacturers = ['bmw', 'ford', 'honda', 'mercedes', 'toyota']

""" # create data
x = df['Weight']
y = df['MPG']
z = df['Weight']
# colors = numpy.random.choice(_manufacturers, size=97)
# use the scatter function
# plt.scatter(x, y, s=z*0.1, c=colors)
plt.scatter(x, y, s=z*0.1) """
# plt.show()
