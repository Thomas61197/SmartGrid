import copy
import random
import math
import pickle

from code.classes import cable
from code.algorithms import original_greedy

class Hill_climber:
    """
    The Hill_climber class that changes a random node in the graph to a random valid value. Each improvement or
    equivalent solution is kept for the next iteration.

    The algorithm requires a fully filled in grid with cables where every house is connected to a battery.

    mutate_house_number is the number of houses of which its connections are changed.

    If cable_to_cable is set to True, houses are connected to the battery by laying a cable from the house to the closest cable that is connected
    to the chosen battery.

    If minimalize_surplus is set to True, the hill climber minimizes output surplus above battery capacity.

    If with_checkpoints is set to true, instances of the class itself are saved at certain iteration intervals. Make sure the files are saved under the correct name. 

    The lay_cable argument specifies how to lay the cable in case cable_to_cable is set to true. It can be "to_closest_cable" or "to_random_house".

    If minimalize_surplus is set to True and cost_and_surplus is set to True, the algorithm minimizes both cost and surplus.
    
    If decrease_mutate_house_number is set to true, it decreases the mutate_house_number linearly with each iteration.
    """
    def __init__(self, grid, mutate_house_number = 1, cable_to_cable = True, minimalize_surplus = False, with_checkpoints = False
    , lay_cable = None, cost_and_surplus = False, decreasing_mutate_house_number = False):
        self.grid = grid
        self.mutate_house_number0 = mutate_house_number
        self.mutate_house_number = mutate_house_number
        self.cable_to_cable = cable_to_cable
        self.minimalize_surplus = minimalize_surplus
        self.with_checkpoints = with_checkpoints
        self.lay_cable = lay_cable
        self.cost_and_surplus = cost_and_surplus
        self.decreasing_mutate_house_number = decreasing_mutate_house_number

    def random_reconfigure_house(self, house, batteries):
        """
        take a house, remove its cable and disconnect it from its current battery and connect it to a random (available) battery with a cable
        """
        old_battery = house.cable.battery
        
        old_battery.remove_house(house)

        # remove cable
        house.cable = None

        new_battery = random.choice(batteries)

        # cable object is created but cable has not been layed yet
        cable1 = cable.Cable(house = house, battery = new_battery)

        # if cables from different houses are allowed to be connected to eachother
        if self.cable_to_cable:
            
            # different ways of connecting a house to a battery
            if self.lay_cable == "to_random_house":
                cable1.lay_cable_to_random_house()
            else:
                cable1.lay_cable_to_closest_cable()
        # connect the house directly to the battery
        else:
            cable1.lay_cable()

        # add new cable and thus new battery to house
        house.add_cable(cable1)

        new_battery.add_house(house)

    def mutate_single_house(self, new_grid):
        """
        Changes the connection of a random house to a battery with a random close to valid connection to a different battery.
        """
        random_house = random.choice(list(new_grid.houses.values()))
        available_batteries = list()

        for battery in new_grid.batteries.values():
            
            # a battery is defined as available when it has not yet reached its maximum capacity
            if not battery.capacity_reached():
                available_batteries.append(battery)
        
        # actually bring about the change
        self.random_reconfigure_house(random_house, available_batteries)

    def mutate_grid(self, new_grid):
        """
        Changes the connection of a number of houses to a random available battery.
        """
        for _ in range(math.ceil(self.mutate_house_number)):
            self.mutate_single_house(new_grid)

    def check_solution(self, new_grid):
        """
        Checks and accepts better solutions than the current solution.
        """
        # in the case that cables can be connected to cables from different houses, costs are calculated differently
        if self.cable_to_cable:
            new_cost = new_grid.calc_cost2()
        else:
            new_cost = new_grid.calc_cost()

        old_cost = self.cost

        if self.minimalize_surplus:
            # surplus = output above battery capacity
            new_surplus = new_grid.calc_surplus()
            old_surplus = self.surplus

            # if both cost and surplus need to be minimized
            if self.cost_and_surplus:

                if new_surplus <= old_surplus and new_cost <= old_cost:
                    self.grid = new_grid
                    self.surplus = new_surplus
                    self.cost = new_cost
            else:
                
                # < and not <= because unnecessary changes are more likely to result in a higher cost
                if new_surplus < old_surplus:
                    self.grid = new_grid
                    self.surplus = new_surplus
                    self.cost = new_cost

        else:

            if new_cost <= old_cost:
                self.grid = new_grid
                self.cost = new_cost
    
    def update_mutate_house_number(self):
        """
        linearly decreases mutate_house_number with each iteration.
        """
        self.mutate_house_number = (self.mutate_house_number - (self.mutate_house_number0 / self.iterations))

    def run(self, iterations, verbose=False):
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """
        if self.cable_to_cable:
            self.cost = self.grid.calc_cost2()
        else:
            self.cost = self.grid.calc_cost()

        if self.minimalize_surplus:
            self.surplus = self.grid.calc_surplus()
            
        self.iterations = iterations

        # for later plotting
        self.cost_list = list()

        # save after every 10k iterations
        self.checkpoints = list(range(10000, self.iterations, 10000))

        for iteration in range(iterations):

            # Nice trick to only print if variable is set to True
            if self.minimalize_surplus:
                print(f'Iteration {iteration}/{iterations}, current surplus: {self.surplus}, current cost: {self.cost}') if verbose else None
                
            else:
                print(f'Iteration {iteration}/{iterations}, current cost: {self.cost}') if verbose else None

            # Create a copy of the grid to simulate the change
            new_grid = copy.deepcopy(self.grid)

            self.mutate_grid(new_grid)

            # Accept it if it is better
            self.check_solution(new_grid)

            # decrease mutate_house_number if requested
            if self.decreasing_mutate_house_number == True:
                self.update_mutate_house_number()

            if self.with_checkpoints:

                if iteration in self.checkpoints and self.grid.is_valid():
                    # NOTE: YOU HAVE TO CHANGE THIS YOURSELF!
                    file_name = f"SmartGrid/data/solutions/10k_or_greedy_ctc_dis1_{iteration}_hc_fix_ctc.pickle"

                    with open(file_name, 'wb') as handle:
                        pickle.dump(self, handle)
            
            self.cost_list.append(self.cost)

    

        