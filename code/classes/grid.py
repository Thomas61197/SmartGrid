import csv

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
                    # let's create the house objects right away
                    # let the id's start at 0
                    houses[count] = House(int(row['x']), int(row['y']), float(row['maxoutput']), count)

            # the output should be a dictionary ala {id: House (object)}
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

            # the output should be a dictionary ala {id: Battery (object)}
            return batteries

    def calc_cost(self):
        pass
        # tot = 0
        
        # for house in self.houses.values():
            # print(house.cable)
            # tot += house.cable.cost()
        
        # return tot