import csv

from .battery import Battery
from .house import House
from .cable import Cable

class Grid():
    def __init__(self, house_file, battery_file):
        self.houses = self.load_houses(self, house_file)
        self.batteries = self.load_batteries(self, battery_file)
    
def load_houses(self, house_file):
        """
        Load the position of the houses and their max output.
        """
        house_coordinatesX = {}
        house_coordinatesY = {}
        house_max_output = {}
        with open(house_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for count, row in enumerate(reader):
                house_coordinatesX[count+1] = row['x']
                house_coordinatesY[count+1] = row['x']
                house_max_output[count+1] = row['maxoutput']

        return house_coordinatesX, house_coordinatesX, house_max_output

def load_batteries(self, battery_file):
        """
        Load the positions of all the batteries.
        """
        batteriesX = {}
        batteriesY = {}
        batteries_capacity = {}
        with open(battery_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for count, row in enumerate(reader):
                coordinates = row['positie'].split(',')
                batteriesX[count+1] = coordinates[0]
                batteriesY[count+1] = coordinates[1]
                batteries_capacity[count+1] = row['capaciteit']

        return batteriesX, batteriesY, batteries_capacity

    def add_cable(self, cable):
        """
        add a cable to the grid.
        """
        pass