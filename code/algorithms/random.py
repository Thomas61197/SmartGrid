import copy
import random
from code.classes import grid, house, battery, cable

class Random:
    """
    Calculates the shortest Manhattan distance from each house to a battery
    """

    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)


    def shuffle_houses(self):
        shuffled = random.shuffle(list(self.grid.houses.keys()))
        print(len(shuffled))
        return shuffled


    def pick_battery(self, battery_id_list):
        random_battery = random.choice(battery_id_list)
        print(random_battery)
        return random_battery


    def run(self):
        random_house_list = self.shuffle_houses()

        for house_id in random_house_list:
            if random_battery.capacity_reached is False:
                random_battery.add_house(house)
            else:
                battery_id_list.remove(random_battery)
                self.pick_battery(battery_id_list)
                self.add_houses( )

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

            house.add_cable(cable.Cable(x, y, house, random_battery, distances[random_battery.id]))
        
        return self.grid

