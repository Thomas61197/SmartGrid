import copy
import random
from code.classes import cable

class Hill_climber:
    """
    The HillClimber class that changes a random node in the graph to a random valid value. Each improvement or
    equivalent solution is kept for the next iteration.
    """
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)

    def random_reconfigure_house(self, house, batteries):
        """
        take a house and connect it to a random (available) battery
        """
        # detach house from battery
        old_battery = house.cable.battery
        old_battery.remove_house(house)
        new_battery = random.choice(batteries)
        new_battery.add_house(house)
        cable1 = cable.Cable(house = house, battery = new_battery)
        cable1.lay_cable()
        house.add_cable(cable1)

    def mutate_single_house(self, new_grid):
        """
        Changes the connection of a random house to a battery with a random valid connection to a different battery.
        """
        random_house = random.choice(list(new_grid.houses.values()))

        self.random_reconfigure_house(random_house, list(new_grid.batteries.values()))

    def mutate_grid(self, new_grid, number_of_houses=1):
        """
        Changes the value of a number of nodes with a random valid value.
        """
        for _ in range(number_of_houses):
            self.mutate_single_house(new_grid)

    def check_solution(self, new_grid):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_cost = new_grid.calc_cost()
        old_cost = self.cost

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

    def run(self, iterations, verbose=False, mutate_houses_number=2):
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """
        self.cost = self.grid.calc_cost()
        self.iterations = iterations

        for iteration in range(iterations):
            # Nice trick to only print if variable is set to True
            print(f'Iteration {iteration}/{iterations}, valid? {self.grid.is_valid()}, current cost: {self.cost}') if verbose else None

            # Create a copy of the graph to simulate the change
            new_grid = copy.deepcopy(self.grid)

            self.mutate_grid(new_grid, number_of_houses=mutate_houses_number)

            # Accept it if it is better
            self.check_solution(new_grid)

        