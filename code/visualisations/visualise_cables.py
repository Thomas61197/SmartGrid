import pandas as pd
import matplotlib.pyplot as plt

from code.classes import grid, house, battery, cable


def visualise(grid, district_number): 
    """
    Visualise the connections of each battery in one grid
    """

    # load data files
    district_number = district_number
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
        if house.cable.battery.id == 0:
            gridcolor = "blue"
        elif house.cable.battery.id == 1: 
            gridcolor = "red"
        elif house.cable.battery.id == 2: 
            gridcolor = "orange"
        elif house.cable.battery.id == 3: 
            gridcolor = "black"
        elif house.cable.battery.id == 4: 
            gridcolor = "gray"

        plt.plot(house.cable.x, house.cable.y, color=gridcolor, linestyle="-")

    # plt.legend()
    plt.show()

    # plt.savefig(f"SmartGrid/docs/cable_visualisation_{grid_name}.png")  
    plt.savefig("docs/cable_visualisation.png")

def visualise_apart(grid, district_number):
    """
    Visualise the connections of each battery in separate grids
    """

    for battery in grid.batteries.values():

        district_number = district_number
        
        # Load house files
        house_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")
        dfhouses = pd.read_csv(house_file)
        dfhouses.plot(kind='scatter', x='x', y='y')

        # Clear the figure
        plt.clf()

        # Plot gridlines
        plt.title('SmartGrid')
        plt.grid(which='minor', color='lightgrey')
        plt.grid(which='major', color='grey')
        plt.minorticks_on()

        # Plot each house and battery in the grid
        plt.scatter(battery.x, battery.y, color='orange', label = "Batteries")
        plt.scatter(dfhouses.x, dfhouses.y, color='blue', label = "Houses")

        # Give the connections of each battery a different colour
        if battery.id == 0:
            gridcolor = "blue"
        elif battery.id == 1: 
            gridcolor = "red"
        elif battery.id == 2: 
            gridcolor = "orange"
        elif battery.id == 3: 
            gridcolor = "black"
        elif battery.id == 4: 
            gridcolor = "gray"

        # Plot cables 
        for house in battery.houses.values():
            plt.scatter(house.x, house.y, color="pink")
            plt.plot(house.cable.x, house.cable.y, color=gridcolor, linestyle="-")

        # plt.legend()
        plt.show()
        plt.savefig(f"docs/cable_visualisation_battery{battery.id}.png")


def visualise_house_apart(grid, district_number):
    """
    Visualise the connections of each house connected to battery 0 in separate grids
    """
    battery = grid.batteries[0]
    for house in battery.houses.values():
        if house.id < 30:

            district_number = district_number
            # Load house files
            house_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")
            dfhouses = pd.read_csv(house_file)
            dfhouses.plot(kind='scatter', x='x', y='y')

            # Clear the figure
            plt.clf()

            # Plot gridlines
            plt.title(f'SmartGrid house {house.id}')
            plt.grid(which='minor', color='lightgrey')
            plt.grid(which='major', color='grey')
            plt.minorticks_on()

            # Plot each house and battery in the grid
            plt.scatter(battery.x, battery.y, color='orange', label = "Batteries")
            plt.scatter(dfhouses.x, dfhouses.y, color='blue', label = "Houses")

            # Give the connections of each battery a different colour
            if battery.id == 0:
                gridcolor = "blue"
            elif battery.id == 1: 
                gridcolor = "red"
            elif battery.id == 2: 
                gridcolor = "orange"
            elif battery.id == 3: 
                gridcolor = "black"
            elif battery.id == 4: 
                gridcolor = "gray"

            # Plot cables 

            plt.scatter(house.x, house.y, color="pink")
            plt.plot(house.cable.x, house.cable.y, color=gridcolor, linestyle="-")

            # plt.legend()
            plt.show()
            plt.savefig(f"docs/cable_visualisation_house{house.id}.png")
            print(house.id, 'coordinates', house.x, house.y)
            print(battery.id, 'coordinates', battery.x, battery.y)
            print(house.id, 'cable', house.cable.x, house.cable.y)
    
