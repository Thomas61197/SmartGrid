from code.classes import grid
from code.algorithms import hill_climber, simulated_annealing
from code.visualisations import visualise_costs,  visualise_cables

import json

if __name__ == "__main__":
    district_number = "1"

    # battery_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_batteries.csv")

    battery_file = (f"SmartGrid/data/Huizen&Batterijen/district_{district_number}/district-{district_number}_batteries.csv")
    # battery_file = "/home/thomas61197/SmartGrid/data/Huizen&Batterijen/district_1/district-1_batteries.csv"

    # house_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")

    house_file = (f"SmartGrid/data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")
    # house_file = "/home/thomas61197/SmartGrid/data/Huizen&Batterijen/district_1/district-1_houses.csv"

    grid1 = grid.Grid(house_file, battery_file)

    # --------------------------- random --------------------------
    # random_costs = list()

    # for i in range(1000):
    #     random1 = random.Random(grid1)
    #     grid2 = random1.run()
    #     random_costs.append(grid2.calc_cost())
    
    # visualise_costs.visualise_costs(random_costs, "random")
    
    # --------------------------- greedy --------------------------
    # greedy1_costs = list()
    
    # for i in range(3):
    #     greedy1 = original_greedy.Greedy(grid1)
    #     greedy1.run()
    #     greedy1_costs.append(greedy1.grid.calc_cost())
    # visualise_costs.visualise_costs(greedy1_costs, "greedy1")

    # greedy1 = original_greedy.Greedy(grid1)
    # greedy1.run()

    # --------------------------- depth_first --------------------------
    # depth1 = depth_first.Depth_first(grid1)
    # depth1.run()
    # --------------------------- greedy 2 --------------------------
    #greedy2_costs = list()
    
    # for i in range(1000):
    #     greedy2 = greedy.Greedy(grid1).run_greedy
    #     grid4 = greedy2.run()
    #     greedy2_costs.append(grid4.calc_cost())

    # visualise_costs.visualise_costs(greedy2_costs, "greedy2")
    # greedy2_costs = list()
    
    # for i in range(3):
    #     greedy2 = greedy.Greedy(grid1)
    #     greedy2.run_greedy()
    #     greedy2_costs.append(greedy2.grid.calc_cost())
    # visualise_costs.visualise_costs(greedy2_costs, "greedy2")
    # --------------------------- Hill Climber ---------------------------------
    print("Setting up Hill Climber...")
    climber = hill_climber.Hill_climber(grid1)

    print("Running Hill Climber...")
    climber.run(2000, verbose=True)

    print(f"Value of the configuration after Hill Climber: "
          f"{climber.grid.calc_cost()}")

    # --------------------------- Simulated Annealing --------------------------
    # It is very difficult to find a good starting temperature for SA. A rule to
    # help you find one is to use the maximum change in score that could happen
    # when mutating your state. In our case, this is 19, because the transmitter
    # maximum difference in score between the most expensive and the cheapest
    # transmitter is 19.

    print("Setting up Simulated Annealing...")
    simanneal = simulated_annealing.Simulated_annealing(grid1, temperature=1250)
    
    print("Running Simulated Annealing...")
    simanneal.run(2000, verbose=True)
    
    print(f"Value of the configuration after Simulated Annealing: "
          f"{simanneal.grid.calc_cost()}")

    # --------------------------- compare --------------------------

    # visualise_costs.compare_costs(random_costs, "random", greedy_costs, "greedy")

    # --------------------------- output --------------------------
    
    # output = list()
    # out_grid = {"district": district_number, "costs-own": grid2.calc_cost()}
    # output.append(out_grid)

    # for battery in grid.batteries.values():
    #     out_battery = {}
    #     out_battery["location"] = f"{battery.x},{battery.y}"
    #     out_battery["capacity"] = battery.capacity
    #     out_battery["houses"] = list()

    #     for house in battery.houses.values():
    #         out_house = {}
    #         out_house["location"] = f"{house.x},{house.y}"
    #         out_house["output"] = house.max_output
    #         out_house["cables"] = list()

    #         for i in range(len(house.cable.x)):
    #             out_house["cables"].append(f"{house.cable.x[i]},{house.cable.y[i]}")
            
    #         out_battery["houses"].append(out_house)

    #     output.append(out_battery)

    # with open('/home/thomas61197/SmartGrid/docs/output.json', 'w') as outfile:
    #     json.dump(output, outfile)


# --------------------------- visualisation --------------------------
# visualise_cables2.visualise_cables(greedy1.grid)
