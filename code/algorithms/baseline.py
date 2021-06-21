import copy
import random
from code.classes import cable, grid

class Baseline:
    """
    Creates a cable between a randomly selected house and a randomly selected battery,
    taking into account the battery capacity
    """

    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)

    # def largest_output_house(self):
    #     output_houses = {}
    #     for house in self.grid.houses.values():
    #         output_houses[house.id] = house.max_output

    #     output_houses = {k: v for k, v in sorted(output_houses.items(), key=lambda item: item[1], reverse=True)}    
        
    #     return output_houses


    def run(self):
        random.shuffle(self.grid.houses)


        for house in self.grid.houses.values():

            random_battery = random.choice(self.grid.batteries)

            # print(house_obj.max_output)
            # cum_max_output = 1500 * 5 = 7500
            # cum_cap = 1507 * 5 = 7535
            # keep picking a random battery until you've found one that has enough space
            # while random_battery.capacity_left() < house.max_output:
            
            while random_battery.capacity_reached():
                random_battery = random.choice(self.grid.batteries)
            # while random_battery.capacity_left() < house_output:
            #     random_battery = random.choice(self.grid.batteries)
            #     if all(battery.capacity_left() < house_output for battery in self.grid.batteries.values()):
            #         print(random_battery.id, 'is:', random_battery.capacity_left(), 'and', house_output)
            
            random_battery.add_house(house)
            house.battery = random_battery.id
            cable1 = cable.Cable(house = house, battery = random_battery)
            cable1.lay_cable()
            house.add_cable(cable1)

            # for battery in self.grid.batteries.values():
            #     print(battery.get_cum_output())
            # print('Output to batteries:')

