import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

cars = pd.read_csv( '../cars-sample.csv' )

cars.dropna(inplace=True)

plt.figure( figsize=( 15, 10 ) )
plt.title( 'Weight vs. MPG' )
plt.xticks(np.arange(1000, 5050, 1000.0))
plt.yticks(np.arange(10, 50, 10.0))
sns.scatterplot( data=cars, x='Weight', y='MPG', size='Weight',
            sizes=(40, 400), alpha=.5, hue='Manufacturer' )
plt.savefig( '../img/py' )

plt.figure( figsize=( 15, 10 ) )
plt.title( 'Weight vs. MPG with Regression' )
plt.xticks(np.arange(1000, 5050, 1000.0))
plt.yticks(np.arange(10, 50, 10.0))
sns.regplot( data=cars, x='Weight', y='MPG' )
plt.savefig( '../img/py_regression' )

plt.figure( figsize=( 15, 10 ) )
plt.title( 'Weight vs. MPG with Logx Regression' )
plt.xticks(np.arange(1000, 5050, 1000.0))
plt.yticks(np.arange(10, 50, 10.0))
sns.regplot( data=cars, x='Weight', y='MPG', logx=True )
plt.savefig( '../img/py_logx' )
