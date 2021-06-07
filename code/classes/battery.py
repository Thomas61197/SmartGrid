class Battery():
    def __init__(self, x, y, capacity, id):
        self.x = x
        self.y = y
        self.capacity = capacity
        self.id = id

        self.houses = {}

    def add_house(self, house):
        self.houses[house.id] = house
    
    def capacity_reached(self):
        cum_output = 0

        for house in self.houses.values():
            cum_output += float(house.max_output)

        if self.capacity < cum_output:
            return False
        
        return True