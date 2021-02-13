import csv
import math
import matplotlib.pyplot as plt
import numpy as np


def main():
    # Create lists to hold variables for plotting
    mpg = []
    weight = []
    color = []
    area = []

    # Load cars from CSV
    with open('cars-sample.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            if row[3] != "NA": # Filter out cars with N/A MPG
                mpg.append(float(row[3]))
                weight.append(float(row[7]))

                # Calculate color based off of manufacturer of car
                manufacturer = row[2]
                if manufacturer == "bmw":
                    color.append("#FF0000")
                elif manufacturer == "ford":
                    color.append("#83814D")
                elif manufacturer == "honda":
                    color.append("#00FF00")
                elif manufacturer == "mercedes":
                    color.append("#0099FF")
                elif manufacturer == "toyota":
                    color.append("#FF00FF")

                # Calculate area of dot based off of weight of car
                r = (float(row[7]) / 750)
                area.append(math.pi * (r ** 2))

    # Set plot x & y limits
    plt.xlim([1500, 5100])
    plt.ylim([8, 47])

    # Explicitly specify where to mark ticks on axes
    plt.xticks(np.arange(2000, 6000, 1000))
    plt.yticks(np.arange(10, 50, 10))

    # Set axis labels
    plt.xlabel("Weight")
    plt.ylabel("MPG")

    # Create scatter plot of data
    plt.scatter(weight, mpg, alpha=0.5, c=color, s=area)

    # Show image of plot
    plt.show()


if __name__ == "__main__":
    main()
