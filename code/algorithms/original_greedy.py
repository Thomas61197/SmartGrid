import copy
import random
from code.classes import cable

class Greedy:
    """
    for a house, finds the closest available battery and connects to it.
    """
    def __init__(self, empty_grid, cable_to_cable = True):
        """
        requires an empty grid to start with.
        if cable_to_cable is set to true, cables are attached to the closest cable connected to the same battery.
        """
        self.grid = copy.deepcopy(empty_grid)
        self.cable_to_cable = cable_to_cable

    def run(self):
        """
        runs the algorithm.
        """
        # otherwise the same result is produced every time
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
                
            closest_battery.add_house(house)
            house.battery = closest_battery.id
            cable1 = cable.Cable(house = house, battery = closest_battery)

            if self.cable_to_cable:
                cable1.lay_cable_to_closest_cable()
            else:
                cable1.lay_cable()

            house.add_cable(cable1)
