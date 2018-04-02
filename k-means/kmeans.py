import numpy as np
import matplotlib.pyplot as plt
import math
import copy
from random import randint
from operator import add
from mpl_toolkits.mplot3d import Axes3D


class Cluster:
    def __init__( self, mean ):
        self.mean = mean
        self.points = []
        self.prevPoints = []
    def addPoints (self, point):
        self.points.append(point)
    def backup(self):
        self.prevPoints = self.points
        self.points = []
    def checkChanged(self):
        return set(self.prevPoints) == set(self.points)

def assignToCluster(clusters, dataset):
    converged = True
    
    for point in dataset:
        minDist = euclDistGeneral(point, clusters[0].mean)
        minCluster = None 

        for cluster in clusters:
            if euclDistGeneral(point, cluster.mean) <= minDist:
                minDist = euclDistGeneral(point, cluster.mean);
                minCluster = cluster
        minCluster.addPoints(point)

        
    for cluster in clusters:

        changeOccured = cluster.checkChanged()

        if (changeOccured):
            converged = False
        
    return converged

def shiftMeans(clusters):
    
    for cluster in clusters:
        average = (0, 0)
        for point in cluster.points:
            average = tuple(map(add, point, average))
        average = tuple(map(lambda x : x/len(cluster.points), average))
            

def euclDist2d(pointA, pointB):
    return math.sqrt( (pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2)

def euclDist3d (pointA, pointB):
    return math.sqrt( (pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2 + (pointA[2] - pointB[2])**2)

def euclDistGeneral (pointA, pointB):
    sum = 0
    for i in range (0, len(pointA)):
        sum += (pointA[i] - pointB[i])**2
    return math.sqrt(sum)

def runCSV (k, CSVString, dim):
    dataset = []
    clusters = []
    colors = ['b.', 'g.', 'r.', 'y.', 'm.']

    
    CSVArray = CSVString.splitlines()
    for i in range(1, len(CSVArray)-1):
        substr = CSVArray[i]
        temp = []
        temp = list(map(lambda x : float(x), substr.split(',')[:]))
        
        for i in range (0, len(temp)-1, 2):
            dataset.append( (temp[i], temp[i+1]) )

    # Random assignment
    for i in range (0, k):
        clusters.append( Cluster(dataset[randint(0, len(dataset) - 1)]) )

    runAlgo(clusters, dataset)
        
    for x in range (0, len(clusters)):
        for point in clusters[x].points:
            plt.plot(point[0], point[1], colors[x])

    return plt
    plt.show()

def runRand (k, numPoints, dim):

    dataset = []
    clusters = []
    colors = ['b.', 'g.', 'r.', 'c.', 'y.', 'm.']

    if (dim == 2):
        for i in range (0, numPoints):
            dataset.append( (randint(0, 200), randint(0, 200)) )

        # Random assignment
        for i in range (0, k):
            clusters.append( Cluster(dataset[randint(0, len(dataset) - 1)]) )

        runAlgo(clusters, dataset)
            
        for x in range (0, len(clusters)):
            for point in clusters[x].points:
                plt.plot(point[0], point[1], colors[x])
                

        return plt
        plt.show()
                    
    elif (dim == 3):
        for i in range (0, numPoints):
            dataset.append( (randint(0, 200), randint(0, 200), randint(0, 200)) )
        print(dataset)

        # Random assignment
        for i in range (0, k):
            clusters.append( Cluster(dataset[randint(0, len(dataset) - 1)]) )
        print(len(clusters))

        runAlgo(clusters, dataset)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        for x in range (0, len(clusters)):
            for point in clusters[x].points:
                ax.scatter(point[0], point[1], point[2], colors[x])

        return plt

def runAlgo(clusters, dataset):
    converged = False

    while  not converged:
        converged = assignToCluster(clusters, dataset)
        shiftMeans(clusters)

    
if __name__ == "__main__":
    k = int(input("Enter the # of means"))
    numPoints = int(input("Enter the # of data points"))
    dim = int(input("enter 2 for 2d, 3 for 3d"))

    plt = runRand (k, numPoints, dim)
    plt.show()
