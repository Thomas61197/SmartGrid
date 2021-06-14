import copy
import random
from code.classes import cable


class Fix_Greedy:
    """
    Take the outcome of the Greedy algorithm, and replace the houses of the batteries that are at max capacity.
    """
    def __init__(self, grid):
        self.grid = grid

    def capacity_full(self):
        # Return the batteries that are at max capacity
        full_batteries = list()
        full_batteries.append([battery for battery in self.grid.batteries.values() if battery.capacity_left() < 0])
        
        return full_batteries

    def calc_distance(self, house, battery):
        # Calculate the distance between a house and a battery
        distance = abs(house.x - battery.x) + abs(house.y - battery.y)
        
        return distance

    def replacable_houses(self, battery):
        # Find the houses that would fix the surplus of current if replaced 
        # a replacable house is a house whose output is larger or equal to the surplus capacity of a battery 
        # surplus = battery.get_cum_output() - battery.capacity
        replacable_houses = list()
<<<<<<< HEAD
        replacable_houses.append([house for house in battery.houses.values() if house.max_output >= abs(battery.capacity_left())])   
        
=======
        replacable_houses.append([house for house_id in battery.houses if self.calc_distance(house_id, battery) > abs(battery.capacity_left())])   
>>>>>>> 8152691717cde943eec66e3c80d821f27726851c
        return replacable_houses

    def find_space(self, house):
        # Find the batteries with enough space to take on the house of a full battery
        space_left = list()
        space_left.append([battery for battery in self.grid.batteries.values() if battery.capacity_left >= house.max_output])
        
        return space_left

    def calc_replace_cost(self, house, battery):
        # Look at the cost of replacing a house to a battery with space
        cost = self.calc_distance(house, battery) * house.cable.cost_per_unit

        return cost

    def run(self):
        """
        For each of the replacable houses, look whether they would fit in the capacity of another battery. 
        Pick the cheapest option. 
        """

        # first get the batteries that need to be fixed
        for battery in self.capacity_full():
            optimal_replace_cost_per_house = {}

            # for each battery, for each replacable house, find space (i.e. find a battery with enough capacity left to add the house in question)             
            for house in self.replacable_houses():
                batteries_with_space = self.find_space(house)
                print('Batteries with space:', batteries_with_space)
                replace_costs = {}
                
                for battery_with_space in batteries_with_space:
                    replace_costs[battery.id] = self.calc_replace_cost(house, battery_with_space)
                    
                replace_costs = {k: v for k, v in sorted(replace_costs.items(), key=lambda item: item[1])}    
                iterable_object = iter(replace_costs.keys())
                cheapest_battery = self.grid.batteries[next(iterable_object)]

                optimal_replace_cost_per_house[house.id] = replace_costs[cheapest_battery.id]

            # Choose optimal house for each battery
            optimal_replace_cost_per_house = {k: v for k, v in sorted(optimal_replace_cost_per_house.items(), key=lambda item: item[1])}    
            iterable_object = iter(optimal_replace_cost_per_house.keys())
            optimal_house = self.grid.houses[next(iterable_object)]
                    
            # Remove found house from its current battery
            battery.remove_house(optimal_house)

            # Connect house to new battery
            cheapest_battery.add_house(optimal_house)

            # replace cable
            cable1 = cable.Cable(optimal_house, cheapest_battery)
            cable1.lay_cable()
            optimal_house.cable = cable1
                


