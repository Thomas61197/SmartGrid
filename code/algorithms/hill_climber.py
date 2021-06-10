import copy
import random
from code.classes import cable
from code.algorithms import baseline

class Hill_climber:
    """
    The HillClimber class that changes a random node in the graph to a random valid value. Each improvement or
    equivalent solution is kept for the next iteration.
    """
    def __init__(self, empty_grid):
        self.empty_grid = empty_grid

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
        available_batteries = list()

        for battery in new_grid.batteries.values():
            
            if not battery.capacity_reached():
                available_batteries.append(battery)

        self.random_reconfigure_house(random_house, available_batteries)

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

        # We are looking for maps that cost less!
        if new_cost <= old_cost:
            self.grid = new_grid
            self.cost = new_cost

    def run(self, iterations, verbose=False, mutate_houses_number=1):
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """
        baseline1 = baseline.Baseline(self.empty_grid)
        baseline1.run()
        self.grid = copy.deepcopy(baseline1.grid)
        self.cost = self.grid.calc_cost()
        self.iterations = iterations

        for iteration in range(iterations):
            # Nice trick to only print if variable is set to True
            print(f'Iteration {iteration}/{iterations}, current cost: {self.cost}') if verbose else None

            # Create a copy of the graph to simulate the change
            new_grid = copy.deepcopy(self.grid)

            self.mutate_grid(new_grid, number_of_houses=mutate_houses_number)

            # Accept it if it is better
            self.check_solution(new_grid)