import random
import math

from .hill_climber import Hill_climber


class Simulated_annealing(Hill_climber):
    """
    The SimulatedAnnealing class that changes a random node in the graph to a random valid value.
    Each improvement or equivalent solution is kept for the next iteration.
    Also sometimes accepts solutions that are worse, depending on the current temperature.
    Most of the functions are similar to those of the HillClimber class, which is why
    we use that as a parent class.
    """
    def __init__(self, empty_grid, temperature=1, cooling_scheme="linear", alpha=0.99, mutate_house_number=20):
        # Use the init of the Hillclimber class
        super().__init__(empty_grid, mutate_house_number)

        # Starting temperature and current temperature
        self.T0 = temperature
        self.T = temperature

        # update_temp parameters
        self.cooling_scheme = cooling_scheme
        self.alpha = alpha

    def update_temperature(self):
        """
        This function implements a *linear* cooling scheme.
        Temperature will become zero after all iterations passed to the run()
        method have passed.
        """
        if self.cooling_scheme == "linear":
            self.T = self.T - (self.T0 / self.iterations)
        else:
            self.cooling_scheme = "exponential"
            # Exponential would look like this:
            self.T = self.T * self.alpha
            # where alpha can be any value below 1 but above 0

    def update_mutate_house_number(self):
        self.mutate_house_number = (self.mutate_house_number - (self.mutate_house_number0 / self.iterations))

    def check_solution(self, new_grid, decreasing_mutate_house_number):
        """
        Checks and accepts better solutions than the current solution.
        Also sometimes accepts solutions that are worse, depending on the current
        temperature.
        """
        new_cost = new_grid.calc_cost()
        old_cost = self.cost

        # Calculate the probability of accepting this new graph
        delta = new_cost - old_cost
        probability = math.exp(-delta / self.T)

        # NOTE: Keep in mind that if we want to maximize the value, we use:
        # delta = old_value - new_value

        # Pull a random number between 0 and 1 and see if we accept the graph!
        if random.random() < probability:
            self.grid = new_grid
            self.cost = new_cost

        # Update the temperature
        self.update_temperature()

        if decreasing_mutate_house_number == True:
            self.update_mutate_house_number()

