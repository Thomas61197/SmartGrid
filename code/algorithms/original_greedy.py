import copy
import random
from code.classes import cable

class Greedy:
    """
    Calculats the shortest Manhattan distance from each house to a battery
    """
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)

    def run(self):
        """
        Calculates the Manhattan distances from each house to a battery
        """
        random.shuffle(self.grid.houses)

        # Create a dictionary of all the houses with a list of the Manhattan distances to each battery
        for house in self.grid.houses.values():
            distances = {}

            for battery in self.grid.batteries.values():
                distances[battery.id] = abs(house.x - battery.x) + abs(house.y - battery.y)

            # Sort distance from low to high
            distances = {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}
            iterable_object = iter(distances.keys())
            closest_battery = self.grid.batteries[next(iterable_object)]

            # go until you find a battery that has not reached capacity yet
            while closest_battery.capacity_reached() == True:
                closest_battery = self.grid.batteries[next(iterable_object)]

            # connect_house_to_battery(grid, house, battery)
            closest_battery.add_house(house)
            cable1 = cable.Cable(house = house, battery = closest_battery)
            cable1.lay_cable()
            house.add_cable(cable1)
            


            


                    
            
       


            
            

## Code van live coding ter inspiratie

    # def get_next_node(self, nodes):
    #     """
    #     Gets the next node with the most neighbours and removes it from the list.
    #     """
    #     nodes.sort(key=lambda node: len(node.neighbours))
    #     return nodes.pop()

    # def run(self):
    #     """
    #     Greedily assigns the lowest costing transmitters to the nodes of the graph.
    #     """
    #     nodes = list(self.graph.nodes.values())

    #     node_possibilities = self.transmitters

    #     # Repeat untill no more possible solution or we've assigned all nodes
    #     while nodes or not node_possibilities:
    #         node = self.get_next_node(nodes)

    #         # Retrieve all valid possible values for a node
    #         node_possibilities = node.get_possibilities(self.transmitters)

    #         # Sort them by value in ascending order
    #         node_possibilities.sort(key=lambda transmitter: transmitter.value)

    #         # Assign the lowest value possibility to the node
    #         node.value = node_possibilities[0]