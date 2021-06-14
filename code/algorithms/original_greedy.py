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
            while closest_battery.capacity_reached():
                closest_battery = self.grid.batteries[next(iterable_object)]

            closest_battery.add_house(house)
            house.battery = closest_battery.id


            # determine cable location
            x = list()
            y = list()

            cable_head_x = house.x
            cable_head_y = house.y

            x.append(cable_head_x)
            y.append(cable_head_y)

            diff_x = house.x - closest_battery.x

            # if diff_x is positive, house is right of battery
            if diff_x > 0:

                while cable_head_x > closest_battery.x:
                    cable_head_x -= 1
                    x.append(cable_head_x)
                    y.append(cable_head_y)
            
            # if diff_x is negative, house is left of battery
            elif diff_x < 0:

                while cable_head_x < closest_battery.x:
                    cable_head_x += 1
                    x.append(cable_head_x)
                    y.append(cable_head_y)

            diff_y = house.y - closest_battery.y

            # if house is above battery
            if diff_y > 0:

                while cable_head_y > closest_battery.y:
                    cable_head_y -= 1
                    x.append(cable_head_x)
                    y.append(cable_head_y)

            # if house is below battery
            elif diff_y < 0:

                while cable_head_y < closest_battery.y:
                    cable_head_y += 1
                    x.append(cable_head_x)
                    y.append(cable_head_y)

            house.add_cable(cable.Cable(x, y, house, closest_battery, distances[closest_battery.id]))
        # for battery in self.grid.batteries.values():
        #     print(battery.capacity_left())
        # print('next:')
            


            


                    
            
       


            
            

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