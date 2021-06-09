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

        