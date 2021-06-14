from numpy import complexfloating
from pandas.core.indexes.base import Index
from code.classes import grid
from code.algorithms import hill_climber, simulated_annealing2, simulated_annealing
# from code.visualisations import visualise_costs,  visualise_cables

import json
import pandas as pd
import pickle

if __name__ == "__main__":
    district_number = "1"

    # battery_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_batteries.csv")
    battery_file = (f"SmartGrid/data/Huizen&Batterijen/district_{district_number}/district-{district_number}_batteries.csv")

    # house_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")
    house_file = (f"SmartGrid/data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")

    grid1 = grid.Grid(house_file, battery_file)

    # --------------------------- random --------------------------
    # random_costs = list()

    # for i in range(1000):
    #     random1 = random.Random(grid1)
    #     grid2 = random1.run()
    #     random_costs.append(grid2.calc_cost())
    
    # visualise_costs.visualise_costs(random_costs, "random")
    
    # --------------------------- original greedy--------------------------
    # greedy1_costs = list()

    # for i in range(1000):
    #     greedy1 = original_greedy.Greedy(grid1)
    #     greedy1.run()
    #     greedy1_costs.append(greedy1.grid.calc_cost())
    # visualise_costs.visualise_costs(greedy1_costs, "greedy1")

    # greedy1 = original_greedy.Greedy(grid1)
    # greedy1.run()

    # --------------------------- greedy 2 --------------------------
    #greedy2_costs = list()
    
    # for i in range(1000):
    #     greedy2 = greedy.Greedy(grid1)
    #     greedy2.run_greedy()
    #     greedy2_costs.append(greedy2.grid.calc_cost())

    # visualise_costs.visualise_costs(greedy2_costs, "greedy2")

    # --------------------------- Hill Climber ---------------------------------
    # print("Setting up Hill Climber...")
    # climber = hill_climber.Hill_climber(grid1)

    # print("Running Hill Climber...")
    # climber.run(2000, verbose=True)

    # print(f"Value of the configuration after Hill Climber: "
    #       f"{climber.grid.calc_cost()}")

    # --------------------------- Simulated Annealing --------------------------
    # It is very difficult to find a good starting temperature for SA. A rule to
    # help you find one is to use the maximum change in score that could happen
    # when mutating your state. In our case, this is 19, because the transmitter
    # maximum difference in score between the most expensive and the cheapest
    # transmitter is 19.
    # maximum difference = (breadth of grid + height of grid) * 9.

    # print("Setting up Simulated Annealing...")
    # simanneal = simulated_annealing.Simulated_annealing(grid1, temperature=(50+50)*9, cooling_scheme="exponential", alpha=0.99999)
    
    # mutate_houses_number = 3
    # print("Running Simulated Annealing...")
    # simanneal.run(1000000, verbose=True, mutate_houses_number = mutate_houses_number)
    
    # print(f"Value of the configuration after Simulated Annealing: "
    #       f"{simanneal.grid.calc_cost()}")

    # simanneal_id = 19
    # file_name = f"SmartGrid/data/solutions/simanneal_{simanneal_id}.pickle"

    # # IMPORTANT: save simanneal object (if lots of iterations)!
    # with open(file_name, 'wb') as handle:
    #     pickle.dump(simanneal, handle)

    # experiments = {}
    # experiments["object_id"] = simanneal_id
    # experiments["district"] = district_number
    # experiments["object_type"] = "simanneal"
    # experiments["cost"] = simanneal.grid.calc_cost()
    # experiments["start_grid"] = "original_greedy"
    # experiments["temperature"] = simanneal.T0
    # experiments["cooling_scheme"] = simanneal.cooling_scheme
    # experiments["alpha"] = simanneal.alpha
    # experiments["iterations"] = simanneal.iterations
    # experiments["mutate_houses_number"] = mutate_houses_number

    # df_experiments = pd.DataFrame(experiments, index=[experiments['object_id']])
    # df_experiments_old = pd.read_csv("/home/thomas61197/SmartGrid/data/experiments.csv")
    # df_experiments_new = pd.concat([df_experiments_old.reset_index(drop=True), df_experiments.reset_index(drop=True)], ignore_index=True)
    # df_experiments_new.set_index('object_id')
    # print(df_experiments_new)
    # df_experiments_new.to_csv("/home/thomas61197/SmartGrid/data/experiments.csv", header = True, index = False)

    # --------------------------- Simulated Annealing 2 --------------------------

    print("Setting up Simulated Annealing...")
    simanneal = simulated_annealing2.Simulated_annealing(grid1, temperature=(50+50)*9, mutate_house_number = 2)
    
    print("Running Simulated Annealing...")
    simanneal.run(1000, verbose=True)
    
    print(f"Value of the configuration after Simulated Annealing: "
          f"{simanneal.grid.calc_cost()}")

    simanneal_id = 27

    # file_name = f"SmartGrid/data/solutions/simanneal_{simanneal_id}.pickle"

    # # IMPORTANT: save simanneal object (if lots of iterations)!
    # with open(file_name, 'wb') as handle:
    #     pickle.dump(simanneal, handle)

    experiments = {}
    experiments["object_id"] = simanneal_id
    experiments["district"] = district_number
    experiments["object_type"] = "simanneal"
    experiments["cost"] = simanneal.grid.calc_cost()
    experiments["start_grid"] = "original_greedy"
    experiments["temperature"] = simanneal.T0
    experiments["cooling_scheme"] = simanneal.cooling_scheme
    experiments["alpha"] = simanneal.alpha
    experiments["iterations"] = simanneal.iterations
    experiments["mutate_house_number"] = simanneal.mutate_house_number
    experiments["mutate_house_number_start"] = simanneal.mutate_house_number0

    df_experiments = pd.DataFrame(experiments, index=[experiments['object_id']])
    df_experiments_old = pd.read_csv("/home/thomas61197/SmartGrid/data/experiments.csv")
    df_experiments_new = pd.concat([df_experiments_old.reset_index(drop=True), df_experiments.reset_index(drop=True)], ignore_index=True)
    df_experiments_new.set_index('object_id')
    print(df_experiments_new)
    df_experiments_new.to_csv("/home/thomas61197/SmartGrid/data/experiments.csv", header = True, index = False)

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
