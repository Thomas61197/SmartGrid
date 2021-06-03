import csv

class Battery():
    def __init__(self, x, y, capacity):
        self.x = x
        self.y = y
        self.capacity = capacity
        
    def load_batteries(battery_file):
        """
        Load the positions of all the batteries.
        """
        batteriesX = {}
        batteriesY = {}
        batteries_capacity = {}
        with open(battery_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for count, row in enumerate(reader):
                coordinates = row['positie'].split(',')
                batteriesX[count+1] = coordinates[0]
                batteriesY[count+1] = coordinates[1]
                batteries_capacity[count+1] = row['capaciteit']

        return batteriesX, batteriesY, batteries_capacity
