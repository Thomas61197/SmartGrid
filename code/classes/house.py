class House():
    def __init__(self, x, y, max_output, id):
        self.x = x
        self.y = y
        self.max_output = max_output
        self.id = id
        self.cable = None
        self.battery_distances = {}
        self.rank = 0
    
    def add_cable(self, cable):
        self.cable = cable

    def get_man_distance(self):
        """
        Calculates the Manhattan distances from each house to a battery
        """

    distances = {}

    for battery in self.grid.batteries.values():
        distances[battery.id] = abs(house.x - battery.x) + abs(house.y - battery.y)
    # Sort distance from low to high
    self.battery_distances = sorted(distances[house.id].items(), key=lambda x: x[1])
