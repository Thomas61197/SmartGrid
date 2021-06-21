import numpy as np

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
        cum_output = self.get_cum_output()

        # if capacity has been reached, return true
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

    def get_cable_matrix(self):
        matrix = np.zeros( (51, 51), dtype=int )

        for house in self.houses.values():

            for x, y in zip(house.cable.x, house.cable.y):
                
                # for some reason, x and y are sometimes lists in object best_greedy
                if type(x) == list:

                    for x2, y2 in zip(x, y):
                        matrix[x2][y2] = int(1)  # -1 bc grid coordinates are from 1 up to and including 50

                else:
                    matrix[x][y] = int(1)
                
        return matrix