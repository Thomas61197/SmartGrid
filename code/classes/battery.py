class Battery():
    def __init__(self, x, y, capacity, id):
        self.x = x
        self.y = y
        self.capacity = capacity
        self.id = id

        self.houses = {}

    def add_house(self, house):
        self.houses[house.id] = house

    def remove_house(self, house):
        del self.houses[house.id]
    
    def capacity_reached(self):
        cum_output = 0.0

        for house in self.houses.values():
            cum_output += float(house.max_output)

        # if capacity has been reached, return true
        self.capacity - cum_output
        if self.capacity < cum_output:
            return True
        
        return False

    def capacity_left(self):

        return self.capacity - self.get_cum_output()

    def get_cum_output(self):
        cum_output = 0.0

        for house in self.houses.values():
            cum_output += float(house.max_output)
            
        return cum_output