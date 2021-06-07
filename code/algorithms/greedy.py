import copy
import random
from code.classes import grid, house, battery, cable

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
        
        # Create a dictionary of all the houses with a list of the Manhattan distances to each battery
        for house in self.grid.houses.values():
            distances = {}

            for battery in self.grid.batteries.values():
                distances[battery.id] = abs(house.x - battery.x) + abs(house.y - battery.y)
            # Sort distance from low to high
            distances = {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}
            closest_battery = self.grid.batteries[next(iter(distances.keys()))]
            closest_battery.add_house(house)





    # alternative
    def get_man_distance(self):
        """
        Calculates the Manhattan distances from each house to a battery
        """
        # Create a dict with for each house a sorted dict of distance to each battery
        distances = {}
        for house in self.grid.houses.values():
            distances[house.id] = {}

            for battery in self.grid.batteries.values():
                distances[house.id][battery.id] = abs(house.x - battery.x) + abs(house.y - battery.y)
            # Sort distance from low to high
            distances[house.id] = sorted(distances[house.id].items(), key=lambda x: x[1])
            house.battery_distances = distances[house.id]
        return distances

    def battery_distance_list(self):
        """
        For each battery, make a sorted dict of connected houses and their distance from that battery
        """
        battery_distances = {}
        distances = self.get_man_distance()
        for battery in self.grid.batteries.values():
            battery_distances[battery.id] = {}

            for house in distances:
                if distances[house][0][0] is battery:
                    battery_distances[battery][house] = distances[house][0][1]
            battery_distances[battery] = sorted(battery_distances[battery].items(), key=lambda x: x[1])
            battery.houses = battery_distances[battery]

        return battery_distances

    def run_greedy(self): ## TO BE FIXED
        """
        Reallocate houses to batteries if max capacity of a battery is reached
        """
        # If summed power is larger than capacity of battery, ditch the house with largest distance:
        # The ditched house gets connected to the second (or third etc) closest battery
        for battery in self.grid.batteries.values():
            while battery.capacity_reached():
                # Pop the last item in the list
                to_be_popped = battery.houses[-1]
                battery.houses.pop()
                # Connect popped house to second closest battery
                house_id = to_be_popped[0]

                self.grid.houses.get(house_id)
                self.grid.houses[]
                house.rank = house.rank + 1
                battery_id = house.battery_distances[house.rank][1]
                # Get battery object somehow
                add_to_battery = get.battery[battery_id]
                add_to_battery.add_house(house_id)


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
        
        return self.grid






####################################################
            


            


                    
            
       


            
            

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