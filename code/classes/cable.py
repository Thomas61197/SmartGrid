import random

class Cable():
    def __init__(self, house, battery):
        self.x = list()
        self.y = list()
        self.house = house
        self.battery = battery
        self.cost_per_unit = 9

        # if cables cannot be connected to cables from other houses
        self.length = abs(house.x - battery.x) + abs(house.y - battery.y)

    def cost(self):

        # only used if cables cannot be connected to cables from other houses
        return self.cost_per_unit * self.length

    def lay_cable_to_closest_cable(self):
        """
        cables are now allowed to be attached to eachother.
        Can be used for empty and filled grids
        """
        # connect to closest cable connected to that battery 
        # or to the battery itself if that is closer or if there are no cables connected to that battery yet
        # step 1: find the closest point
        # first get the distance between the house and the battery

        # minimum distance
        min_distance = self.length

        connect_to = [self.battery.x, self.battery.y]

        # get the cables connected to the battery
        cable_matrix = self.battery.get_cable_matrix()

        # loop through the grid coordinates
        for y in range(len(cable_matrix[0][:])):

            for x in range(len(cable_matrix[:][0])):
                
                # if there is a cable, calculate the distance from the house to that cable
                if cable_matrix[x][y] == 1:
                    distance = abs(self.house.x - x) + abs(self.house.y - y)

                    # if this distance is smaller than the minimum_distance, minimum_distance becomes new distance and new point to connect to is found
                    if distance < min_distance:
                        min_distance = distance
                        connect_to = [x, y]

        # step 2: lay cable to closest point
        self.lay_cable(connect_to[0], connect_to[1])

        # now append from closest cable to battery. This needs to be done because otherwise houses will not be connected to a battery when a house is reconnected
        second_part_of_cable_x = list()
        second_part_of_cable_y = list()

        # find house with a cable which contains the coordinates of the closest cable
        for house in self.battery.houses.values():
            start_appending = False

            # if this house has a cable
            if house.cable is not None:
                # loop through the cable coordinates until you find the coordinates of the closest cable
                # keep looping through the rest of the cable while adding the rest of the cable coordinates to second_part_of_cable
                for x, y in zip(house.cable.x, house.cable.y):

                    if x == connect_to[0] and y == connect_to[1]:
                        # the house of interest has been found and we need the rest of the cable from this point onwards
                        start_appending = True

                    if start_appending:
                        second_part_of_cable_x.append(x)
                        second_part_of_cable_y.append(y)

                # we only need the rest of that cable once
                if start_appending:
                    break
        
        # the closest cable would be twice in there if we didnt do this
        second_part_of_cable_x = second_part_of_cable_x[1:]
        second_part_of_cable_y = second_part_of_cable_y[1:]

        # add it to the actual cable
        for x, y in zip(second_part_of_cable_x, second_part_of_cable_y):
            self.x.append(x)
            self.y.append(y)

    def lay_cable(self, connect_to_x = None, connect_to_y = None):
        """
        provide connect_to_x and connect_to_y if you dont want to connect to the battery directly.
        connects to given point with manhattan distance and only one kink in the cable.
        """

        # determine cable location
        # connect to battery if no target given
        if connect_to_x is None:
            connect_to_x = self.battery.x
            connect_to_y = self.battery.y

        # start by laying the cable where the house is
        cable_head_x = self.house.x
        cable_head_y = self.house.y

        self.x.append(cable_head_x)
        self.y.append(cable_head_y)

        # first horizontal then vertical with a chance of 1 in 2. Why? Because the algorithm can then decide which one is better.
        if random.random() > 0.5:
            diff_x = self.house.x - connect_to_x

            # if diff_x is positive, house is right of battery/point of interest
            if diff_x > 0:

                while cable_head_x > connect_to_x:
                    cable_head_x -= 1
                    self.x.append(cable_head_x)
                    self.y.append(cable_head_y)
            
            # if diff_x is negative, house is left of battery/point of interest
            elif diff_x < 0:

                while cable_head_x < connect_to_x:
                    cable_head_x += 1
                    self.x.append(cable_head_x)
                    self.y.append(cable_head_y)

            diff_y = self.house.y - connect_to_y

            # if house is above battery/point of interest
            if diff_y > 0:

                while cable_head_y > connect_to_y:
                    cable_head_y -= 1
                    self.x.append(cable_head_x)
                    self.y.append(cable_head_y)

            # if house is below battery/point of interest
            elif diff_y < 0:

                while cable_head_y < connect_to_y:
                    cable_head_y += 1
                    self.x.append(cable_head_x)
                    self.y.append(cable_head_y)

        # first vertical, then horizontal
        else:
            diff_y = self.house.y - connect_to_y

            # if house is above battery/point of interest
            if diff_y > 0:

                while cable_head_y > connect_to_y:
                    cable_head_y -= 1
                    self.x.append(cable_head_x)
                    self.y.append(cable_head_y)

            # if house is below battery/point of interest
            elif diff_y < 0:

                while cable_head_y < connect_to_y:
                    cable_head_y += 1
                    self.x.append(cable_head_x)
                    self.y.append(cable_head_y)

            diff_x = self.house.x - connect_to_x

            # if diff_x is positive, house is right of battery/point of interest
            if diff_x > 0:

                while cable_head_x > connect_to_x:
                    cable_head_x -= 1
                    self.x.append(cable_head_x)
                    self.y.append(cable_head_y)
            
            # if diff_x is negative, house is left of battery/point of interest
            elif diff_x < 0:

                while cable_head_x < connect_to_x:
                    cable_head_x += 1
                    self.x.append(cable_head_x)
                    self.y.append(cable_head_y)


    def lay_cable_to_random_house(self):
        """
        lays cable to a random house connected to that battery.
        """
        random_house = random.choice(list(self.battery.houses.values()))

        # lay cable to random house
        self.lay_cable(connect_to_x=random_house.x, connect_to_y = random_house.y)

        # add the random house cable to the cable, otherwise the house will not be connected to a battery if a house is reconnected
        for x, y in zip(random_house.cable.x, random_house.cable.y):
            self.x.append(x)
            self.y.append(y)

    
    