import random
import copy
from code.algorithms import baseline, greedy

class Simulated_annealing:
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)

    def run(self):
        # start off with a valid solution
        # can either be random or greedy
        
