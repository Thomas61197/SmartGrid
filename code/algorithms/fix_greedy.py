import copy
import random
from code.classes import cable


class Fix_greedy:
    """
    Take the outcome of the Greedy algorithm, and replace the houses of the batteries that are at max capacity.
    """
    def __init__(self, grid):
        self.grid = grid

    def capacity_full(self):
        # Return the batteries that are at max capacity
        full_batteries = [battery for battery in self.grid.batteries.values() if battery.capacity_left() < 0]
        
        return full_batteries

    def calc_distance(self, house, battery):
        # Calculate the distance between a house and a battery
        distance = abs(house.x - battery.x) + abs(house.y - battery.y)
        
        return distance

    def replacable_houses(self, battery):
        # Find the houses that would fix the surplus of current if replaced 
        # a replacable house is a house whose output is larger or equal to the surplus capacity of a battery 
        # surplus = battery.get_cum_output() - battery.capacity == abs(battery.capacity_left())
        
        # replacable_houses = [house for house in battery.houses.values() if self.calc_distance(house, battery) > abs(battery.capacity_left())] 
        replacable_houses = list()

        for house in battery.houses.values():
            print("house max")
            print(house.max_output)
            print("cap left")
            print(float(abs(battery.capacity_left())))
            
            if house.max_output >= float(abs(battery.capacity_left())):
                replacable_houses.append(house)
                
        print('Replacable houses:', replacable_houses)
        return replacable_houses

    def find_space(self, house):
        # Find the batteries with enough space to take on the house of a full battery
        space_left = [battery for battery in self.grid.batteries.values() if battery.capacity_left() >= house.max_output]
        
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
            # while battery is not yet fixed
            while battery.capacity_reached() == True:

                optimal_replace_cost_per_house = {}

                # for each battery, for each replacable house, find space (i.e. find a battery with enough capacity left to add the house in question)             
                for house in battery.houses.values():
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

    def battery_most_space(self):
        space_left = {}
        for battery in self.grid.batteries.values():
            space_left[battery.id] = battery.capacity_left()

        space_left = {k: v for k, v in sorted(space_left.items(), key=lambda item: item[1])}    
        iterable_object = iter(space_left.keys())
        battery_most_space = self.grid.batteries[next(iterable_object)]
        
        return battery_most_space

    def run2(self):
        # for all full batteries
        for full_battery in self.capacity_full():
            # find the battery with the most space left
            battery_most_space = self.battery_most_space()
            fitting_houses = list()
            # from the houses connected to the full battery, find a house with a max output smaller or equal to the space that is left
            for house in full_battery.houses.values():
                
                if house.max_output <= battery_most_space.capacity_left():
                    fitting_houses.append(house)
                         
            # disconnect this house from the full battery and connect it to the battery with the most space left
            fitting_house = fitting_houses[0]
            
            # Remove found house from its current battery
            full_battery.remove_house(fitting_house)

            # Connect house to new battery
            battery_most_space.add_house(fitting_house)

            # replace cable
            cable1 = cable.Cable(fitting_house, battery_most_space)
            cable1.lay_cable()
            fitting_house.cable = cable1

    def run3(self):

        # while at least 1 battery is full
            # take the house with the largest max output from the battery with the most cumulative output
            # disconnect this house from the battery with the most cumulative output
            # add it to the battery with the lowest cumulative output

            # take the house with the smallest max output from the battery with the least cumulative output
            # disconnect this house from the battery with the least cumulative output
            # add it to the battery with the most cumulative output
        pass
                


