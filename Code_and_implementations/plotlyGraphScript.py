import plotly.express as px
import numpy as np
import plotly.io as pio
pio.renderers.default = "browser"

cardata = np.genfromtxt(
    "cars-sample.csv", names=True,
    dtype="float", delimiter=",")

fig = px.scatter(cardata, x="Weight", y="MPG", color="Manufacturer",
                 size='Weight')
fig.update_yaxes(nticks=4)
fig.update_xaxes(nticks=5)
fig.show()