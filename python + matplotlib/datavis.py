import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt("../cars-sample.csv", delimiter=",", 
                     names=["", "car", "manufacturer", "mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "modelyear", "origin"])

plt.scatter(x = data['weight'], y = data['mpg'], s = data['weight']/20, alpha = 0.5)

plt.xlabel("Weight")
plt.ylabel("MPG")

plt.show()
