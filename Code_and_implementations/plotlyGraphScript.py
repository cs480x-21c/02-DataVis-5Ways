import plotly.express as px
import pandas as pd

cardata = pd.read_csv("cars-sample.csv")

s = [n * 0.03 for n in cardata["Weight"]]

mans = []

for man in cardata["Manufacturer"]:
    if man not in mans:
        mans.append(man)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
colorMapping = []
for man in cardata["Manufacturer"]:
    colorMapping.append(colors[mans.index(man)])

cardata['ColorMappingMan'] = colorMapping

fig = px.scatter(cardata, x="Weight", y="MPG", size='Weight', color="ColorMappingMan")
fig.update_layout(
    xaxis = dict(
        tickmode = 'array',
        tickvals = [2000, 3000,4000, 5000]
    ),
    yaxis = dict(
        tickmode = 'array',
        tickvals = [10, 20, 30, 40]
    )
)

fig.show()
