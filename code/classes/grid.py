import csv

import numpy as np
from .battery import Battery
from .house import House
from .cable import Cable

class Grid():
    def __init__(self, house_file, battery_file):
        self.houses = self.load_houses(house_file)
        self.batteries = self.load_batteries(battery_file)

    def load_houses(self, house_file):
            """
            Load the position of the houses and their max output.
            """

            houses = {}

            with open(house_file, 'r') as in_file:
                reader = csv.DictReader(in_file)

                for count, row in enumerate(reader):
                    # Create house object
                    houses[count] = House(int(row['x']), int(row['y']), float(row['maxoutput']), count)

            return houses

    def load_batteries(self, battery_file):
            """
            Load the positions of all the batteries.
            """
            batteries = {}

            with open(battery_file, 'r') as in_file:
                reader = csv.DictReader(in_file)

                for count, row in enumerate(reader):
                    coordinates = row['positie'].split(',')
                    batteries[count] = Battery(int(coordinates[0]), int(coordinates[1]), float(row['capaciteit']), count)

            return batteries

    def calc_cost(self):
        tot = 0
        
        for house in self.houses.values():
            tot += house.cable.cost()
        
        return tot



    def calc_cost2(self):
        ''' 
        Calculating the cost of cables without duplicates.
        Initialise empty grid represented as a matrix filled with zeros
        Cables are added as ones in matrix at the corresponding coordinates, duplicate cables are not accepted. 
        '''

        tot = 0
        matrix = np.zeros( (50, 50), dtype=int )

        for house in self.houses.values():
            for x, y in zip(house.cable.x, house.cable.y):
                    matrix[x][y] = int(1)

        tot = np.count_nonzero(matrix == 1) * house.cable.cost_per_unit
                
        return tot
