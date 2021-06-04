from code.classes import grid
from code.algorithms import greedy
import json
# from code.visualisation import visualise as vis

if __name__ == "__main__":
    district_number = "1"

    # battery_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_batteries.csv")
    battery_file = "/home/thomas61197/SmartGrid/data/Huizen&Batterijen/district_1/district-1_batteries.csv"

    # house_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")
    house_file = "/home/thomas61197/SmartGrid/data/Huizen&Batterijen/district_1/district-1_houses.csv"

    grid1 = grid.Grid(house_file, battery_file)
    
    # --------------------------- greedy --------------------------
    
    greedy1 = greedy.Greedy(grid1)
    greedy1.run()

    # --------------------------- output --------------------------
    output = list()
    out_grid = {"district": district_number, "costs-own": "grid1.calc_cost()"}
    output.append(out_grid)
    out_batteries = {"location": "38,12"}
    output.append(out_batteries)
    print(output) 

#with open('smartgrid_output.txt', 'w') as outfile:
#    json.dump(output, outfile)
