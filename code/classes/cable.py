class Cable():
    def __init__(self, x, y, house, battery, length):
        self.x = x
        self.y = y
        self.house = house
        self.battery = battery
        self.cost_per_unit = 9
        self.length = length

    def cost(self):
        return self.cost_per_unit * self.length
        