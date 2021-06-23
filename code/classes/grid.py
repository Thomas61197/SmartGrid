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
                houses[count] = House(x = int(row['x']), y = int(row['y']), max_output = float(row['maxoutput']), id = count)

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
                # Create battery object
                batteries[count] = Battery(x = int(coordinates[0]), y = int(coordinates[1]), capacity = float(row['capaciteit']), id = count)

        return batteries

    def calc_cost(self):
        """
        Calculate the cost of a grid if houses have separate cables connecting them to batteries
        """
        tot = 0
        
        for house in self.houses.values():
            tot += house.cable.cost()
        for battery in self.batteries.values():
            tot += battery.cost
        
        return tot 

    def is_valid(self):
        """
        Returns True if all batteries are not at maximum capacity
        """
        valid = True

        for battery in self.batteries.values():

            if battery.capacity_reached():
                valid = False

        return valid

    def print_status_batteries(self):
        """
        Display the current cumulative output from houses to battery, and how much capacity is 'left'
        """
        for battery in self.batteries.values():
            print(f"battery_{battery.id}, cum_output: {battery.get_cum_output()}, capacity: {battery.capacity}\
, cum-cap: {battery.get_cum_output() - battery.capacity}")
            
    def calc_cost2(self):
        ''' 
        Calculating the cost of cables without duplicates per battery network.
        Initialise empty grid represented as a matrix filled with zeros
        Cables are added as ones in matrix at the corresponding coordinates, duplicate cables are not accepted. 
        '''
        for house in self.houses.values():
            house = house
            break

        tot = []
        
        for battery in self.batteries.values():
            matrix = battery.get_cable_matrix()
            # cost_per_matrix  = np.count_nonzero(matrix == 1) * battery.houses[house.id].cable.cost_per_unit + battery.cost
            cost_per_matrix  = np.count_nonzero(matrix == 1) * 9 + battery.cost
            tot.append(cost_per_matrix)

        return sum(tot)

    def calc_surplus(self):
        """
        Calculates the total surplus of capacity of all the batteries, 
        based on the max output of the houses connected to each battery
        """
        surplus = 0

        for battery in self.batteries.values():
            diff = battery.get_cum_output() - battery.capacity

            if diff > 0:
                surplus += diff
        
        return surplus

