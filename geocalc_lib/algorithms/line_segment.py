# This solution is inspired by Geeksforgeeks solution :
# https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/

# Thid-party imports.
import numpy as np


class LineSegmentIntersection:
    """
    A class to represent the line segment intersection algorithm.

    Attributes
    ----------
    points : np.array
        An array of points.

    Methods
    -------
    on_segment(p, q, r)
        Given three points p, q, and r, the function checks if point q
        lies on line segment 'pr'.
    orientation(p, q, r)
        Given three points p, q, and r, the function finds the
        orientation.
    do_intersect(p1, q1, p2, q2)
        Given two line segments p1q1 and p2q2, the function checks if
        they intersect.

    Usage
    -----
    import numpy as np
    from geocalc-lib import LineSegmentIntersection

    # Example points.
    points = np.array([[1, 2], [3, 4], [1, 3], [2, 5], [6, 1]])

    # Initialize the class with the points.
    lsi = LineSegmentIntersection(points)

    # Find the line segment intersection.
    intersect = lsi.do_intersect(points[0], points[1], points[2], points[3])
    """

    def __init__(self, points: np.array) -> None:
        self.points = points

    def on_segment(self, p, q, r) -> bool:
        """
        Given three points p, q, and r, the function checks if point q
        lies on line segment 'pr'
        """

        # Check if q is horizontally between p and r (inclusive)
        horizontal = ((p.coords[0] <= q.coords[0] <= r.coords[0]) or
                      (r.coords[0] <= q.coords[0] <= p.coords[0]))
        # Check if q is vertically between p and r (inclusive)
        vertical = ((p.coords[1] <= q.coords[1] <= r.coords[1]) or
                    (r.coords[1] <= q.coords[1] <= p.coords[1]))
        # if q both horizontally and vertically in range, return
        return horizontal and vertical

    # to find the orientation of an ordered triplet (p,q,r)
    def orientation(self, p, q, r) -> int:
        """
        Given three points p, q, and r, the function finds the
        orientation
        """

        # function returns the following values:
        # If val > 0 -> clockwise (returns 1).
        # If val < 0 -> counterclockwise (returns 2).
        # If val is zero -> collinear (returns 0).
        val = np.cross(q.coords - p.coords, r.coords - q.coords)
        return 1 if (val > 0) else (2 if val < 0 else 0)

    def do_intersect(self, p1, q1, p2, q2):
        """
        Given two line segments p1q1 and p2q2, the function checks if
        they intersect.
        """

        # Using the orientation method, compute all different
        # orientation combinations.
        o1 = self.orientation(p1, q1, p2)
        o2 = self.orientation(p1, q1, q2)
        o3 = self.orientation(p2, q2, p1)
        o4 = self.orientation(p2, q2, q1)

        # Check the general case (p1q1p2 differ from p1q1q2 AND p2q2p1
        # differ from p2q2q1)
        if ((o1 != o2) and (o3 != o4)):
            return True
        # Check the special cases
        # if the orientation method return collinear x lies on
        # segement pq.
        if ((o1 == 0) and self.on_segment(p1, p2, q1)):
            return True
        if ((o2 == 0) and self.on_segment(p1, q2, q1)):
            return True
        if ((o3 == 0) and self.on_segment(p2, p1, q2)):
            return True
        if ((o4 == 0) and self.on_segment(p2, q1, q2)):
            return True

        # Otherwise ret false.
        return False
