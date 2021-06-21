# OPTION 1 connect to closest house (or battery) based on cheapest_gready
#
#   class Greedy_cheapest:
    """
    Calculates the shortest Manhattan distance from each house to   *** THE CLOSEST HOUSE OR BATTERY ***
    """
#    def __init__(self, grid):
#        self.grid = copy.deepcopy(grid)
#
#
#     def get_distance_house(self):
        """
        Calculates the Manhattan distances from each house to a battery
        """

#       def battery_distance_list(self):
        """
        For each battery, make a sorted dict of connected houses and their distance from that battery
        """


# ------------------ new -------------------
#       def closest_neighbour (self):
        """ 
        Calculates the Manhattan distances from each house to *** THE CLOSEST HOUSE OR BATTERY ***
        """
        # Option 1 Operates like get_distance_house and battery_distance_list but treats other house as batteries
            
            # Create a dict with for each house a sorted dict of distances to all other houses

            # idea 2*** select "10" closest houses, delete the rest

            # Sort distances from low to high 

        
        # Option 2 for each house first select other houses from district-*_houses.csv with coordinates -5/+5 
            
            # Create a dict with with the distances to those houses 

            # idea 2*** select "10" closest houses, delete the rest

            # Sort distances from low to high 

# -----------------------------------------


#       def run_greedy(self): 
            """
            Find the houses with the shortest distance to their second closest battery, 
            connect if capacity of current battery is filled
            """
            # Sort distances from each house to each battery
            

            # Add houses to their closest battery
        

        
        # Start laying cables
        
        # ------------------ new -------------------
            # for each battery select closest battery 
            # lay cable 

            # for each unconnected ^ 
            # select the closest neighbor (battery or house)
            # lay cable
        

            # delete double cables

        # 
        # -------------------------------------