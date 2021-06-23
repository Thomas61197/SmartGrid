from code.classes import grid
from code.algorithms import hill_climber, simulated_annealing, cheapest_greedy, fix_greedy, greedy, original_greedy, baseline
from code.visualisations import visualise_costs, visualise_cables

import json
import pandas as pd
import pickle
import copy

if __name__ == "__main__":
    district_number = "2"
    greedy_version = 2

    battery_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_batteries.csv")
    #battery_file = (f"SmartGrid/data/Huizen&Batterijen/district_{district_number}/district-{district_number}_batteries.csv")

    house_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")
    #house_file = (f"SmartGrid/data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")

    empty_grid = grid.Grid(house_file, battery_file)

    # --------------------------- load pickled grid --------------------------

    # file_name = "/home/thomas61197/SmartGrid/data/solutions/best_greedy_100k.pickle"
    # file_name = "/home/thomas61197/SmartGrid/data/solutions/best_original_greedy.pickle"
    # file_name = "/home/thomas61197/SmartGrid/data/solutions/simanneal_cable_to_cable_34.pickle"

    # with open(file_name, 'rb') as handle:
        # best_greedy = pickle.load(handle)
        # best_original_greedy = pickle.load(handle)
        # simanneal_cable_to_cable = pickle.load(handle)

    # --------------------------- baseline --------------------------
    if greedy_version == "baseline":
        print('Running baseline version..')
        baseline_costs = list()
        baseline1 = baseline.Baseline(empty_grid)
        baseline1.run()
        # best_base = copy.deepcopy(baseline1)

        for i in range(1):
            baseline1 = baseline.Baseline(empty_grid)
            baseline1.run()
            # print(f"i: {i}, cost: {best_base.grid.calc_cost()}")

            # if baseline1.grid.calc_cost() < best_base.grid.calc_cost():
            #     best_base = copy.deepcopy(baseline1)

            baseline_costs.append(baseline1.grid.calc_cost())
            # if baseline1.grid.is_valid():
            #     print("hurray")
        
        visualise_costs.visualise_costs(baseline_costs, "random")

        # file_name = f"SmartGrid/data/solutions/best_baseline.pickle"

        # with open(file_name, 'wb') as handle:
        #     pickle.dump(best_base, handle)
    
    # --------------------------- original greedy--------------------------
    if greedy_version == 1:
        print('running Greedy version 1..')
        # greedy1_costs = list()
        greedy1 = original_greedy.Greedy(empty_grid)
        greedy1.run()
        best_greedy = copy.deepcopy(greedy1)

        for i in range(1):
            greedy1 = original_greedy.Greedy(empty_grid)
            greedy1.run()
            print(f"i: {i}, cost: {best_greedy.grid.calc_cost()}")

            if greedy1.grid.calc_cost() < best_greedy.grid.calc_cost():
                best_greedy = copy.deepcopy(greedy1)

            greedy1_costs.append(greedy1.grid.calc_cost())
        print(count)
        best_grid = best_greedy.grid
        visualise_costs.visualise_costs(greedy1_costs, "greedy1")
        # file_name = f"SmartGrid/data/solutions/best_greedy.pickle"

        # with open(file_name, 'wb') as handle:
        #     pickle.dump(best_greedy, handle)
    
    # --------------------------- greedy 2 --------------------------
    if greedy_version == 2:

        print('Running Greedy version 2..')
        greedy2_costs = list()
        best_cost = 70000


        for i in range(100000):
            greedy2 = greedy.Greedy(empty_grid)
            greedy2.run_greedy()
            
            if greedy2.grid.is_valid():
                if greedy2.grid.calc_cost2() < best_cost:
                    best_grid = greedy2.grid
                    best_cost = greedy2.grid.calc_cost2()
                    best_greedy2_100k_ctc_dis2 = greedy2
            greedy2_costs.append(greedy2.grid.calc_cost2())
            # print(f'iteration {i}', greedy2.grid.calc_cost2())

        print('Price cheapest valid Greedy:', best_cost)
        visualise_costs.histogram_costs(greedy2_costs, "greedy2", nbins = 50)

        file_name = f"data/solutions/best_greedy2_100k_dis2.pickle"

        with open(file_name, 'wb') as handle:
            pickle.dump(best_greedy2_100k_ctc_dis2, handle)

    # --------------------------- visualisation --------------------------
    # visualise_cables.visualise_apart(best_grid, district_number)
    # visualise_cables.visualise(best_grid, district_number)
    # visualise_costs.histogram_costs(greedy2_costs, "greedy2", nbins = 50)

        # --------------------------- greedy - each house to closest battery--------------------------
    if greedy_version == 3:

        print('Running Greedy version 3, connecting each house to closest battery..')
        greedy3_costs = list()

        for i in range(100):
            greedy3 = cheapest_greedy.Greedy_cheapest(empty_grid)
            greedy3.run_greedy()
            if greedy3.grid.is_valid():
                print("hurray")

            greedy3_costs.append(greedy3.grid.calc_cost())

        visualise_costs.visualise_costs(greedy3_costs, "greedy3")
    
    # --------------------------- Simulated Annealing --------------------------
    # Simulated annealing 2 is different from simulated annealing 1 in that this one decreases the mutate_house_number linearly with 
    # each iteration, whereas in the other one the mutate_house_number is static.

    # print("Setting up Simulated Annealing...")
    # simanneal = simulated_annealing.Simulated_annealing(greedy1.grid, temperature=(50+50)*9, mutate_house_number = 3
    # , alpha = 0.999, cooling_scheme="exponential", cable_to_cable = True)
    
    # print("Running Simulated Annealing...")
    # simanneal.run(100, verbose=True, decreasing_mutate_house_number = False)
    
    # print(f"Value of the configuration after Simulated Annealing: "
    #       f"{simanneal.grid.calc_cost2()}")

    # simanneal_id = 35

    # file_name = f"SmartGrid/data/solutions/simanneal_cable_to_cable_{simanneal_id}.pickle"

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

    # --------------------------- Hill Climber (fix) ---------------------------------

    # print(best_greedy2_1000_ctc.grid.calc_cost())
    
    # # print("Setting up Hill Climber...")
    # climber = hill_climber.Hill_climber(best_greedy2_1000_ctc.grid, fix = True, mutate_house_number=10)

    # # print("Running Hill Climber...")
    # climber.run(1000, verbose=True)

    # print(f"Value of the configuration after Hill Climber: "
    #       f"{climber.grid.calc_cost2()}")

    # print("valid?")
    # print(climber.grid.is_valid())

    # if climber.grid.is_valid():
    #     climber_id = 6
    #     file_name = f"data/solutions/climber_{climber_id}_best_greedy2_1000_c2c.pickle"

    #     with open(file_name, 'wb') as handle:
    #         pickle.dump(climber, handle)


    # --------------------------- visualisation --------------------------
    # visualise_cables.visualise(greedy3.grid, district_number)
    # visualise_cables.visualise(simanneal.grid, district_number)
    # visualise_cables.visualise(climber.grid, district_number)
    # visualise_cables.visualise(greedy1.grid, district_number)

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



