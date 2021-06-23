from code.classes import grid
from code.algorithms import hill_climber, simulated_annealing, cheapest_greedy, greedy, original_greedy, baseline
from code.visualisations import visualise_costs, visualise_cables

import json
import pandas as pd
import pickle
import copy

if __name__ == "__main__":
    district_number = "2"
    greedy_version = 4

    # Load in the data files
    battery_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_batteries.csv")
    # battery_file = (f"SmartGrid/data/Huizen&Batterijen/district_{district_number}/district-{district_number}_batteries.csv")

    house_file = (f"data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")
    # house_file = (f"SmartGrid/data/Huizen&Batterijen/district_{district_number}/district-{district_number}_houses.csv")

    empty_grid = grid.Grid(house_file, battery_file)

    # --------------------------- load pickled grid --------------------------

    # file_name = "/home/thomas61197/SmartGrid/data/solutions/best_greedy_100k.pickle"
    # file_name = "/home/thomas61197/SmartGrid/data/solutions/best_original_greedy.pickle"
    # file_name = "/home/thomas61197/SmartGrid/data/solutions/simanneal_cable_to_cable_34.pickle"
    # file_name = "/home/thomas61197/SmartGrid/data/solutions/10k_it_or_greedy_ctc_dis1.pickle"
    # file_name = "/home/thomas61197/SmartGrid/data/solutions/best_baseline_100k.pickle"
    # file_name = "/home/thomas61197/SmartGrid/data/solutions/10k_it_or_greedy_ctc_dis1_1mil_it_simanneal_36_ctc.pickle"
    # file_name = "/home/thomas61197/SmartGrid/data/solutions/best_solution_yet_dis1_sa_valid.pickle"
    # file_name = "/home/thomas61197/SmartGrid/data/solutions/5k_it_or_greedy_ctc_dis2_1mil_it_simanneal_37_ctc.pickle"
    # file_name = "/home/thomas61197/SmartGrid/data/solutions/5k_or_greedy_ctc_dis3_100k_sa_38_ctc.pickle"
    file_name = f"/home/thomas61197/SmartGrid/data/solutions/final/district{district_number}/simulated_annealing/final_sa_valid_dis{district_number}.pickle"

    with open(file_name, 'rb') as handle:
        # best_greedy = pickle.load(handle)
        # best_original_greedy = pickle.load(handle)
        # simanneal_cable_to_cable = pickle.load(handle)
        # best_base = pickle.load(handle)
        final_sa_valid = pickle.load(handle)

    # best_original_greedy.grid.print_status_batteries()

    # save as
    grid_name = f"final2_sa_valid_dis{district_number}"

    # --------------------------- baseline --------------------------
    if greedy_version == None:
        """
        Baseline, connects random house to random battery that is not yet full
        """
        print('Running baseline version..')

        # make a list which holds the cost of the grid after each iteration
        baseline_costs = list()

        # instantiate the algorithm with an empty grid
        baseline1 = baseline.Baseline(empty_grid)

        baseline1.run()

        # save a copy of the cheapest grid found so far
        best_base = copy.deepcopy(baseline1)

        # run the algorithm a number of times
        for i in range(1):
            baseline1 = baseline.Baseline(empty_grid)
            baseline1.run()
            print(f"i: {i}, cost: {best_base.grid.calc_cost()}")

            if baseline1.grid.calc_cost2() < best_base.grid.calc_cost2():
                best_base = copy.deepcopy(baseline1)

            baseline_costs.append(baseline1.grid.calc_cost())
        
        # visualise_costs.visualise_costs(baseline_costs, "random")

        # file_name = f"SmartGrid/data/solutions/best_baseline.pickle"

        # with open(file_name, 'wb') as handle:
        #     pickle.dump(best_base, handle)
    
    # --------------------------- original greedy--------------------------
    if greedy_version == 1:
        """
        If battery is full, reconnects the house with the lowest cost
        """
        print('running Greedy version 1..')

        # Instantiate Greedy with an empty grid
        greedy1_costs = list()
        greedy1 = original_greedy.Greedy(empty_grid)
        greedy1.run()
        best_greedy = copy.deepcopy(greedy1)

        for i in range(5000):
            greedy1 = original_greedy.Greedy(empty_grid)
            greedy1.run()
            print(f"i: {i}, cost: {best_greedy.grid.calc_cost2()}")

            # If this run is cheaper, make it the new best grid
            if greedy1.grid.calc_cost2() < best_greedy.grid.calc_cost2():
                best_greedy = copy.deepcopy(greedy1)

            greedy1_costs.append(greedy1.grid.calc_cost2())

        # visualise_costs.visualise_costs(greedy1_costs, "greedy1")

        file_name = f"SmartGrid/data/solutions/5k_or_greedy_ctc_dis{district_number}.pickle"

        with open(file_name, 'wb') as handle:
            pickle.dump(best_greedy, handle)

        file_name = f"SmartGrid/data/solutions/5k_or_greedy_ctc_dis{district_number}_cost_list.pickle"

        with open(file_name, 'wb') as handle:
            pickle.dump(greedy1_costs, handle)
    
    # --------------------------- greedy 2 --------------------------
    if greedy_version == 2:
        """
        If battery is full, reconnects the house that costs the least to replace to another battery
        """
        print('Running Greedy version 2..')
        greedy2_costs = list()
        best_cost = 70000


        for i in range(100):
            greedy2 = greedy.Greedy(empty_grid)
            greedy2.run_greedy()
            
            # If this run is valid ánd cheaper, make it the best grid
            if greedy2.grid.is_valid():
                if greedy2.grid.calc_cost2() < best_cost:
                    best_grid = greedy2.grid
                    best_cost = greedy2.grid.calc_cost2()
                    # best_greedy2_100k_ctc_dis2 = greedy2

            greedy2_costs.append(greedy2.grid.calc_cost2())
            # print(f'iteration {i}', greedy2.grid.calc_cost2())

        print('Price cheapest valid Greedy:', best_cost)
        visualise_costs.histogram_costs(greedy2_costs, "greedy2", nbins = 50)

        # Pickle best greedy 
        # file_name = f"data/solutions/best_greedy2_100k_dis2.pickle"

        # with open(file_name, 'wb') as handle:
        #     pickle.dump(best_greedy2_100k_ctc_dis2, handle)

        # --------------------------- greedy - each house to closest battery--------------------------
    if greedy_version == 3:
        """
        Connects each house to closest battery. Lowest cost baseline.
        """

        print('Running Greedy version 3..')
        greedy3_costs = list()

        for i in range(100):
            greedy3 = cheapest_greedy.Greedy_cheapest(empty_grid)
            greedy3.run_greedy()
            greedy3_costs.append(greedy3.grid.calc_cost())

        visualise_costs.visualise_costs(greedy3_costs, "greedy3")
    
    # --------------------------- Simulated Annealing --------------------------
    """
    A starting temperature of (51+51)*9 was chosen because, often, a good starting temperature for this algorithm is equal to the 
    maximum difference in the value you are trying to maximize/minimize. In this case, the grid has a length of 51, a breadth of 51
    and the cost of laying a piece of cable on asingle grid segment is 9.

    """
    # print("Setting up Simulated Annealing...")
    # simanneal = simulated_annealing.Simulated_annealing(best_greedy.grid, temperature=(51+51)*9, mutate_house_number = 3
    # , alpha = 0.9999, cooling_scheme="exponential", cable_to_cable = True, lay_cable = "to_closest_cable", decreasing_mutate_house_number = False)
    
    # print("Running Simulated Annealing...")
    # simanneal.run(100000, verbose=True)
    
    # print(f"Value of the configuration after Simulated Annealing: "
    #       f"{simanneal.grid.calc_cost2()}")

    # simanneal_id = 38

    # file_name = f"SmartGrid/data/solutions/5k_or_greedy_ctc_dis{district_number}_100k_sa_{simanneal_id}_ctc.pickle"

    # # IMPORTANT: save simanneal object (if lots of iterations)!
    # with open(file_name, 'wb') as handle:
    #     pickle.dump(simanneal, handle)

    # experiments = {}
    # experiments["object_id"] = simanneal_id
    # experiments["district"] = district_number
    # experiments["object_type"] = "simanneal"
    # experiments["cost"] = simanneal.grid.calc_cost2()
    # experiments["start_grid"] = "5k_original_greedy_ctc"
    # experiments["temperature"] = simanneal.T0
    # experiments["cooling_scheme"] = simanneal.cooling_scheme
    # experiments["alpha"] = simanneal.alpha
    # experiments["iterations"] = simanneal.iterations
    # experiments["mutate_house_number"] = simanneal.mutate_house_number
    # experiments["mutate_house_number_start"] = simanneal.mutate_house_number0
    # experiments["cable_to_cable"] = simanneal.cable_to_cable

    # df_experiments = pd.DataFrame(experiments, index=[experiments['object_id']])
    # df_experiments_old = pd.read_csv("/home/thomas61197/SmartGrid/data/experiments.csv")
    # df_experiments_new = pd.concat([df_experiments_old.reset_index(drop=True), df_experiments.reset_index(drop=True)]
    # , ignore_index=True)
    # df_experiments_new.set_index('object_id')
    # print(df_experiments_new)
    # df_experiments_new.to_csv("/home/thomas61197/SmartGrid/data/experiments.csv", header = True, index = False)

    # --------------------------- Hill Climber (fix) ---------------------------------
    
    print("Setting up Hill Climber...")
    climber = hill_climber.Hill_climber(final_sa_valid.grid, mutate_house_number = 3, cable_to_cable = True
    , minimalize_surplus = True, with_checkpoints = False, lay_cable = "to_closest_cable", cost_and_surplus=True
    , decreasing_mutate_house_number = False)

    # print("Running Hill Climber...")
    climber.run(100000, verbose=True)

    # print(f"Value of the configuration after Hill Climber: "
    #       f"{climber.grid.calc_cost2()}")

    if climber.grid.is_valid():
        climber_id = 10
        file_name = f"SmartGrid/data/solutions/final/district{district_number}/simulated_annealing/{grid_name}.pickle"

    #     with open(file_name, 'wb') as handle:
    #         pickle.dump(climber, handle)

    # --------------------------- visualisation --------------------------
    # visualise_cables.visualise(greedy3.grid)

    # visualise_cables.visualise(simanneal.grid, district_number)
    # visualise_cables.visualise_apart(simanneal.grid, district_number)
    # visualise_cables.visualise_house_apart(simanneal.grid, district_number)

    visualise_cables.visualise(climber.grid, district_number, grid_name=grid_name)
    visualise_cables.visualise_apart(climber.grid, district_number, grid_name=grid_name)

    # visualise_cables.visualise(greedy2_dis1.grid, district_number)
    # visualise_cables.visualise_empty_grid(best_grid, district_number)
    # visualise_cables.visualise_apart(best_greedy.grid, district_number)
    # visualise_cables.visualise_house_apart(greedy1.grid, district_number)

    # visualise_cables.visualise(best_original_greedy.grid, district_number)
    # visualise_cables.visualise_apart(best_original_greedy.grid, district_number)

    # visualise_cables.visualise_apart(best_grid, district_number)
    # visualise_cables.visualise(best_grid, district_number)
    # visualise_cables.visualise_house_apart(best_grid, district_number)

    # visualise_cables.visualise(final_sa_valid_dis1.grid, district_number, grid_name=grid_name)
    # visualise_cables.visualise_apart(final_sa_valid_dis1.grid, district_number, grid_name=grid_name)

    # --------------------------- compare --------------------------

    # visualise_costs.compare_costs(random_costs, "random", greedy_costs, "greedy")

    # --------------------------- output --------------------------
    
    output = list()
    greedy_grid = best_grid_greedy2_dis1.grid
    out_grid = {"district": district_number, "costs-shared": greedy_grid.calc_cost2()}
    output.append(out_grid)

    for battery in greedy_grid.batteries.values():
        out_battery = {}
        out_battery["location"] = f"{battery.x},{battery.y}"
        out_battery["capacity"] = battery.capacity
        out_battery["houses"] = list()

        for house in battery.houses.values():
            out_house = {}
            out_house["location"] = f"{house.x},{house.y}"
            out_house["output"] = house.max_output
            out_house["cables"] = list()

            for i in range(len(house.cable.x)):
                out_house["cables"].append(f"{house.cable.x[i]},{house.cable.y[i]}")
            
            out_battery["houses"].append(out_house)

        output.append(out_battery)

    with open('/home/ysanne/SmartGrid/docs/output.json', 'w') as outfile:
        json.dump(output, outfile)



