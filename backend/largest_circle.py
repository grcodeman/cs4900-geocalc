import numpy as np
from scipy.spatial import Delaunay


class LargestEmptyCircle:
    def __init__(self, points):
        self.points = np.array(points)
        self.delaunay = Delaunay(points)

    def find_largest_empty_circle(self):
        max_radius = 0
        best_circle = None

        for simplex in self.delaunay.simplices:
            # Calculate the circumcenter and radius of the circumcircle for each simplex (triangle)
            pts = self.points[simplex, :]
            A = np.linalg.det(np.c_[pts, np.ones((3, 1))])
            center = np.linalg.det(np.c_[np.sum(pts*pts, axis=1), pts[:,1], np.ones((3, 1))])
            center = np.array([center, np.linalg.det(np.c_[pts[:,0], np.sum(pts*pts, axis=1),
                                                           np.ones((3, 1))])]) / (2.0 * A)

            radius = np.sqrt(np.sum(np.square(pts[0] - center)))

            # Check if the circle is empty and larger than the current largest
            if radius > max_radius and all(radius < np.linalg.norm(p - center) for p in self.points):
                max_radius = radius
                best_circle = (center, radius)

        return best_circle
