import csv

with open ('cars-sample.csv') as csvfile:
    cars = list(csv.reader(csvfile))

cars.pop(0)
print(cars)

import matplotlib.pyplot as plt

fig = plt.figure()


carWeight = []
carManufacturer = []

def toNum(numIn):
    if(numIn=='NA'):
        return 0
    else:
        return float(numIn)

def columnNum(matrix, i):
    return [toNum(row[i]) for row in matrix]

def column(matrix, i):
    return [row[i] for row in matrix]

carMPG = columnNum(cars, 3)
print(carMPG)

carWeight = columnNum(cars, 7)
print(carWeight)

carManufacturer = column(cars, 2)
print(carManufacturer)

#removing "NA" points


weightSize = []
for x in carWeight:
    weightSize.append(x/30)

color = []
for x in carManufacturer:
    if(x=='bmw'):
        color.append('darkblue')
    elif (x=='ford'):
        color.append('lightblue')
    elif (x=='honda'):
        color.append('green')
    elif (x=='mercedes'):
        color.append('gold')
    elif (x=='toyota'):
        color.append('red')

plt.scatter(carWeight, carMPG, s=weightSize, c=color, alpha=0.5)
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.show()
