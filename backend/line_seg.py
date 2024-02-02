from algorithm import Algorithms
from point import Point
import numpy as np
class LineSegmentIntersection(Algorithms):
    def __init__(self):
        super().__init__()

    def on_segment(self, p, q, r): # for given p,q,r, check that q between both p and r for both the horizontal and vertical axis
        # Check if q is horizontally between p and r (inclusive)
        horizontal = ((p.coords[0] <= q.coords[0] <= r.coords[0]) or
        (r.coords[0] <= q.coords[0] <= p.coords[0]))
        # Check if q is vertically between p and r (inclusive)
        vertical = ((p.coords[1] <= q.coords[1] <= r.coords[1]) or 
        (r.coords[1] <= q.coords[1] <= p.coords[1]))
        #if q both horizontally and vertically in range, return
        return horizontal and vertical


    def orientation(self, p, q, r): # to find the orientation of an ordered triplet (p,q,r) 
        # function returns the following values: 
        # If val > 0 -> clockwise (returns 1).
        # If val < 0 -> counterclockwise (returns 2).
        # If val is zero -> collinear (returns 0).
        val = np.cross(q.coords - p.coords, r.coords - q.coords)
        return 1 if (val > 0) else (2 if val < 0 else 0)


    def do_intersect(self, p1, q1, p2, q2): #This method will indicate if p1q1 and p2q2 intersect
        #using the orientation method, compute all different orientation combinations
        o1 = self.orientation(p1, q1, p2)
        o2 = self.orientation(p1, q1, q2)
        o3 = self.orientation(p2, q2, p1)
        o4 = self.orientation(p2, q2, q1)

        # Check the general case (p1q1p2 differ from p1q1q2 AND p2q2p1 differ from p2q2q1)
        if ((o1 != o2) and (o3 != o4)): 
            return True
        # Check the special cases 
        # if the orientation method return collinear x lies on segement pq..
        if ((o1 == 0) and self.on_segment(p1, p2, q1)): 
            return True    
        if ((o2 == 0) and self.on_segment(p1, q2, q1)): 
            return True
        if ((o3 == 0) and self.on_segment(p2, p1, q2)): 
            return True    
        if ((o4 == 0) and self.on_segment(p2, q1, q2)): 
            return True
    
        # Otherwise ret false
        return False

# Usage Example:
lsi = LineSegmentIntersection()
lsi.add_point(Point(1, 1))
lsi.add_point(Point(10, 10))
lsi.add_point(Point(1, 10))
lsi.add_point(Point(10, 1))

segment1 = (lsi.points[0], lsi.points[1])
segment2 = (lsi.points[2], lsi.points[3])

if lsi.do_intersect(*segment1, *segment2):
    print("Segments intersect")
else:
    print("Segments do not intersect")


# This solution is inspired by Geeksforgeeks solution : 
# https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/