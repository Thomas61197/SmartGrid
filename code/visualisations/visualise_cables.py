import pandas as pd
import matplotlib.pyplot as plt

from code.classes import grid, house, battery, cable


def visualise(grid): 

    # load data files
    district_number = '1'
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
        if house.battery == 0:
            gridcolor = "blue"
        elif house.battery == 1: 
            gridcolor = "red"
        elif house.battery == 2: 
            gridcolor = "orange"
        elif house.battery == 3: 
            gridcolor = "black"
        elif house.battery == 4: 
            gridcolor = "gray"

        plt.plot(house.cable.x, house.cable.y, color=gridcolor, linestyle="-")

    # plt.legend()
    plt.show()
    plt.savefig("docs/cable_visualisation.png")
<<<<<<< HEAD

def visualise_apart(grid):
        # plot battries and houses
    for battery in grid.batteries.values():
        # load data files
        district_number = '1'
        battery_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_batteries.csv")
        house_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")

        dfhouses = pd.read_csv(house_file)
        dfhouses.plot(kind='scatter', x='x', y='y')



        # clear the figure
        plt.clf()

        # plot grid
        plt.title('SmartGrid')
        plt.grid(which='minor', color='lightgrey')
        plt.grid(which='major', color='grey')
        plt.minorticks_on()


        plt.scatter(battery.x, battery.y, color='orange', label = "Batteries")
        plt.scatter(dfhouses['x'], dfhouses['y'], color='blue', label = "Houses")

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

=======
    
def visualise_apart(grid):
    # load data files
    district_number = '1'
    battery_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_batteries.csv")
    house_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")

    dfhouses = pd.read_csv(house_file)
    dfhouses.plot(kind='scatter', x='x', y='y')

    dfbatteries =  grid.batteries

    # clear the figure
    plt.clf()

    # plot grid
    plt.title('SmartGrid')
    plt.grid(which='minor', color='lightgrey')
    plt.grid(which='major', color='grey')
    plt.minorticks_on()

    # plot battries and houses
    for battery in grid.batteries.values():
        plt.scatter(battery.x, battery.y, color='orange', label = "Batteries")
        plt.scatter(dfhouses['x'], dfhouses['y'], color='blue', label = "Houses")

>>>>>>> 9d7b5d7c40669497af30828ee06892a6559960e4
        # plot cables 
        for house in battery.houses.values():
            

<<<<<<< HEAD
            plt.plot(house.cable.x, house.cable.y, color=gridcolor, linestyle="-")

        # plt.legend()
        plt.show()
        plt.savefig(f"docs/cable_visualisation{battery.id}.png")
    
=======
            plt.plot(house.cable.x, house.cable.y, color="red", linestyle="-")

        # plt.legend()
        plt.show()
        plt.savefig(f"docs/cable_visualisation{battery.id}.png")
>>>>>>> 9d7b5d7c40669497af30828ee06892a6559960e4
