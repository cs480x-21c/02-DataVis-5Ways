#Making the MPG vs Weight Graph with Python + matplotlib
import csv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#Establish variables
manufacturerData = []
weightData = []
MPGData = []

skipRow1 = 1;   #Ensures header details are not in the first row
color = 'red'   #Basic color declaration
count = 0;      #Incrementing variable used in legend and plot creation

#Read the data
with open('cars-sample.csv') as cars:
    reader = csv.reader(cars)

    for row in reader:
        #Add to the dataset
        if skipRow1 == 1:
            skipRow1 = 0
        else:

            if(str(row[7]) == 'NA' or str(row[3]) == 'NA'):
                continue
            else:
                weightData.append(float(row[7]))
                MPGData.append(float(row[3]))
                manufacturerData.append(row[2])

#Get the particular color for the manufacturer
manufacturers = {'bmw': 'red',
                 'ford': 'orange',
                 'honda': 'green',
                 'mercedes': 'blue',
                 'toyota': 'purple' }


#Making the Graph and plot points
fig, ax = plt.subplots()

for manufacturer in manufacturerData:
    #Get manufacturer and corresponding color
    color = manufacturers[manufacturer]
    
    #Plot each point
    ax.scatter(weightData[count], MPGData[count], c = color, s = (weightData[count]/15), alpha = 0.5)        
    count = count + 1

#Add legend for manufacturers
bmw_patch = mpatches.Patch(color='red', label='bmw')
ford_patch = mpatches.Patch(color='orange', label='ford')
honda_patch = mpatches.Patch(color='green', label='honda')
mercedes_patch = mpatches.Patch(color='blue', label='mercedes')
toyota_patch = mpatches.Patch(color='purple', label='toyota')

plt.legend(handles=[bmw_patch, ford_patch, honda_patch, mercedes_patch, toyota_patch])

#Add final details
ax.grid(True)
ax.set_yticks([5,10,20,30,40,50])
plt.xlabel("Weight")
plt.ylabel("MPG")

#Show the plot
plt.show()


