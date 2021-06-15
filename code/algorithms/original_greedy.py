import copy
import random
from code.classes import cable

class Greedy:
    """
    Calculats the shortest Manhattan distance from each house to a battery
    """
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)

    def run(self):
        """
        Calculates the Manhattan distances from each house to a battery
        """
        random.shuffle(self.grid.houses)

        # Create a dictionary of all the houses with a list of the Manhattan distances to each battery
        for house in self.grid.houses.values():
            distances = {}

            for battery in self.grid.batteries.values():
                distances[battery.id] = abs(house.x - battery.x) + abs(house.y - battery.y)

            # Sort distance from low to high
            distances = {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}
            iterable_object = iter(distances.keys())
            closest_battery = self.grid.batteries[next(iterable_object)]

            # go until you find a battery that has not reached capacity yet
            while closest_battery.capacity_reached():
                closest_battery = self.grid.batteries[next(iterable_object)]

            # while closest_battery.capacity_left() < house.max_output:
            #     closest_battery = self.grid.batteries[next(iterable_object)]
                
            # if closest_battery.capacity_left() < house.max_output:
            closest_battery.add_house(house)
            cable1 = cable.Cable(house = house, battery = closest_battery)
            cable1.lay_cable()
            house.add_cable(cable1)
            # else:
            #     break
