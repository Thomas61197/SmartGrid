import pandas as pd
import matplotlib.pyplot as plt

from code.classes import grid, house, battery, cable


def visualise(grid): 

    # load data files
    district_number = 'small_test'
    battery_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_batteries.csv")
    house_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")

    dfhouses = pd.read_csv(house_file)
    dfhouses.plot(kind='scatter', x='x', y='y')

    dfbatteries =  pd.read_csv(battery_file)
    dfbatteries[['x','y']] = dfbatteries.positie.str.split(",",expand=True).astype(str).astype(int)

    # clear the figure
    plt.clf()

    # plot grid
    plt.title('SmartGrid')
    plt.grid(which='minor', color='lightgrey')
    plt.grid(which='major', color='grey')
    plt.minorticks_on()

    # plot battries and houses
    plt.scatter(dfbatteries['x'], dfbatteries['y'], color='orange', label = "Batteries")
    plt.scatter(dfhouses['x'], dfhouses['y'], color='blue', label = "Houses")

    # plot cables 
    for house in grid.houses.values():
        plt.plot(house.cable.x, house.cable.y, color="grey", linestyle="-")

    plt.legend()
    plt.show()
    plt.savefig("SmartGrid/docs/cable_visualisation.png")
    