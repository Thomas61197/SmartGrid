import copy
import random
from code.classes import grid, house, battery, cable

class Greedy_cheapest:
    """
    Calculates the shortest Manhattan distance from each house to a battery
    """
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)

    def get_distance_house(self):
        """
        Calculates the Manhattan distances from each house to a battery
        """
        # Create a dict with for each house a sorted dict of distance to each battery
        for house in self.grid.houses.values():
            distances = {}
            for battery in self.grid.batteries.values():
                distances[battery.id] = abs(house.x - battery.x) + abs(house.y - battery.y)
            # Sort distance from low to high
            house.battery_distances = sorted(distances.items(), key=lambda x: x[1])


    def battery_distance_list(self):
        """
        For each battery, make a sorted dict of connected houses and their distance from that battery
        """
        for battery in self.grid.batteries.values():

            for house in self.grid.houses.values():
                if house.battery_distances[0][0] is battery.id:
                    battery.add_house(house)
                
    def run_greedy(self): 
        """
        Find the houses with the shortest distance to their second closest battery, 
        connect if capacity of current battery is filled
        """
        # Sort distances from each house to each battery
        self.get_distance_house()

        # Add houses to their closest battery
        self.battery_distance_list()

        # Start laying cables
        for house in self.grid.houses.values():
            closest_battery_id = house.battery_distances[house.rank][0]
            closest_battery = self.grid.batteries[closest_battery_id]
            house.battery = closest_battery_id

            cable1 = cable.Cable(house = house, battery = closest_battery)
            cable1.lay_cable()
            house.add_cable(cable1)
            
