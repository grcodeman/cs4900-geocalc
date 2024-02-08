# Standard library imports.
from operator import itemgetter
from math import atan2

# Third-party imports.
import numpy as np


class ConvexHull:
    """
    A class to represent the Convex Hull algorithm.

    Attributes
    ----------
    points : np.array
        An array of points.

    Methods
    -------
    orientation(a, b, c)
        Determine the orientation of the the points.
    graham_scan(points)
        This method will return the convex hull of the points.

    Usage
    -----
    import numpy as np
    from geocalc-lib import ConvexHull

    # Example points.
    points = np.array([[1, 2], [3, 4], [1, 3], [2, 5], [6, 1]])

    # Initialize the class with the points.
    convex_hull_finder = ConvexHull(points)

    # Find the convex hull of the points.
    convex_hull = convex_hull_finder.graham_scan(points)
    """

    def __init__(self, points: np.array) -> None:
        self.points = points

    def orientation(self, a, b, c) -> int:
        # Determine the orienatation of the the points.
        values = (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])
        if values == 0:
            return 0
        elif values > 0:
            return 1
        else:
            return 2

    def graham_scan(self, points) -> list:
        # Ensure the user enters at least 3 points.
        if len(points) < 3:
            return "Not possible for Convex Hull with less than 3 points."

        # Find the pivot point (minimum y-coordinate in the list).
        pivot = min(points, key=itemgetter(1, 0))

        # Sort the points.
        sorted_points = sorted(points, key=lambda point: (
            atan2(point[1] - pivot[1], point[0] - pivot[0]), point))

        # Initialize the convex hull with the pivot & 1st two sorted
        # points.
        hull = [pivot]

        # Loop over the rest of the points.
        for point in sorted_points:
            # Ensures to add points to the convex hull in
            # counterclockwise.
            while (len(hull) >= 2 and
                   self.orientation(hull[-2], hull[-1], point) != 2):
                hull.pop()
            hull.append(point)
        # Add the pivot point back to array to come back to starting
        # point & make a loop.
        hull.append(pivot)
        return hull
