import copy
import random
from code.classes import grid, house, battery, cable


class Fix_Greedy:
    """
    Take the outcome of the Greedy algorithm, and replace the houses of the batteries that are at max capacity.
    """

    def capacity_full(self):
        # Return the batteries that are at max capacity
        full_batteries = list()
        full_batteries.append([battery.id for battery in self.grid.batteries.values() if battery.capacity_left() < 0])
        return full_batteries

    def calc_distance(self, house_id, battery):
        # Calculate the distance between a house and a battery
        distance = abs(self.grid.houses[house_id].x - battery.x) + abs(self.grid.houses[house_id].y - battery.y)
        return distance

    def replacable_houses(self, battery_id):
        # Find the houses that would fix the surplus of current if replaced 
        battery = self.grid.batteries[battery_id]
        replacable_houses = list()
        replacable_houses.append([house for house_id in battery.houses if self.calc_distance(house_id, battery) > abs(battery.capacity_left())])   
        return replacable_houses

    # Optimalisatie stap: welk van die huizen kan het best worden verplaatst?

    def find_space(self, house_distance):
        # Find the batteries with enough space to take on the house of a full battery
        space_left = list()
        space_left.append([battery for battery in self.grid.batteries.values if battery.capacity_left >= house_distance])