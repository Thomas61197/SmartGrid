import copy
import random
from code.classes import cable

class Baseline:
    """
    Creates a cable between a randomly selected house and a randomly selected battery,
    taking into account the battery capacity
    """

    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)


    def run(self):
        random.shuffle(self.grid.houses)

        for house in self.grid.houses.values():
            random_battery = random.choice(self.grid.batteries)

            # cum_max_output = 1500 * 5 = 7500
            # cum_cap = 1507 * 5 = 7535
            # keep picking a random battery until you've found one that has enough space
            # while random_battery.capacity_left() < house.max_output:
            
            while random_battery.capacity_reached():
                random_battery = random.choice(self.grid.batteries)
            
            random_battery.add_house(house)
            cable1 = cable.Cable(house = house, battery = random_battery)
            cable1.lay_cable()
            house.add_cable(cable1)

