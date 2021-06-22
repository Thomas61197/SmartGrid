import copy
import random
import math

from code.classes import cable
from code.algorithms import original_greedy

class Hill_climber:
    """
    The HillClimber class that changes a random node in the graph to a random valid value. Each improvement or
    equivalent solution is kept for the next iteration.
    """
    def __init__(self, grid, mutate_house_number = 1, cable_to_cable = True, fix = False):
        self.grid = grid
        self.mutate_house_number0 = mutate_house_number
        self.mutate_house_number = mutate_house_number
        self.cable_to_cable = cable_to_cable
        self.fix = fix

    def random_reconfigure_house(self, house, batteries):
        """
        take a house and connect it to a random (available) battery
        """
        # detach house from battery
        old_battery = house.cable.battery
        old_battery.remove_house(house)

        # remove cable
        house.cable = None

        # add house to new battery
        new_battery = random.choice(batteries)
        new_battery.add_house(house)
        cable1 = cable.Cable(house = house, battery = new_battery)

        if self.cable_to_cable:
            cable1.lay_cable_to_closest_cable()
        else:
            cable1.lay_cable()

        # add new cable and thus new battery to house
        house.add_cable(cable1)

    def mutate_single_house(self, new_grid):
        """
        Changes the connection of a random house to a battery with a random valid connection to a different battery.
        """
        random_house = random.choice(list(new_grid.houses.values()))
        available_batteries = list()

        for battery in new_grid.batteries.values():
            
            if not battery.capacity_reached():
                available_batteries.append(battery)

        if self.fix:
            self.random_reconfigure_house(random_house, list(new_grid.batteries.values()))
        else:
            self.random_reconfigure_house(random_house, available_batteries)

    def mutate_grid(self, new_grid):
        """
        Changes the value of a number of nodes with a random valid value.
        """
        for _ in range(math.ceil(self.mutate_house_number)):
            self.mutate_single_house(new_grid)

    def check_solution(self, new_grid, decreasing_mutate_house_number):
        """
        Checks and accepts better solutions than the current solution.
        """
        if self.cable_to_cable:
            new_cost = new_grid.calc_cost2()
        else:
            new_cost = new_grid.calc_cost()

        old_cost = self.cost

        if self.fix:
            # if current grid is invalid, accept any new grid that is valid, no matter the cost
            if not self.grid.is_valid():

                if new_grid.is_valid():
                    self.grid = new_grid
                    self.cost = new_cost

            # else, accept new_grid if valid and lower cost
            else:

                if new_grid.is_valid():

                    if new_cost <= old_cost:
                        self.grid = new_grid
                        self.cost = new_cost
        else:
            if new_cost <= old_cost:
                self.grid = new_grid
                self.cost = new_cost

    def run(self, iterations, verbose=False, decreasing_mutate_house_number = False):
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        Takes a filled in grid as starting grid
        """
        if self.cable_to_cable:
            self.cost = self.grid.calc_cost2()
        else:
            self.cost = self.grid.calc_cost()
            
        self.iterations = iterations

        for iteration in range(iterations):

            # Nice trick to only print if variable is set to True
            if self.fix:
                print(f'Iteration {iteration}/{iterations}, valid? {self.grid.is_valid()}, current cost: {self.cost}') if verbose else None
            
            else:
                print(f'Iteration {iteration}/{iterations}, current cost: {self.cost}') if verbose else None

            # Create a copy of the graph to simulate the change
            new_grid = copy.deepcopy(self.grid)

            self.mutate_grid(new_grid)

            # Accept it if it is better
            self.check_solution(new_grid, decreasing_mutate_house_number)

    

        