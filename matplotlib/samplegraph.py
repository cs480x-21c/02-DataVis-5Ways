import matplotlib.pyplot as plt
import pandas
import math

def calculate_size_from_weight(weight):
    res = math.floor(weight/1000)
    if res == 1:
        return 18
    elif res == 2:
        return 30
    elif res == 3:
        return 45
    elif res == 4:
        return 65


data = pandas.read_csv("cars-sample.csv")
print(data)


fig, ax = plt.subplots()
colorMap = [[1,"bmw"], [2,"ford"],  [3,"mercedes"], 
            [4, "toyota"], [5, "honda"]]
colorDict = {}
manuDict = {}
for item in colorMap:
    colorDict[item[1]] = item[0]
    manuDict[item[0]] = item[1]

sizeMap = [[18, 1000], [30, 2000], [45, 3000], [65, 4000]]
sizesList = [18, 30, 45, 65]
sizeDict = {}
domainSizeDict = {}
for item in sizeMap:
    sizeDict[item[1]] = item[0]
    domainSizeDict[item[0]] = item[1]


weights = []
mpg = []
Manufacturer = []
sizes = []
for index, row in data.iterrows():
    weights.append(row["Weight"])
    mpg.append(row["MPG"])
    Manufacturer.append(colorDict[row["Manufacturer"]])
    sizes.append(calculate_size_from_weight(row["Weight"]))


scatter = plt.scatter(weights, mpg, c = Manufacturer, s = sizes, alpha=0.5)


handels, labels = scatter.legend_elements(prop="colors", alpha=0.7)
handelSize, labelSize = scatter.legend_elements(prop="sizes", alpha=0.7)
print(labelSize)

for i in range(1,6):
    labels[i-1] = labels[i-1].replace(str(i), manuDict[i])

for i in range(0, len(sizesList)):
    print()
    labelSize[i] = labelSize[i].replace(str(sizesList[i]), str(domainSizeDict[sizesList[i]]))

print(labelSize)
legend1 = ax.legend(handels, labels,
                    loc="upper right", title="Manufacturer")
ax.add_artist(legend1)
legend2 = ax.legend(handelSize, labelSize,
                    loc="center right", title="Weight")
#ax.add_artist(legend1)

plt.show()