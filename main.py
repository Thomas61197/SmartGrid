from code.classes import grid
from code.algorithms import hill_climber, hill_climber_fix2, simulated_annealing, fix_greedy, greedy, original_greedy, baseline
from code.visualisations import visualise_costs, visualise_cables

import json
import pandas as pd
import pickle
import copy

if __name__ == "__main__":
    district_number = "1"

    # battery_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_batteries.csv")
    battery_file = (f"SmartGrid/data/Huizen&Batterijen/district_{district_number}/district-{district_number}_batteries.csv")

    # house_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")
    house_file = (f"SmartGrid/data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")

    empty_grid = grid.Grid(house_file, battery_file)

    # --------------------------- load pickled grid --------------------------

    file_name = "/home/thomas61197/SmartGrid/data/solutions/best_greedy_100k.pickle"

    with open(file_name, 'rb') as handle:
        best_greedy = pickle.load(handle)

    # --------------------------- baseline --------------------------
    # baseline_costs = list()
    # baseline1 = baseline.Baseline(empty_grid)
    # baseline1.run()
    # best_base = copy.deepcopy(baseline1)

    # for i in range(100000):
    #     baseline1 = baseline.Baseline(empty_grid)
    #     baseline1.run()
    #     print(f"i: {i}, cost: {best_base.grid.calc_cost()}")

    #     if baseline1.grid.calc_cost() < best_base.grid.calc_cost():
    #         best_base = copy.deepcopy(baseline1)

        # baseline_costs.append(baseline1.calc_cost())
        # if baseline1.grid.is_valid():
        #     print("hurray")
    
    # visualise_costs.visualise_costs(random_costs, "random")

    # file_name = f"SmartGrid/data/solutions/best_baseline.pickle"

    # with open(file_name, 'wb') as handle:
    #     pickle.dump(best_base, handle)
    
    # --------------------------- original greedy--------------------------
    # greedy1_costs = list()
    # greedy1 = original_greedy.Greedy(empty_grid)
    # greedy1.run()
    # best_greedy = copy.deepcopy(greedy1)

    # for i in range(100000):
    #     greedy1 = original_greedy.Greedy(empty_grid)
    #     greedy1.run()
    #     print(f"i: {i}, cost: {best_greedy.grid.calc_cost()}")

    #     if greedy1.grid.calc_cost() < best_greedy.grid.calc_cost():
    #         best_greedy = copy.deepcopy(greedy1)

        # greedy1_costs.append(greedy1.grid.calc_cost())

    # visualise_costs.visualise_costs(greedy1_costs, "greedy1")
    # file_name = f"SmartGrid/data/solutions/best_greedy.pickle"

    # with open(file_name, 'wb') as handle:
    #     pickle.dump(best_greedy, handle)

    # --------------------------- greedy 2 --------------------------
    # greedy2_costs = list()
    # greedy2 = greedy.Greedy(empty_grid)
    # greedy2.run_greedy()
    # best_greedy = copy.deepcopy(greedy2)
    
    # for i in range(100000):
    #     greedy2 = greedy.Greedy(empty_grid)
    #     greedy2.run_greedy()
    #     print(f"i: {i}, cost: {best_greedy.grid.calc_cost()}")

    #     if greedy2.grid.calc_cost() < best_greedy.grid.calc_cost():
    #         best_greedy = copy.deepcopy(greedy2)

        # fixed_greedy = fix_greedy.Fix_greedy(greedy2.grid)
        # fixed_greedy.run2()
        # greedy2_costs.append(greedy2.grid.calc_cost())

    # visualise_costs.visualise_costs(greedy2_costs, "greedy2")
    # file_name = f"SmartGrid/data/solutions/best_greedy_100k.pickle"
    for i in range(20):
        greedy2 = greedy.Greedy(grid1)
        greedy2.run_greedy()
        # fixed_greedy = fix_greedy.Fix_greedy(greedy2.grid)
        # fixed_greedy.run3()
        if greedy2.grid.is_valid():
             print("hurray")
        greedy2_costs.append(greedy2.grid.calc_cost())

    # with open(file_name, 'wb') as handle:
    #     pickle.dump(best_greedy, handle)


    # --------------------------- Hill Climber ---------------------------------
    best_greedy.grid.print_cum_output_per_battery()

    print("Setting up Hill Climber...")
    climber = hill_climber.Hill_climber(best_greedy.grid)

    print("Running Hill Climber...")
    climber.run(100, verbose=True)

    print(f"Value of the configuration after Hill Climber: "
          f"{climber.grid.calc_cost()}")

    print("valid?")
    print(climber.grid.is_valid())

    climber.grid.print_cum_output_per_battery()

    # --------------------------- Hill Climber fix 2 ---------------------------------

    # print(best_greedy.grid.calc_cost())
    
    # print("Setting up Hill Climber...")
    # climber = hill_climber_fix2.Hill_climber(best_greedy.grid)

    # print("Running Hill Climber...")
    # climber.run(1000000, verbose=True, mutate_houses_number=20)

    # print(f"Value of the configuration after Hill Climber: "
    #       f"{climber.grid.calc_cost()}")

    # print("valid?")
    # print(climber.grid.is_valid())

    # if climber.grid.is_valid():
    #     climber_id = 5
    #     file_name = f"SmartGrid/data/solutions/climber_{climber_id}_best_greedy.pickle"

    #     with open(file_name, 'wb') as handle:
    #         pickle.dump(climber, handle)

    # --------------------------- Simulated Annealing --------------------------
    # Simulated annealing 2 is different from simulated annealing 1 in that this one decreases the mutate_house_number linearly with each iteration, 
    # whereas in the other one the mutate_house_number is static.

    # print("Setting up Simulated Annealing...")
    # simanneal = simulated_annealing.Simulated_annealing(best_greedy.grid, temperature=(50+50)*9, mutate_house_number = 3, alpha = 0.994
    # , cooling_scheme="exponential")
    
    # print("Running Simulated Annealing...")
    # simanneal.run(1000, verbose=True, decreasing_mutate_house_number = False)
    
    # print(f"Value of the configuration after Simulated Annealing: "
    #       f"{simanneal.grid.calc_cost()}")

    # simanneal_id = 32

    # file_name = f"SmartGrid/data/solutions/simanneal_{simanneal_id}.pickle"

    # IMPORTANT: save simanneal object (if lots of iterations)!
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
    # experiments["mutate_house_number"] = simanneal.mutate_house_number
    # experiments["mutate_house_number_start"] = simanneal.mutate_house_number0

    # df_experiments = pd.DataFrame(experiments, index=[experiments['object_id']])
    # df_experiments_old = pd.read_csv("/home/thomas61197/SmartGrid/data/experiments.csv")
    # df_experiments_new = pd.concat([df_experiments_old.reset_index(drop=True), df_experiments.reset_index(drop=True)], ignore_index=True)
    # df_experiments_new.set_index('object_id')
    # print(df_experiments_new)
    # df_experiments_new.to_csv("/home/thomas61197/SmartGrid/data/experiments.csv", header = True, index = False)

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
# visualise_cables.visualise(greedy2.grid)
