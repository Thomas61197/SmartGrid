import pandas as pd
import matplotlib.pyplot as plt

from code.classes import grid, house, battery, cable



def visualise_cables(grid): 

    # load data files
    district_number = 'small_test' #!!!
    battery_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_batteries.csv")
    house_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")

    dfhouses = pd.read_csv(house_file)
    dfhouses.plot(kind='scatter', x='x', y='y')

    dfbatteries =  pd.read_csv(battery_file)
    dfbatteries[['x','y']] = dfbatteries.positie.str.split(",",expand=True).astype(str).astype(int)



    # ###################### cable ######################

    # # visualise all cables in grid
    # # for house in houses: 
    
    # visualise cable for 1 house
    house = grid.houses[1]

    x_values = []
    y_values = []
    # x_values = [2,1,1,0,0]
    # y_values = [1,1,2,2,3]
    for i in range(len(house.cable.x)):
        x_values.append(house.cable.x[i])
        y_values.append(house.cable.y[i])
    print(x_values)
    print(y_values)


    # ###################################################


    # plot data
    plt.clf()
    plt.title('SmartGrid')
    plt.scatter(dfbatteries['x'], dfbatteries['y'], color='orange', label = "Batteries")
    plt.scatter(dfhouses['x'], dfhouses['y'], color='blue', label = "Houses")


    ##################################
    plt.plot(x_values, y_values, 'g-')
    ##################################

    plt.grid(which='minor', color='lightgrey')
    plt.grid(which='major', color='grey')
    plt.minorticks_on()
    plt.legend()
    plt.show()
    plt.savefig("docs/result.png") ###!