# pip3 install matplotlib

import matplotlib.pyplot as plt
import numpy as np

def visualise_costs(costs, algo):
    print('mean costs of', algo, 'is', sum(costs)/len(costs))

    plt.figure()
    plt.title(f"{algo} algorithm costs")
    plt.xlabel("Iteration")
    plt.ylabel("Cost")
    plt.scatter(list(range(len(costs))), costs)
    #plt.savefig(f'SmartGrid/docs/{algo}_costs.png')
    plt.savefig(f'docs/{algo}_costs.png')

def histogram_costs(costs, algo, nbins):
    """
    Make a histogram with the frequency of output costs of the algorithm, for a number of iterations
    """
    plt.figure()
    plt.title(f"Frequency different {algo} algorithm costs for {len(costs)} iterations")
    plt.xlabel("Cost")
    plt.ylabel("Frequency")
    plt.style.use('ggplot')
    plt.hist(costs, bins=nbins, color="maroon")
    plt.savefig(f'docs/hist_{algo}_costs.png')

def compare_costs(costs1, algo1, costs2, algo2):
    plt.figure()
    plt.title("cost comparison")
    plt.xlabel("algorithm")
    plt.ylabel("average cost")
    plt.bar(f"{algo1}", np.mean(costs1))
    plt.bar(f"{algo2}", np.mean(costs2))
    plt.savefig(f'SmartGrid/docs/comparison_costs.png')
    