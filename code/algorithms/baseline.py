import copy
import random
from code.classes import cable

class Baseline:
    """
    Creates a cable between a randomly selected house and a randomly selected battery,
    taking into account the battery capacity
    """

    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)


    def run(self):
        random.shuffle(self.grid.houses)

        for house in self.grid.houses.values():
            random_battery = random.choice(self.grid.batteries)

            # keep picking a random battery until you've found one that has not reached capacity yet
            while random_battery.capacity_reached == True:
                random_battery = random.choice(self.grid.batteries)
            
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

