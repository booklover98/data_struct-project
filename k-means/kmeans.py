# <cheesy-javadoc-style-header>
############################
# version 0.1.1.1.25
# Group: Sunny Patel, Ari Lotter, Samantha Husack
#
# Instructions: This file is not intended to be run as a standalone program
#               Instead, run kmeans-GUI.py, which imports this file :)
#
# Additional features: 3-D plotting and higher-dimensional capability, GUI
############################
# </cheesy-javadoc-style-header>

import numpy as np
import matplotlib.pyplot as plt
import math
import timeit
import random
from random import randint
from operator import add
from mpl_toolkits.mplot3d import Axes3D

#Cluster class, defines a cluster with a center and a bunch of points assigned to that center
class Cluster:

    #Constructor:
    #@param mean: tuple (a tuple that represents apoint in d-dimensions
    #Defines the center a blank list of points, and a list of points from the previous assignment
    def __init__( self, mean ):
        self.mean = mean
        self.points = []
        self.prevPoints = []

    #Assign a point to this cluster if this cluster is the closest cluster to that point
    #@param point: tuple - A point to add to the cluster
    def addPoints (self, point):
        self.points.append(point)

    #Back up all current points to a a secondary list and purge existing list to prep for re-assignment
    def backup(self):
        self.prevPoints = list(self.points)
        self.points = []

    #Only to be used post-assignment
    #Checks to see if there was a change in points assigned to cluster over the last 2 assignments
    def checkChanged(self):
        if (len(self.prevPoints) == 0): return False
        return set(self.prevPoints) == set(self.points)

#ASSIGNMENT PHASE
#Assigns points to a cluster the center of that cluster is the closeest to that point, for every point in the dataset
#@param
    #clusters: Cluster[] - A list of k clusters that exist
    #datset: tuple[] - A list of all points in the dataset, as tuples of length d
#@return true if the values are converged (i.e. no changes found since last assignment for every cluster), false otherwise
def assignToCluster(clusters, dataset):
    #Assume points are converged unless proven otherwise
    converged = True

    #For every point, consider every cluster
    for point in dataset:
        #Set the minimum distance and associated cluster to cluster 0 (just in case a distance of 100000 doesn't suffice)
        minDist = euclDistGeneral(point, clusters[0].mean)
        minCluster = clusters[0]

        #Compare euclidean distance to every cluster. Add point to the smallest
        for cluster in clusters:
            if euclDistGeneral(point, cluster.mean) < minDist:
                minDist = euclDistGeneral(point, cluster.mean);
                minCluster = cluster
        minCluster.addPoints(point)

    #Check to see if a change occured. If it did, points may not be converged
    for cluster in clusters:
        changeOccured = cluster.checkChanged()

        if (not changeOccured):
            converged = False

    #Return if points are converged
    return converged

#ReCENTERING PHASE
#Recalculates the centers for each cluster to be the centroid of all points in that cluster
#Additionaly uses the Cluster.backup() method to copy current points to a secondary array for comparison purposes
#@params
    #clusters: Cluster[] - A list of k clusters that were assigned points in the previous phase
def shiftMeans(clusters):

    for cluster in clusters: #For every cluster, find the centroid, assign to mean
        
        average = (0,)*len(cluster.mean)#set average to (0,0) or (0,0,0) etc. depending on dimension size
        for point in cluster.points:
            average = tuple(map(add, point, average))
        average = tuple(map(lambda x : x/len(cluster.points), average))
        
        cluster.mean = average
        cluster.backup()#Back up the cluster to prep for next assignment phase

#Calculates the euclidean distance in d dimensions
#@params
    #pointA: tuple - A tuple of length d that contains the first point to compare
    #pointB: tuple - A tuple of length d that contains the second point to compare
#@output: float - the euclidean distance, squared
def euclDistGeneral (pointA, pointB):
    sum = 0
    for i in range (0, len(pointA)):
        sum += (pointA[i] - pointB[i])**2
    return sum

#Runs the k-means algorithm for 2 or 3 dimensions given a string of CSV data
#@params
    #k: integer         - the number of clusters required
    #CSVString: string  - the string of csv values to be used as a datset
        #format: d (dimensional) comma separated values per line, first line ignored as headings
