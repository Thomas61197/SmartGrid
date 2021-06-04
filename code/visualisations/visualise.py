import pandas as pd
import matplotlib.pyplot as plt

# load data files
district_number = '1'
battery_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_batteries.csv")
house_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")

dfhouses = pd.read_csv(house_file)
dfhouses.plot(kind='scatter', x='x', y='y')

dfbatteries =  pd.read_csv(battery_file)
dfbatteries[['x','y']] = dfbatteries.positie.str.split(",",expand=True).astype(str).astype(int)

# plot data
plt.clf()
plt.title('SmartGrid')
plt.scatter(dfbatteries['x'], dfbatteries['y'], color='orange', label = "Batteries")
plt.scatter(dfhouses['x'], dfhouses['y'], color='blue', label = "dfHouses")

plt.grid(which='minor', color='lightgrey')
plt.grid(which='major', color='grey')
plt.minorticks_on()
plt.legend()
plt.show()
plt.savefig('result.png')