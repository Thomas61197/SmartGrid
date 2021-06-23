import pandas as pd
import matplotlib.pyplot as plt

from code.classes import grid, house, battery, cable

def visualise(grid, district_number, grid_name):

    # load data files
    # battery_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_batteries.csv")
    battery_file = (f"SmartGrid/data/Huizen&Batterijen/district_{district_number}/district-{district_number}_batteries.csv")
    # house_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")
    house_file = (f"SmartGrid/data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")

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
            gridcolor = "purple"

        plt.plot(house.cable.x, house.cable.y, color=gridcolor, linestyle="-")

    # plt.legend()
    plt.show()
    plt.savefig(f"SmartGrid/docs/final/district{district_number}/simulated_annealing/cable_visualisation_{grid_name}.png")
    # plt.savefig("docs/cable_visualisation.png")

def visualise_apart(grid, district_number, grid_name):
    """
    Visualise the connections of each battery in separate grids
    """

    for battery in grid.batteries.values():
        
        # Load house files
        house_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")
        # house_file = (f"SmartGrid/data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")
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
            gridcolor = "purple"

        # Plot cables 
        for house in battery.houses.values():
            plt.scatter(house.x, house.y, color="pink")
            plt.plot(house.cable.x, house.cable.y, color=gridcolor, linestyle="-")

        # plt.legend()
        plt.show()
        plt.savefig(f"docs/final/district{district_number}/cable_visualisation_battery{battery.id}_{grid_name}.png")




def visualise_empty_grid(grid, district_number):
    """
    Visualise the connections of each battery in separate grids
    """

    # load data files
    battery_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_batteries.csv")
    # battery_file = (f"SmartGrid/data/Huizen&Batterijen/district_{district_number}/district-{district_number}_batteries.csv")
    house_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")
    # house_file = (f"SmartGrid/data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")

    dfhouses = pd.read_csv(house_file)
    dfhouses.plot(kind='scatter', x='x', y='y')

    dfbatteries =  pd.read_csv(battery_file)
    dfbatteries[['x','y']] = dfbatteries.positie.str.split(",",expand=True).astype(str).astype(int)


    # Clear the figure
    plt.clf()

    # Plot gridlines
    plt.title(f'SmartGrid district {district_number}')
    plt.grid(which='minor', color='lightgrey')
    plt.grid(which='major', color='grey')
    plt.minorticks_on()

    
    # Plot each house and battery in the grid
    for battery in grid.batteries.values():
        # Give the connections of each battery a different colour
        if battery.id == 0:
            gridcolor = "white"
        elif battery.id == 1: 
            gridcolor = "red"
        elif battery.id == 2: 
            gridcolor = "orange"
        elif battery.id == 3: 
            gridcolor = "black"
        elif battery.id == 4: 
            gridcolor = "purple"


        plt.scatter(battery.x, battery.y, s=120, color=gridcolor, label = "Batteries")
    plt.scatter(dfhouses.x, dfhouses.y, s=30, color='blue', label = "Houses")

    plt.savefig(f"docs/greedy2_empty_dis{district_number}.png")

    
