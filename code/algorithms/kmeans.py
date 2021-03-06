# ---------------------------------- summary ----------------------------------
# K-means is a classic example of unsupervised learning: there is no target that we are trying to predict, and instead we are trying to extract a hidden structure. 
# The goal of k-means is to find  π  clusters, or groups, within a dataset. 
# Each cluster is represented by a point  π , and the data points that are closest to that point are assigned to the corresponding cluster. 
# The means aspect of the algorithm comes from how these cluster representations are calculated: by computing the mean of the points currently assigned to that cluster.



# ---------------------------------- pseudocode --------------------------------

# INPUT: a data set X (of size NxD) <Grid, the number of clusters π <nbattries

# Initialize π  mean vectors  ππ  (each of size 1xD) to k random data points in X


# Do:
    # For each data point <house π₯π  in  π <houses:
        # Find the mean  ππ  with the minimum squared <manhattan> distrance to battery  π₯π : argmin π ||π₯πβππ||2 <replace by manhattan distance
        # Assign  π₯π <house to the  π th cluster  πΆπ <battery, which had the nearest mean  ππ .
        # For each mean  ππ  for  πβ[1,β¦,π] :
            # Re-compute the mean  ππ  by taking the mean of the points <houses currently assigned to cluster  πΆπ  <battery:  ππ=1|πΆπ|βπ₯βπΆππ₯ , where  |πΆπ|  denotes the number of points <houses currently assigned to cluster  πΆπ  <battery and the sum is taken over all data points in  πΆπ .

# While:
    #  Not Converged: The cluster assignments have changed from the previous iteration of the Do-loop.


# OUTPUT: the cluster means  {π1,β¦,ππ} <best batterie coordinates, the cluster assignments (cluster index per data point)



# ---------------------------------- implementation --------------------------------
# import numpy as np

# # k, number of clusters     = nbatteries        "4"
# # x, datapoints             = housecoordinates  "[[1.6 0.4][1.5 0.4][4.  1.2] ... ]"
# def init_clusters(x, k):
#     ''' Randomly initialize the π means for the number of batteries from π random house coordinates '''
#     np.random.shuffle(x)
#     return x[:k]


# # x0, coordinate input 1     = battery       "[1.4 0.3]"
# # x0, coordinate input 2     = house         "[4.5 1.5]"
# def distance(x0, x1):
#     ''' Computes Manhattan distance between two inputs '''
#     return np.sum((x1-x0)**2) # <--- replace for manhattan distance



