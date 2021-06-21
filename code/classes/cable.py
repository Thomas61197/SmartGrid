import random

class Cable():
    def __init__(self, house, battery):
        self.x = None
        self.y = None
        self.house = house
        self.battery = battery
        self.cost_per_unit = 9
        self.length = abs(house.x - battery.x) + abs(house.y - battery.y)

    def cost(self):
        return self.cost_per_unit * self.length

    def lay_cable(self):
        # determine cable location
        x = list()
        y = list()

        cable_head_x = self.house.x
        cable_head_y = self.house.y

        x.append(cable_head_x)
        y.append(cable_head_y)

        diff_x = self.house.x - self.battery.x

        # if diff_x is positive, house is right of battery
        if diff_x > 0:

            while cable_head_x > self.battery.x:
                cable_head_x -= 1
                x.append(cable_head_x)
                y.append(cable_head_y)
        
        # if diff_x is negative, house is left of battery
        elif diff_x < 0:

            while cable_head_x < self.battery.x:
                cable_head_x += 1
                x.append(cable_head_x)
                y.append(cable_head_y)

        diff_y = self.house.y - self.battery.y

        # if house is above battery
        if diff_y > 0:

            while cable_head_y > self.battery.y:
                cable_head_y -= 1
                x.append(cable_head_x)
                y.append(cable_head_y)

        # if house is below battery
        elif diff_y < 0:

            while cable_head_y < self.battery.y:
                cable_head_y += 1
                x.append(cable_head_x)
                y.append(cable_head_y)

        self.x = x
        self.y = y

    def lay_cable2(self):
        """
        cables are now allowed to be attached to eachother
        """
        # connect to closest cable connected to that battery 
        # OR (to the battery itself if that is closer
        # OR to the battery itself if there are no cables connected to that battery yet)

        # step 1: find the closest point
        # first get the distance between the ouse and the battery
        min_distance = self.length
        connect_to = [self.battery.x, self.battery.y]
        cable_matrix = self.battery.get_cable_matrix()

        for y in range(len(cable_matrix[0][:])):

            for x in range(len(cable_matrix[:][0])):

                if cable_matrix[x][y] == 1:
                    distance = abs(self.house.x - x) + abs(self.house.y - y)

                    if distance < min_distance:
                        min_distance = distance
                        connect_to = [x, y]

        # step 2: lay cable to closest point
        first_part_of_cable_x, first_part_of_cable_y = self.lay_cable3(self, connect_to[0], connect_to[1])

        # now append from closest point to battery

    def lay_cable3(self, connect_to_x, connect_to_y):
        # determine cable location
        x = list()
        y = list()

        cable_head_x = self.house.x
        cable_head_y = self.house.y

        x.append(cable_head_x)
        y.append(cable_head_y)

        if random.random() > 0.5:

            diff_x = self.house.x - connect_to_x

            # if diff_x is positive, house is right of battery
            if diff_x > 0:

                while cable_head_x > connect_to_x:
                    cable_head_x -= 1
                    x.append(cable_head_x)
                    y.append(cable_head_y)
            
            # if diff_x is negative, house is left of battery
            elif diff_x < 0:

                while cable_head_x < connect_to_x:
                    cable_head_x += 1
                    x.append(cable_head_x)
                    y.append(cable_head_y)

            diff_y = self.house.y - connect_to_y

            # if house is above battery
            if diff_y > 0:

                while cable_head_y > connect_to_y:
                    cable_head_y -= 1
                    x.append(cable_head_x)
                    y.append(cable_head_y)

            # if house is below battery
            elif diff_y < 0:

                while cable_head_y < connect_to_y:
                    cable_head_y += 1
                    x.append(cable_head_x)
                    y.append(cable_head_y)

        else:
            diff_y = self.house.y - connect_to_y

            # if house is above battery
            if diff_y > 0:

                while cable_head_y > connect_to_y:
                    cable_head_y -= 1
                    x.append(cable_head_x)
                    y.append(cable_head_y)

            # if house is below battery
            elif diff_y < 0:

                while cable_head_y < connect_to_y:
                    cable_head_y += 1
                    x.append(cable_head_x)
                    y.append(cable_head_y)

            diff_x = self.house.x - connect_to_x

            # if diff_x is positive, house is right of battery
            if diff_x > 0:

                while cable_head_x > connect_to_x:
                    cable_head_x -= 1
                    x.append(cable_head_x)
                    y.append(cable_head_y)
            
            # if diff_x is negative, house is left of battery
            elif diff_x < 0:

                while cable_head_x < connect_to_x:
                    cable_head_x += 1
                    x.append(cable_head_x)
                    y.append(cable_head_y)


        return x, y

    def lay_cable4(self):
        # from all houses connected to that battery and the battery itself
        # choose a random one
        to_pick_from = list()
        to_pick_from.append(self.battery)
        to_pick_from.append(self.battery.houses.values())
        picked = random.choice(to_pick_from)
        
        # if it's a battery
        if picked == self.battery:
            # lay cable directly from house to battery
            self.x, self.y = self.lay_cable(self.battery.x, self.battery.y)

        # if it's a house
        else:
            random_house = picked
            final_cable_x_list = list()
            final_cable_y_list = list()
            # lay a cable from the given house to the random house
            # call it green
            green_x_list, green_y_list = self.lay_cable(random_house.x, random_house.y)
            # get the cable from the random house
            # call it orange
            orange_x_list = random_house.cable.x
            orange_y_list = random_house.cable.y

            # _______________

            # final_cable.append(green not in orange)
            # shared = green in orange
            shared_x_list = list()
            shared_y_list = list()

            for green_x, green_y in zip(green_x_list, green_y_list):
                green_in_orange = False

                for orange_x, orange_y in zip(orange_x_list, orange_y_list):

                    if orange_x == green_x and orange_y == green_y:
                        green_in_orange = True
                        shared_x_list.append(green_x)
                        shared_y_list.append(green_y)

                if not green_in_orange:
                    final_cable_x_list.append(green_x)
                    final_cable_y_list.append(green_y)

            # final_cable.append(orange not in shared)
            for orange_x, orange_y in zip(orange_x_list, orange_y_list):
                orange_in_shared = False

                for shared_x, shared_y in zip(shared_x_list, shared_y_list):

                    if orange_x == shared_x and orange_y == shared_y:
                        orange_in_shared = True

                if not orange_in_shared:
                    final_cable_x_list.append(orange_x)
                    final_cable_y_list.append(orange_y)
            # __________________

            # eerst links rechts, dan boven beneden of andersom, random bepaald