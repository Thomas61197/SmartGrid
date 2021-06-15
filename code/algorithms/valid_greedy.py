import copy
import random
from code.classes import cable

class Greedy:
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)

    def run(self):
        # sort houses from high to low max_output
        # attach the house to the battery with the lowest capacity_left()