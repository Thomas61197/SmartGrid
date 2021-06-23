import copy
import random
import math
import pickle

from code.classes import cable
from code.algorithms import original_greedy

class Hill_climber:
    """
    The HillClimber class that changes a random node in the graph to a random valid value. Each improvement or
    equivalent solution is kept for the next iteration.
    """
    def __init__(self, grid, mutate_house_number = 1, cable_to_cable = True, minimalize_surplus = False, with_checkpoints = False
    , lay_cable = None):
        self.grid = grid
        self.mutate_house_number0 = mutate_house_number
        self.mutate_house_number = mutate_house_number
        self.cable_to_cable = cable_to_cable
        self.minimalize_surplus = minimalize_surplus
        self.with_checkpoints = with_checkpoints
        self.lay_cable = lay_cable

    def random_reconfigure_house(self, house, batteries):
        """
        take a house and connect it to a random (available) battery
        """
        # detach house from battery
        old_battery = house.cable.battery
            
        old_battery.remove_house(house)

        # remove cable
        house.cable = None

        new_battery = random.choice(batteries)

        cable1 = cable.Cable(house = house, battery = new_battery)

        if self.cable_to_cable:
            
            if self.lay_cable == "to_random_house":
                cable1.lay_cable_to_random_house()
            else:
                cable1.lay_cable_to_closest_cable()
        else:
            cable1.lay_cable()

        # add new cable and thus new battery to house
        house.add_cable(cable1)

        # add house to new battery
        new_battery.add_house(house)

    def mutate_single_house(self, new_grid):
        """
        Changes the connection of a random house to a battery with a random valid connection to a different battery.
        """
        random_house = random.choice(list(new_grid.houses.values()))
        available_batteries = list()

        for battery in new_grid.batteries.values():
            
            if not battery.capacity_reached():
                available_batteries.append(battery)

        
        # print(f"available batteries: {available_batteries}")
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

        if self.minimalize_surplus:
            new_surplus = new_grid.calc_surplus()
            old_surplus = self.surplus

        if self.minimalize_surplus:
            # print(f"new_surplus: {new_surplus}")

            if new_surplus <= old_surplus and new_cost <= old_cost:
            # if new_surplus < old_surplus:
                self.grid = new_grid
                self.surplus = new_surplus
                self.cost = new_cost

        else:

            if new_cost <= old_cost:
                self.grid = new_grid
                self.cost = new_cost

        # new_grid.print_status_batteries()

    def run(self, iterations, verbose=False, decreasing_mutate_house_number = False):
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        Takes a filled in grid as starting grid
        """
        if self.cable_to_cable:
            self.cost = self.grid.calc_cost2()
        else:
            self.cost = self.grid.calc_cost()

        if self.minimalize_surplus:
            self.surplus = self.grid.calc_surplus()
            
        self.iterations = iterations
        self.cost_list = list()
        self.checkpoints = list(range(10000, self.iterations, 10000))

        for iteration in range(iterations):

            # Nice trick to only print if variable is set to True
            if self.minimalize_surplus:
                print(f'Iteration {iteration}/{iterations}, valid? {self.grid.is_valid()}, current surplus: {self.surplus}, current cost: {self.cost}') if verbose else None
                
            else:
                print(f'Iteration {iteration}/{iterations}, current cost: {self.cost}') if verbose else None

            # Create a copy of the graph to simulate the change
            new_grid = copy.deepcopy(self.grid)

            self.mutate_grid(new_grid)

            # Accept it if it is better
            self.check_solution(new_grid, decreasing_mutate_house_number)

            if self.with_checkpoints:

                if iteration in self.checkpoints and self.grid.is_valid():
                    file_name = f"SmartGrid/data/solutions/10k_or_greedy_ctc_dis1_{iteration}_hc_fix_ctc.pickle"

                    with open(file_name, 'wb') as handle:
                        pickle.dump(self, handle)
                    
                    print(f"checkpoint: {iteration}")
            
            
            self.cost_list.append(self.cost)

    

        