# This solution is inspired by Geeksforgeeks solution :
# https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/#

from geocalc_lib.shapes.point import Point

# Thirty party imports.
import numpy as np


class ClosestPairOfPoints:
    """
    A class to represent the closest pair of points algorithm.

    Attributes
    ----------
    points : np.array
        An array of points.

    Methods
    -------
    dist(p1, p2)
        Given two points, calculate the euclidean distance, using
        linalg.norm.
    brute_force(points)
        This method will return the smallest distance between pairs
        among all points we have.
    strip_closest(strip, d)
        Given a list of points, find if the min distance is among this
        list.
    closest_util(points, sort_x=True)
        Given a list of points, find if the min distance is among this
        list.

    Usage
    -----
    import numpy as np
    from geocalc-lib import ClosestPairOfPoints

    # Example points.
    points = np.array([[1, 2], [3, 4], [1, 3], [2, 5], [6, 1]])

    # Initialize the class with the points.
    closest_pair_finder = ClosestPairOfPoints(points)

    # Find the closest pair of points.
    min_distance = closest_pair_finder.closest_util(points)
    """

    def __init__(self, points: np.array) -> None:
        self.points = points

    def dist(self, p1, p2) -> float:
        """
        Given two points, calculate the euclidean distance, using
        linalg.norm.
        """
        
        return np.linalg.norm(p1.coords - p2.coords)

    def brute_force(self, points) -> float:
        """
        Return the smallest distance between pairs among all points
        that we have.
        """

        min_dist = float("inf")
        n = len(points)
        min_pair = None
        for i in range(n):
            for j in range(i+1, n):
                dist_ij = self.dist(points[i], points[j])
                if dist_ij < min_dist:
                    min_dist = dist_ij
                    min_pair = (points[i],points[j])
        return min_dist, min_pair

    def strip_closest(self, strip, d, best_pair) -> float:
        """
        Given a list of points, find if the min distance is among this
        list.
        """

        min_dist = d
        min_pair = best_pair
        # Number of points in the strip.
        size = len(strip)
        # Sort the list according to the y-axis.
        strip.sort(key=lambda point: point.coords[1])

        for i in range(size):
            for j in range(i+1, size):
                # If the y-axis between i and j >= to the min_dist,
                # increment i and continue.
                if (strip[j].coords[1] - strip[i].coords[1]) >= min_dist:
                    break
                # Euclidean distance between points i and j
                dist_ij = self.dist(strip[i], strip[j])

                # if the min distance found, replace the current min
                # with it.
                if dist_ij < min_dist:
                    min_dist = dist_ij
                    min_pair = (strip[i], strip[j])

        return min_dist, min_pair

    def closest_util(self, points, sort_x=True) -> float:
        """
        Given a list of points, find if the min distance is among this
        list.
        """

        # Check if sorted already or not.
        if sort_x:  
            points = sorted(points, key=lambda point: point.coords[0])

        n = len(points)
        # If there are few points, do it directly.
        if n <= 3:
            return self.brute_force(points)
        
        # Otherwise, divide it to two parts and recursivly call each
        # halve.
        mid = n // 2
        midPoint = points[mid]
        dl, pair_left = self.closest_util(points[:mid], sort_x=False)
        dr, pair_right = self.closest_util(points[mid:], sort_x=False)

        # Assign the minimum halve to d.
        if dl < dr:
            d = dl
            best_pair = pair_left
        else:
            d = dr
            best_pair = pair_right
        # Initialize an empty list for points within the strip.
        strip = []
        # Iterate through each point.
        for p in points:
            # Check if the point is within distance 'd' of the midpoint
            # on the x-axis.
            if abs(p.coords[0] - midPoint.coords[0]) < d:
                # Add the point to the strip if it's within the
                # distance.
                strip.append(p)

        # Find the closest distance within the strip using strip
        # closest function.
        strip_dist, strip_pair = self.strip_closest(strip, d, best_pair)
        # Check if the closest distance within the strip is less than
        # the minimum distance found so far.
        if strip_dist < d:
            # If yes, return the closest distance within the strip.
            return strip_dist, strip_pair
        else:
            # Otherwise, return the minimum distance found in the
            # divided sections.
            return d, best_pair  