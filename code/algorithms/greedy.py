import copy
import random
from code.classes import grid, house, battery, cable

class Greedy:
    """
    Calculats the shortest Manhattan distance from each house to a battery
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


    def replace_connections(self): 
        """
        Find the houses with the shortest distance to their next closest battery. 
        If the battery they're connected to now is full, replace that house to next closest battery.
        """

        random.shuffle(self.grid.batteries)

        for battery in self.grid.batteries.values():

            while battery.capacity_reached():

                # Make a dict of distances from houses to their next closest battery
                next_closest_battery_dict = {}
                for house in battery.houses:
                    house_obj = self.grid.houses[house]

                    # Pick the battery that is second closest after the one we're at now
                    if house_obj.rank < 4:
                        next_closest = house_obj.battery_distances[(house_obj.rank + 1)]
                        next_closest_battery_dict[house] = next_closest
                    # Go back to the beginning of the battery distance list
                    else:
                        house_obj.rank = 0
                        next_closest = house_obj.battery_distances[(house_obj.rank)]
                        next_closest_battery_dict[house] = next_closest


                # Sort that dict
                next_closest_battery_dict = sorted(next_closest_battery_dict.items(), key=lambda x: x[1])              
                # Indexing -> 1. First place in sorted dict 2. Want second item, tuple with battery id + distance to house
                # 3. We want the battery id
                replace_to_battery_id = next_closest_battery_dict[0][1][0]

                # Pick the house with the shortest distance to reconnect
                replace_house_id = next_closest_battery_dict[0][0]

                replace_house = self.grid.houses[replace_house_id]
                # Remove found house from current battery
                battery.remove_house(replace_house)
                # Indicate with rank that we've changed batteries
                replace_house.rank += 1
                # Add house to new battery 
                self.grid.batteries[replace_to_battery_id].add_house(replace_house)


    def run_greedy(self): 
        """
        Find the houses with the shortest distance to their second closest battery, 
        connect if capacity of current battery is filled
        """
        # Sort distances from each house to each battery
        self.get_distance_house()

        # Add houses to their closest battery
        self.battery_distance_list()

        # If battery capacity is full, reconnect houses with the shortest distance to the next battery
        for i in range(100):
            self.replace_connections()
            
        # Start laying cables
        for battery in self.grid.batteries.values():
            for house in battery.houses.values():
                house.battery = battery

                cable1 = cable.Cable(house = house, battery = battery)
                cable1.lay_cable()
                house.add_cable(cable1)



