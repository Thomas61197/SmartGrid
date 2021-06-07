import copy
import random
from code.classes import grid, house, battery, cable

class Random:
    """
    Creates a cable between a randomly selected house and a randomly selected battery,
    taking into account the battery capacity
    """

    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)


    def run(self):
        random_house_id_list = list(self.grid.houses.keys())
        random.shuffle(random_house_id_list)

        for house_id in random_house_id_list:
            house = self.grid.houses[house_id]
            random_battery = self.grid.batteries[random.choice(list(self.grid.batteries.keys()))]

            # keep picking a random battery until you've found one that has not reached capacity yet
            while random_battery.capacity_reached == True:
                random_battery = self.grid.batteries[self.get_random_battery_id()]
            
            random_battery.add_house(house)

            # determine cable location
            x = list()
            y = list()

            cable_head_x = house.x
            cable_head_y = house.y

            x.append(cable_head_x)
            y.append(cable_head_y)

            diff_x = house.x - random_battery.x

            # if diff_x is positive, house is right of battery
            if diff_x > 0:

                while cable_head_x > random_battery.x:
                    cable_head_x -= 1
                    x.append(cable_head_x)
                    y.append(cable_head_y)
            
            # if diff_x is negative, house is left of battery
            elif diff_x < 0:

                while cable_head_x < random_battery.x:
                    cable_head_x += 1
                    x.append(cable_head_x)
                    y.append(cable_head_y)

            diff_y = house.y - random_battery.y

            # if house is above battery
            if diff_y > 0:

                while cable_head_y > random_battery.y:
                    cable_head_y -= 1
                    x.append(cable_head_x)
                    y.append(cable_head_y)

            # if house is below battery
            elif diff_y < 0:

                while cable_head_y < random_battery.y:
                    cable_head_y += 1
                    x.append(cable_head_x)
                    y.append(cable_head_y)
            
            cable_length = abs(house.x - random_battery.x) + abs(house.y - random_battery.y)
            house.add_cable(cable.Cable(x, y, house, random_battery, cable_length))
        
        return self.grid

