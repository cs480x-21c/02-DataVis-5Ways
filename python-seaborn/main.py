import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os.path

def main():
    print("hello!")
    cars = pd.read_csv(os.path.dirname(__file__) + '/../cars-sample.csv')
    sns.relplot(x="Weight", y="MPG", data=cars, hue="Manufacturer", size="Weight", alpha=0.5)
    plt.show()

if __name__ == "__main__":
    main()
