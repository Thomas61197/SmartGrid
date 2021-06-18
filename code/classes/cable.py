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

        return x, y

            


        