# pip3 install matplotlib

import matplotlib.pyplot as plt
import numpy as np

def visualise_costs(costs, algo):
    plt.figure()
    plt.title(f"{algo} algorithm costs")
    plt.xlabel("iteration")
    plt.ylabel("cost")
    plt.scatter(list(range(len(costs))), costs)
    plt.savefig(f'SmartGrid/docs/{algo}_costs.png')

def compare_costs(costs1, algo1, costs2, algo2):
    plt.figure()
    plt.title("cost comparison")
    plt.xlabel("algorithm")
    plt.ylabel("average cost")
    plt.bar(f"{algo1}", np.mean(costs1))
    plt.bar(f"{algo2}", np.mean(costs2))
    plt.savefig(f'SmartGrid/docs/comparison_costs.png')
    