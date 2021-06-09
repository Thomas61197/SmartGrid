import random
import copy
from code.algorithms import baseline

class Simulated_annealing:
    def __init__(self, empty_grid):
        self.empty_grid = empty_grid

    def run(self):
        # repeat:
            # choose a random start state
            self.grid = copy.deepcopy(baseline.Baseline(self.empty_grid))

            # choose a starting temperature
            temp = 100

            # repeat N times:
            for i in range(20000):
                # make a small adjustment
                # okay so this part is 
                # when random() > chance(old, new, temperature):
                    # revert adjustment
                # lower temperature

# import random
# import math

# from .hillclimber import HillClimber


# class SimulatedAnnealing(HillClimber):
#     """
#     The SimulatedAnnealing class that changes a random node in the graph to a random valid value.
#     Each improvement or equivalent solution is kept for the next iteration.
#     Also sometimes accepts solutions that are worse, depending on the current temperature.
#     Most of the functions are similar to those of the HillClimber class, which is why
#     we use that as a parent class.
#     """
#     def __init__(self, graph, transmitters, temperature=1):
#         # Use the init of the Hillclimber class
#         super().__init__(graph, transmitters)

#         # Starting temperature and current temperature
#         self.T0 = temperature
#         self.T = temperature

#     def update_temperature(self):
#         """
#         This function implements a *linear* cooling scheme.
#         Temperature will become zero after all iterations passed to the run()
#         method have passed.
#         """
#         self.T = self.T - (self.T0 / self.iterations)

#         # Exponential would look like this:
#         # alpha = 0.99
#         # self.T = self.T * alpha

#         # where alpha can be any value below 1 but above 0

#     def check_solution(self, new_graph):
#         """
#         Checks and accepts better solutions than the current solution.
#         Also sometimes accepts solutions that are worse, depending on the current
#         temperature.
#         """
#         new_value = new_graph.calculate_value()
#         old_value = self.value

#         # Calculate the probability of accepting this new graph
#         delta = new_value - old_value
#         probability = math.exp(-delta / self.T)

#         # NOTE: Keep in mind that if we want to maximize the value, we use:
#         # delta = old_value - new_value

#         # Pull a random number between 0 and 1 and see if we accept the graph!
#         if random.random() < probability:
#             self.graph = new_graph
#             self.value = new_value

#         # Update the temperature
#         self.update_temperature()

import copy
import random

from .randomise import random_reconfigure_node


class HillClimber:
    """
    The HillClimber class that changes a random node in the graph to a random valid value. Each improvement or
    equivalent solution is kept for the next iteration.
    """
    def __init__(self, graph, transmitters):
        if not graph.is_solution():
            raise Exception("HillClimber requires a complete solution.")

        self.graph = copy.deepcopy(graph)
        self.value = graph.calculate_value()

        self.transmitters = transmitters

    def mutate_single_node(self, new_graph):
        """
        Changes the value of a random node with a random valid value.
        """
        random_node = random.choice(list(new_graph.nodes.values()))
        available_transmitters = random_node.get_possibilities(self.transmitters)
        random_reconfigure_node(new_graph, random_node, available_transmitters)

    def mutate_graph(self, new_graph, number_of_nodes=1):
        """
        Changes the value of a number of nodes with a random valid value.
        """
        for _ in range(number_of_nodes):
            self.mutate_single_node(new_graph)

    def check_solution(self, new_graph):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_value = new_graph.calculate_value()
        old_value = self.value

        # We are looking for maps that cost less!
        if new_value <= old_value:
            self.graph = new_graph
            self.value = new_value

    def run(self, iterations, verbose=False, mutate_nodes_number=1):
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """
        self.iterations = iterations

        for iteration in range(iterations):
            # Nice trick to only print if variable is set to True
            print(f'Iteration {iteration}/{iterations}, current value: {self.value}') if verbose else None

            # Create a copy of the graph to simulate the change
            new_graph = copy.deepcopy(self.graph)

            self.mutate_graph(new_graph, number_of_nodes=mutate_nodes_number)

            # Accept it if it is better
            self.check_solution(new_graph)

