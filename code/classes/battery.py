import numpy as np

class Battery():
    def __init__(self, id, x, y, capacity):
        self.id = id
        self.x = x
        self.y = y
        self.capacity = capacity
        self.cost = 5000
        self.houses = {}

    def add_house(self, house):
        """
        Add a house object to the dict of houses that this battery is connected to
        """
        self.houses[house.id] = house

    def remove_house(self, house):
        """
        Remove a house object from the dict of houses that this battery is connected to
        """
        del self.houses[house.id]
    
    def capacity_reached(self):
        """
        Returns True if the capacity of the battery has been reached
        """
        cum_output = self.get_cum_output()

        if self.capacity < cum_output:
            return True
        
        return False

    def capacity_left(self):
        """
        Returns how much output the battery can still receive
        """
        return self.capacity - self.get_cum_output()

    def get_cum_output(self):
        """
        Add the cumulative output of all the houses connected to that battery
        """
        cum_output = 0.0

        for house in self.houses.values():
            cum_output += float(house.max_output)

        return cum_output

    def get_cable_matrix(self):
        """
        Creates a matrix of ones and zeroes, with ones indicating the cables connecting the houses to this battery
        """
        # the length and width are 51 bc it goes from 0 up to and including 50
        matrix = np.zeros( (51, 51), dtype=int )

        for house in self.houses.values():
            
            # these checks need to be here because this function can also be used on (semi)empty grids
            if not house.cable is None:

                if not house.cable.x is None:

                    for x, y in zip(house.cable.x, house.cable.y):
                        matrix[x][y] = int(1)
                
        return matrix