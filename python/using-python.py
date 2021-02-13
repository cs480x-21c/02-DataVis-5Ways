import matplotlib.pyplot as plt 
import matplotlib.colors
import pandas as pandas

data = pandas.read_csv('cars-sample.csv')
x = data['Weight']
y = data['MPG']
manufacturers=data['Manufacturer']

colors = {"bmw":"lightcoral","ford":"tab:green","honda":"green","mercedes":"cornflowerblue","toyota":"tab:pink"}
dictionary = pandas.DataFrame(dict(x=x,y=y,manufacturers = manufacturers))

fig, ax = plt.subplots()

ax.scatter(dictionary['x'],dictionary['y'],c=dictionary['manufacturers'].map(colors),s = dictionary['x']/15,alpha=0.5)
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.show()



