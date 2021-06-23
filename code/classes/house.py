class House():
    """
    Dataclass containing house info
    """
    def __init__(self, x, y, max_output, id):
        self.x = x
        self.y = y
        self.max_output = max_output
        self.id = id
        self.cable = None
        self.battery_distances = {}
        self.rank = 0
        self.battery = None
    
    def add_cable(self, cable):
        """
        set cable for house.
        """
        self.cable = cable


