import pandas as pd
import matplotlib.pyplot as plt

from code.classes import grid, house, battery, cable



# def visulualise_cables(grid): 
    
# load data files
district_number = '1'
battery_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_batteries.csv")
house_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")

dfhouses = pd.read_csv(house_file)
dfhouses.plot(kind='scatter', x='x', y='y')

dfbatteries =  pd.read_csv(battery_file)
dfbatteries[['x','y']] = dfbatteries.positie.str.split(",",expand=True).astype(str).astype(int)



# ###################### cable ######################

# # visualise all cables in grid
# # for house in houses: 

# # plot cable start @house
# xh = grid.house(self.x)
# yh = grid.house(self.y)
# print(xh)
# print(yh)
# plt(xh, yh, color="red")


# # plot cable
# x_values = []
# y_values = []
# for i in range(len(house.cable.x)):
#     x_values.append(house.cable.x[i])
#     y_values.append(house.cable.y[i])
# # print(x_values)
# # print(y_values)
# plt(x_values, y_values, "bo-")

# # plot cable end @battery
# xb = grid.battery(self.x)
# yb = grid.battery(self.y)
# print(xb)
# print(yb)
# plt(xb, yb, color="green")


# ###################################################


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
plt.savefig("SmartGrid/docs/result.png")