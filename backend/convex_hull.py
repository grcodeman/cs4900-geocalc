from math import atan2
from point import Point
from operator import itemgetter
from algorithm import Algorithms


class Convex_Hull:
    def __init__(self):
        super().__init__()

    def orientation(self, a, b, c):
        # determine the orienatation of the the points
        values = (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])
        if values == 0:
            return 0
        elif values > 0:
            return 1
        else:
            return 2

    def graham_scan(self, points):
        # ensure the user enters at least 3 points
        if len(points) < 3:
            return "Not possible for Convex Hull with less than 3 points."

        # find the pivot point (minimum y-coordinate in the list)
        pivot = min(points, key=itemgetter(1, 0))

        # sorting the poitns
        sorted_points = sorted(points, key=lambda point: (
            atan2(point[1] - pivot[1], point[0] - pivot[0]), point))

        # initialize the convex hull with the pivot & 1st two sorted points
        hull = [pivot]

        # loop over the rest of the points
        for point in sorted_points:
            # ensures to add points to the convex hull in counterclockwise
            while len(hull) >= 2 and self.orientation(hull[-2], hull[-1], point) != 2:
                hull.pop()
            hull.append(point)
        # add the pivot point back to array to come back to starting point & make a loop
        hull.append(pivot)
        return hull