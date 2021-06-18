# ---------------------------------- summary ----------------------------------
# K-means is a classic example of unsupervised learning: there is no target that we are trying to predict, and instead we are trying to extract a hidden structure. 
# The goal of k-means is to find  𝑘  clusters, or groups, within a dataset. 
# Each cluster is represented by a point  𝑚 , and the data points that are closest to that point are assigned to the corresponding cluster. 
# The means aspect of the algorithm comes from how these cluster representations are calculated: by computing the mean of the points currently assigned to that cluster.



# ---------------------------------- pseudocode --------------------------------

# INPUT: a data set X (of size NxD) <Grid, the number of clusters 𝑘 <nbattries

# Initialize 𝑘  mean vectors  𝑚𝑗  (each of size 1xD) to k random data points in X


# Do:
    # For each data point <house 𝑥𝑛  in  𝑋 <houses:
        # Find the mean  𝑚𝑗  with the minimum squared <manhattan> distrance to battery  𝑥𝑛 : argmin 𝑗 ||𝑥𝑛−𝑚𝑗||2 <replace by manhattan distance
        # Assign  𝑥𝑛 <house to the  𝑗 th cluster  𝐶𝑗 <battery, which had the nearest mean  𝑚𝑗 .
        # For each mean  𝑚𝑗  for  𝑗∈[1,…,𝑘] :
            # Re-compute the mean  𝑚𝑗  by taking the mean of the points <houses currently assigned to cluster  𝐶𝑗  <battery:  𝑚𝑗=1|𝐶𝑗|∑𝑥∈𝐶𝑗𝑥 , where  |𝐶𝑗|  denotes the number of points <houses currently assigned to cluster  𝐶𝑗  <battery and the sum is taken over all data points in  𝐶𝑗 .

# While:
    #  Not Converged: The cluster assignments have changed from the previous iteration of the Do-loop.


# OUTPUT: the cluster means  {𝑚1,…,𝑚𝑘} <best batterie coordinates, the cluster assignments (cluster index per data point)



# ---------------------------------- implementation --------------------------------
# import numpy as np

# # k, number of clusters     = nbatteries        "4"
# # x, datapoints             = housecoordinates  "[[1.6 0.4][1.5 0.4][4.  1.2] ... ]"
# def init_clusters(x, k):
#     ''' Randomly initialize the 𝑘 means for the number of batteries from 𝑘 random house coordinates '''
#     np.random.shuffle(x)
#     return x[:k]


# # x0, coordinate input 1     = battery       "[1.4 0.3]"
# # x0, coordinate input 2     = house         "[4.5 1.5]"
# def distance(x0, x1):
#     ''' Computes Manhattan distance between two inputs '''
#     return np.sum((x1-x0)**2) # <--- replace for manhattan distance



