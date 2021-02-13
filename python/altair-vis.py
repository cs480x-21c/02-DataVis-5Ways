import pandas
import altair as alt

alt.renderers.enable('mimetype')


data = pandas.read_csv('cars-sample.csv')
xdata = data['Weight']
ydata = data['MPG']
manufacturers=data['Manufacturer']
colors = ["lightcoral","olive","green","cornflowerblue","fuchsia"]
man_types = ["bmw","ford","honda","mercedes","toyota"]

dictionary = pandas.DataFrame(dict(Weight=xdata,MPG=ydata,Manufacturer = manufacturers))

chart = alt.Chart(dictionary).mark_circle(opacity=0.5).encode(x=alt.X('Weight', scale=alt.Scale(domain=(1500, 5000))),y='MPG', size = 'Weight:N',color= alt.Color('Manufacturer', scale=alt.Scale(domain=man_types, range=colors)))

chart.save('altair.html')
