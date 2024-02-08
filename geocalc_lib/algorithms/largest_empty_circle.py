# Standard library imports.
import unittest

# Third-party imports.
import numpy as np
from scipy.spatial import Delaunay


class LargestEmptyCircle:
    """
    A class to represent the largest empty circle algorithm.

    Attributes
    ----------
    points : np.array
        An array of points.
    delaunay : scipy.spatial.Delaunay
        A Delaunay triangulation of the points.

    Methods
    -------
    find_largest_empty_circle()
        This method will return the center and radius of the largest
        empty circle.

    Usage
    -----
    import numpy as np
    from geocalc-lib import LargestEmptyCircle

    # Example points.
    points = np.array([[1, 2], [3, 4], [1, 3], [2, 5], [6, 1]])

    # Initialize the class with the points.
    lec = LargestEmptyCircle(points)

    # Find the largest empty circle.
    center, radius = lec.find_largest_empty_circle()
    """

    def __init__(self, points) -> None:
        self.points = np.array(points)
        self.delaunay = Delaunay(points)

    def find_largest_empty_circle(self) -> tuple:
        max_radius = 0
        best_circle = None

        for simplex in self.delaunay.simplices:
            # Calculate the circumcenter and radius of the circumcircle
            # for each simplex (triangle).
            pts = self.points[simplex, :]
            A = np.linalg.det(np.c_[pts, np.ones((3, 1))])
            center = np.linalg.det(np.c_[np.sum(pts*pts, axis=1),
                                   pts[:, 1],
                                   np.ones((3, 1))])
            center = np.array([center,
                               np.linalg.det(np.c_[pts[:, 0],
                                             np.sum(pts*pts, axis=1),
                                             np.ones((3, 1))])]) / (2.0 * A)

            radius = np.sqrt(np.sum(np.square(pts[0] - center)))

            # Check if the circle is empty and larger than the current
            # largest. Exclude simplex vertices from the check.
            simplex_points = set(tuple(point) for point in pts)
            other_points = []
            for p in self.points:
                if tuple(p) not in simplex_points:
                    other_points.append(p)

            if radius > max_radius:
                if all(np.linalg.norm(p - center) > radius for p in other_points):
                    max_radius = radius
                best_circle = (center, radius)

        return best_circle


class TestLargestEmptyCircle(unittest.TestCase):
    def test_largest_empty_circle(self) -> None:
        points = np.array([
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1]
        ])

        # Instantiate the LargestEmptyCircle class with the points.
        lec = LargestEmptyCircle(points)

        # Find the largest empty circle.
        center, radius = lec.find_largest_empty_circle()

        # Expected center and radius for the largest empty circle in
        # the square.
        expected_center = np.array([0.5, 0.5])
        expected_radius = np.sqrt(2) / 2

        # Check if the found center and radius are close to the
        # expected values.
        fail_message = "The center of the largest empty circle is incorrect."
        self.assertTrue(np.allclose(center, expected_center), fail_message)
        radius_fail_message = ("The radius of the largest empty circle is "
                               + "incorrect.")
        self.assertAlmostEqual(radius, expected_radius, places=5,
                               msg=radius_fail_message)
