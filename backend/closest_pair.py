import math
import numpy as np

from algorithm import Algorithms
from point import Point


class ClosestPairOfPoints(Algorithms):
    def __init__(self):
        super().__init__()
    #Given two points, calculate the euclidean distance, using linalg.norm
    def dist(self, p1, p2):
        return np.linalg.norm(p1.coords - p2.coords)


    def bruteForce(self, points): #This method will return the smallest distance between pairs among all points we have
        min_dist = float("inf")
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                #Euclidean distance between points i and j
                dist_ij = self.dist(points[i], points[j])
                
                # If the calculated distance is smaller than min variable, update it
                if dist_ij < min_dist:
                    min_dist = dist_ij
        return min_dist

    def stripClosest(self, strip, d): #Given a list of points, find if the min distance is among this list
        min_dist = d
        size = len(strip) #number of points in the strip
        strip.sort(key=lambda point: point.coords[1]) #Sort the list according to the y-axis

        for i in range(size):
            for j in range(i+1, size):
                # If the y-axis between i and j >= to the min_dist, increment i and continue
                if (strip[j].coords[1] - strip[i].coords[1]) >= min_dist:
                    break
                #Euclidean distance between points i and j
                dist_ij = self.dist(strip[i], strip[j])

                #if the min distance found, replace the current min with it.
                if dist_ij < min_dist:
                    min_dist = dist_ij
        return min_dist

    def closestUtil(self, points, sort_x=True):
        if sort_x: #Check if sorted already or not
            points = sorted(points, key=lambda point: point.coords[0])

        n = len(points)
        if n <= 3: #If there are few points, do it directly
            return self.bruteForce(points)
        #Otherwise, divid it to two parts and recursivly call each halve
        mid = n // 2
        midPoint = points[mid]
        dl = self.closestUtil(points[:mid], sort_x=False)
        dr = self.closestUtil(points[mid:], sort_x=False)
        #Assign the minimum halve to d
        if dl < dr:
            d = dl
        else:
            d = dr


        # Initialize an empty list for points within the strip
        strip = []
        # Iterate through each point
        for p in points:
            # Check if the point is within distance 'd' of the midpoint on the x-axis
            if abs(p.coords[0] - midPoint.coords[0]) < d: #abs: calculate the absolute value
                strip.append(p)  # Add the point to the strip if it's within the distance

        # Find the closest distance within the strip using strip closest function
        strip_dist = self.stripClosest(strip, d)
        # Check if the closest distance within the strip is less than the minimum distance found so far
        if strip_dist < d:
            return strip_dist  # If yes, return the closest distance within the strip
        else:
            return d  # Otherwise, return the minimum distance found in the divided sections

# Usage Example:
cpp = ClosestPairOfPoints()
cpp.add_point(Point(2, 3))
cpp.add_point(Point(12, 30))
cpp.add_point(Point(40, 50))
cpp.add_point(Point(5, 1))
cpp.add_point(Point(12, 10))
cpp.add_point(Point(3, 4))

print("The smallest distance is", cpp.closestUtil(cpp.points))



#This solution is inspired by Geeksforgeeks solution : 
# https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/#