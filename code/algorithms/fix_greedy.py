import copy
import random
from code.classes import grid, house, battery, cable


class Fix_Greedy:
    """
    Take the outcome of the Greedy algorithm, and replace the houses of the batteries that are at max capacity.
    """

    def capacity_bad(self):
        # Return the batteries that are at max capacity
        full_batteries = list()
        full_batteries.append([battery.id for battery in self.grid.batteries.values() if battery.capacity_left() < 0])
        return full_batteries

    def calc_distance(self, house_id, battery):
        # Calc the distance between a house and a battery
        distance = abs(self.grid.houses[house_id].x - battery.x) + abs(self.grid.houses[house_id].y - battery.y)
        return distance

    def replacable_houses(self, battery_id):
        # Find the houses that would fix the surplus of current if replaced 
        battery = self.grid.batteries[battery_id]
        replacable_houses = list()
        replacable_houses.append([house for house in battery.houses if self.distance(house, battery) > abs(battery.capacity_left())])   
