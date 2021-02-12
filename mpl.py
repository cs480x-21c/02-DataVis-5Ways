import pandas as pd
from plotnine import ggplot, aes, geom_point
import matplotlib.pyplot as plt

df = pd.read_csv('cars-sample.csv')
print(df)
#
# ax1 = df.plot.scatter(x='Weight',
#                       y='MPG',
#                       c='Manufacturer',
#                       colormap='viridis')
(
ggplot(aes(x='Weight', y='MPG', color='Manufacturer'), data=df) + geom_point()
)