#@output: MatPlotLib.pyplot plot object. This is so that rendering does not show up in the timing functions
def runCSV (k, CSVString):

    #Define blank lists, color list for plotting
    dataset = []
    clusters = []
    colors = ['b.', 'g.', 'r.', 'y.', 'm.']

    # Split by line
    CSVArray = CSVString.splitlines()

    # Split by comma
    for i in range(1, len(CSVArray)-1):
        substr = CSVArray[i]
        temp = []
        temp = list(map(lambda x : float(x), substr.split(',')[:]))
        
        for i in range (0, len(temp)-1, 2):
            dataset.append( (temp[i], temp[i+1]) )

    # Random assignment
    x = random.sample(range(0, len(dataset)-1),k)
    for randIndex in x:
        clusters.append( Cluster(dataset[randIndex]))

    # Run core algorithm
    runAlgo(clusters, dataset)

    # Plot points using matplotlib.pyplot's messed up arguments    
    for x in range (0, len(clusters)):
        for point in clusters[x].points:
            plt.plot(point[0], point[1], colors[x])

    # Return plot for graphing
    return plt

#Runs our core k-means algorithm for random numbers in 2-dimensions
#@params
    #k: integer         - the number of clusters
    #numPoints: integer - the number of points to plot
#No output - no plotting required to get an idea of the time used
def runRandTimed (k, numPoints):

    # Define blank lists, color lists for plotting
    dataset = []
    clusters = []
    colors = ['b.', 'g.', 'r.', 'c.', 'y.', 'm.']

    # Generate random data
    for i in range (0, numPoints):
        dataset.append( (randint(0, 200), randint(0, 200)) )

    # Random assignment of points as centers
    x = random.sample(range(0, len(dataset)-1),k)
    for randIndex in x:
        clusters.append( Cluster(dataset[randIndex]))

    # Run core algorithm
    runAlgo(clusters, dataset)

#Runs our K-means algorithm
#@params
    #k: integer         - the number of clusters
    #numPoints: integer - the number of points to plots
    #dim: integer       - the dimensions (length of each tuple)
def runRand (k, numPoints, dim):

    # Define blank lists
    dataset = []
    clusters = []
    
    #If working in 2 dimensional space
    if (dim == 2):
        # Assign colors with point modifier
        colors = ['b.', 'g.', 'r.', 'c.', 'y.', 'm.']
        for i in range (0, numPoints):
            dataset.append( (randint(0, 200), randint(0, 200)) )

        # Random assignment of points to centers
        x = random.sample(range(0, len(dataset)-1),k)
        for randIndex in x:
            clusters.append( Cluster(dataset[randIndex]))
        # Run core algorithm
        runAlgo(clusters, dataset)

        # Plot points    
        for x in range (0, len(clusters)):
            for point in clusters[x].points:
                plt.plot(point[0], point[1], colors[x])

        # Return plot for GUI
        return plt

    #If working in 3 dimensional space                
    elif (dim == 3):
        # Assign colors without point modifier
        colors = ['b','g','r','c','y','m']

        # Randomly generate points
        for i in range (0, numPoints):
            dataset.append( (randint(0, 200), randint(0, 200), randint(0, 200)) )

        # Random assignment of points as cluster centers
        x = random.sample(range(0, len(dataset)-1),k)
        for randIndex in x:
            clusters.append( Cluster(dataset[randIndex]))

        # Run core algorithm    
        runAlgo(clusters, dataset)

        # Plot in 3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for x in range (0, len(clusters)):
            for point in clusters[x].points:
                ax.scatter(point[0], point[1], point[2], c=colors[x])

        # Return the plot for GUI
        return plt

#Runs the core loop of assignment, recentering untill convergence occurs
def runAlgo(clusters, dataset):
    converged = False

    while  not converged:
        converged = assignToCluster(clusters, dataset)
        if (not converged):
            shiftMeans(clusters)

#If running this file alone, then it will have a text-based interface

if __name__ == "__main__":
    k = int(input("Enter the # of means"))
    numPoints = int(input("Enter the # of data points"))
    dim = int(input("enter 2 for 2d, 3 for 3d"))

    start = timeit.default_timer()
    plt = runRand (k, numPoints, dim)
    stop = timeit.default_timer()
    print("operation took ", (stop - start), "seconds")
    plt.show()
