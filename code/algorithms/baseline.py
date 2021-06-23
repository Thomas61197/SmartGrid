import copy
import random
from code.classes import cable

class Baseline:
    """
    Creates a cable between a randomly selected house and a randomly selected battery one by one,
    taking into account the battery capacity
    """

    def __init__(self, empty_grid):
        """
        requires an empty grid to start with.
        """
        self.grid = copy.deepcopy(empty_grid)

    def run(self):
        """
        Randomly assigns houses to batteries with enough capacity left
        """
        random.shuffle(self.grid.houses)

        for house in self.grid.houses.values():

            random_battery = random.choice(self.grid.batteries)

            # keep choosing a random battery until you've found one that has enough space
            while random_battery.capacity_reached():
                random_battery = random.choice(self.grid.batteries)
            
            # If found, connect the house to that battery
            random_battery.add_house(house)
            house.battery = random_battery.id
            cable1 = cable.Cable(house = house, battery = random_battery)
            cable1.lay_cable()
            house.add_cable(cable1)


