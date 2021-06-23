from code.visualisations import visualise_costs, visualise_cables
import pickle

file_name = "/home/ysanne/SmartGrid/data/solutions/best_greedy2_100k_dis1.pickle"

with open(file_name, 'rb') as handle:
    greedy2_dis1 = pickle.load(handle)
    
visualise_cables.visualise(greedy2_dis1.grid, district_number = 1)