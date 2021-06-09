import random
import copy
from code.algorithms import baseline

class Simulated_annealing:
    def __init__(self, empty_grid):
        self.empty_grid = empty_grid

    def run(self):
        # repeat:
            # choose a random start state
            self.grid = copy.deepcopy(baseline.Baseline(self.empty_grid))

            # choose a starting temperature
            temp = 100

            # repeat N times:
            for i in range(20000):
                # make a small adjustment
                # okay so this part is 
                # when random() > chance(old, new, temperature):
                    # revert adjustment
                # lower temperature

