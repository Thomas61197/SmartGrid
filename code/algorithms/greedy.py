import copy
import random
from code.classes import grid, house, battery, cable

class Greedy:
    """
    Calculats the shortest Manhattan distance from each house to a battery
    """
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)

    def get_distance_house(self):
        """
        Calculates the Manhattan distances from each house to a battery
        """
        # Create a dict with for each house a sorted dict of distance to each battery
        for house in self.grid.houses.values():
            distances = {}
            for battery in self.grid.batteries.values():
                distances[battery.id] = abs(house.x - battery.x) + abs(house.y - battery.y)
            # Sort distance from low to high
            house.battery_distances = sorted(distances.items(), key=lambda x: x[1])


    def battery_distance_list(self):
        """
        For each battery, make a sorted dict of connected houses and their distance from that battery
        """
        for battery in self.grid.batteries.values():

            for house in self.grid.houses.values():
                if house.battery_distances[0][0] is battery.id:
                    battery.add_house(house)


    def replace_connections(self): 
        """
        Find the houses with the shortest distance to their second closest battery, 
        connect if capacity of current battery is filled
        """
        battery_numbers = [*range(0,len(self.grid.batteries.values()))]

        for battery in self.grid.batteries.values():
            battery = self.grid.batteries[(random.choice(battery_numbers))]
            while battery.capacity_reached():
                # Make a dict of distances from houses to their next closest battery
                second_closest_battery = {}
                for house in battery.houses:
                    house_obj = self.grid.houses[house]

                    # Only move a house if there is still batteries left to move it too
                    if house_obj.rank < 4:
                        second_closest = house_obj.battery_distances[(house_obj.rank + 1)]
                        second_closest_battery[house] = second_closest


                # Sort that dict
                second_closest_battery = sorted(second_closest_battery.items(), key=lambda x: x[1])
                
                # Pick the one with the shortest distance to reconnect
                replace_house_id = second_closest_battery[0][0]
                replace_to_battery_id = second_closest_battery[0][1][0]

                replace_house = self.grid.houses[replace_house_id]
                # Remove found house from current battery
                battery.remove_house(replace_house)
                # Indicate with rank that we've changed batteries
                if replace_house.rank < 3:
                    replace_house.rank += 1

                # Add house to new battery INDEX DIFFERENTLY
                self.grid.batteries[replace_to_battery_id].add_house(replace_house)


    def run_greedy(self): 
        """
        Find the houses with the shortest distance to their second closest battery, 
        connect if capacity of current battery is filled
        """
        # Sort distances from each house to each battery
        self.get_distance_house()

        # Add houses to their closest battery
        self.battery_distance_list()

        # If battery capacity is full, reconnect houses with the shortest distance to the next battery
        for i in range(10):

            self.replace_connections()
            
        # Start laying cables
        for house in self.grid.houses.values():
            closest_battery_id = house.battery_distances[house.rank][0]
            closest_battery = self.grid.batteries[closest_battery_id]
            house.battery = closest_battery_id

            cable1 = cable.Cable(house = house, battery = closest_battery)
            cable1.lay_cable()
            house.add_cable(cable1)
            
        for battery in self.grid.batteries.values():
                print(battery.get_cum_output())
        print('Output to batteries:')



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