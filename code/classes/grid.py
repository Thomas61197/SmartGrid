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
        Load all the houses onto the grid.
        """
        # nodes = {}
        # with open(source_file, 'r') as in_file:
        #     reader = csv.DictReader(in_file)

        #     for row in reader:
        #         nodes[row['id']] = Node(row['id'], row['id'])

        # return nodes
        pass

    def load_batteries(self, battery_file):
        """
        Load all the batteries onto the grid.
        """
        pass

    def add_cable(self, cable):
        """
        add a cable to the grid.
        """
        pass