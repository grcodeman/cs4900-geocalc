import pytest
import numpy as np
from point import Point
from ClosestPair import ClosestPairOfPoints

class TestClosestPairOfPoints:
    @pytest.fixture
    def cpp(self):
        return ClosestPairOfPoints()

    def test_distance_calculation_positive_integers(self, cpp):
        p1 = Point(0, 0)
        p2 = Point(3, 4)
        expected_dist = 5
        assert np.allclose(cpp.dist(p1, p2), expected_dist)

    def test_distance_calculation_zero_distance(self, cpp):
        p1 = Point(1, 1)
        expected_dist = 0
        assert np.allclose(cpp.dist(p1, p1), expected_dist)

    def test_distance_calculation_negative_coordinates(self, cpp):
        p1 = Point(-1, -1)
        p2 = Point(1, 1)
        expected_dist = 8 ** 0.5
        assert np.allclose(cpp.dist(p1, p2), expected_dist)

    def test_distance_calculation_floating_points(self, cpp):
        p1 = Point(0.5, 0.5)
        p2 = Point(1.5, 1.5)
        expected_dist = 2 ** 0.5
        assert np.allclose(cpp.dist(p1, p2), expected_dist)

    def test_distance_calculation_close_points(self, cpp):
        p1 = Point(0.0001, 0.0001)
        p2 = Point(0.0002, 0.0002)
        expected_dist = (2 ** 0.5) * 0.0001
        assert np.allclose(cpp.dist(p1, p2), expected_dist)

    def test_distance_calculation_zero_coordinates(self, cpp):
        p1 = Point(0, 10)
        p2 = Point(0, 0)
        expected_dist = 10
        assert np.allclose(cpp.dist(p1, p2), expected_dist)

    def test_distance_calculation_one_point_at_origin(self, cpp):
        p1 = Point(0, 0)
        p2 = Point(10, 10)
        expected_dist = (200) ** 0.5
        assert np.allclose(cpp.dist(p1, p2), expected_dist)

    def test_distance_calculation_diagonal_line(self, cpp):
        p1 = Point(1, 1)
        p2 = Point(2, 2)
        expected_dist = 2 ** 0.5
        assert np.allclose(cpp.dist(p1, p2), expected_dist)

    def test_distance_calculation_symmetry(self, cpp):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        dist_1_to_2 = cpp.dist(p1, p2)
        dist_2_to_1 = cpp.dist(p2, p1)
        assert np.allclose(dist_1_to_2, dist_2_to_1)

    def test_bruteForce_empty_list(self, cpp):
            points = []
            expected_dist = float("inf")
            assert cpp.bruteForce(points) == expected_dist

    def test_bruteForce_single_point(self, cpp):
        p1 = Point(1, 1)
        points = [p1]
        expected_dist = float("inf")
        assert cpp.bruteForce(points) == expected_dist

    def test_bruteForce_two_points(self, cpp):
        p1 = Point(1, 1)
        p2 = Point(3, 4)
        points = [p1, p2]
        expected_dist =  3.605551275463989
        assert cpp.bruteForce(points) == expected_dist

    def test_bruteForce_three_points(self, cpp):
        p1 = Point(1, 1)
        p2 = Point(3, 4)
        p3 = Point(5, 6)
        points = [p1, p2, p3]
        expected_dist = 2.8284271247461903
        assert cpp.bruteForce(points) == expected_dist

    def test_bruteForce_duplicate_points(self, cpp):
        p1 = Point(1, 1)
        p2 = Point(3, 4)
        p3 = Point(3, 4)
        points = [p1, p2, p3]
        expected_dist = 0
        assert cpp.bruteForce(points) == expected_dist

    def test_bruteForce_negative_coordinates(self, cpp):
        p1 = Point(-1, -1)
        p2 = Point(1, 1)
        p3 = Point(2, 2)
        points = [p1, p2, p3]
        expected_dist = 2 ** 0.5
        assert cpp.bruteForce(points) == expected_dist

    # Used some arbitrary value for d...
    def test_stripClosest_empty_strip(self, cpp):
        strip = []
        d = 5  
        assert cpp.stripClosest(strip, d) == d

    def test_stripClosest_two_points(self, cpp):
        p1 = Point(1, 1)
        p2 = Point(2, 2)
        strip = [p1, p2]
        expected_dist = np.linalg.norm(p1.coords - p2.coords)  # Calculate the known distance
        assert cpp.stripClosest(strip, float("inf")) == expected_dist

    def test_stripClosest_multiple_points(self, cpp):
        p1 = Point(1, 1)
        p2 = Point(2, 2)
        p3 = Point(3, 3)
        p4 = Point(4, 4)
        strip = [p1, p2, p3, p4]
        # Calculate the minimum distance among these points
        expected_dist = min(
            np.linalg.norm(p1.coords - p2.coords),
            np.linalg.norm(p1.coords - p3.coords),
            np.linalg.norm(p1.coords - p4.coords),
            np.linalg.norm(p2.coords - p3.coords),
            np.linalg.norm(p2.coords - p4.coords),
            np.linalg.norm(p3.coords - p4.coords)
        )
        assert cpp.stripClosest(strip, float("inf")) == expected_dist

    def test_stripClosest_negative_coordinates(self, cpp):
        p1 = Point(-1, -2)
        p2 = Point(0, 0)
        p3 = Point(1, 2)
        strip = [p1, p2, p3]
        d = float("inf")
        # Calculate the min distance
        expected_dist = min(
            np.linalg.norm(p1.coords - p2.coords),
            np.linalg.norm(p1.coords - p3.coords),
            np.linalg.norm(p2.coords - p3.coords)
        )
        assert cpp.stripClosest(strip, d) == expected_dist

    def test_stripClosest_floating_point_coordinates(self, cpp):
        p1 = Point(0.5, 0.5)
        p2 = Point(1.5, 1.5)
        p3 = Point(2.5, 2.5)
        strip = [p1, p2, p3]
        d = float("inf")
        # Calculate min distance
        expected_dist = min(
            np.linalg.norm(p1.coords - p2.coords),
            np.linalg.norm(p1.coords - p3.coords),
            np.linalg.norm(p2.coords - p3.coords)
        )
        assert cpp.stripClosest(strip, d) == expected_dist

    def test_stripClosest_large_strip(self, cpp):
        strip = [Point(i, i) for i in range(1, 1001)]
        d = 1.4142135623730951
        assert cpp.stripClosest(strip, float("inf")) == d

    def test_closestUtil_basic_few_points(self, cpp): #This will test triggering brute force method
        points = [Point(0, 0), Point(3, 4)]
        expected_dist = 5
        result = cpp.closestUtil(points)
        assert result == expected_dist

    def test_closestUtil_integer_coordinates(self, cpp): # This test handling integer points.
        points = [Point(1, 1), Point(1, 2), Point(2, 1), Point(2, 2)]
        expected_dist = 1
        result = cpp.closestUtil(points)
        assert result == expected_dist

    def test_closestUtil_floating_point_coordinates(self, cpp): # This test handling float points.
        points = [Point(0.5, 0.5), Point(1.5, 1.5), Point(2.5, 2.5)]
        expected_dist = (2 ** 0.5)
        result = cpp.closestUtil(points)
        assert result == expected_dist

    def test_closestUtil_points_along_a_line(self, cpp): # This test the points that are aligned in x and y axises.
        points = [Point(0, 0), Point(0, 1), Point(0, 2), Point(0, 3)]
        expected_dist = 1
        result = cpp.closestUtil(points)
        assert result == expected_dist

    def test_closestUtil_duplicate_coordinates(self, cpp): # This test check duplicates points
        points = [Point(1, 1), Point(1, 1), Point(2, 2)]
        expected_dist = 0
        result = cpp.closestUtil(points)
        assert result == expected_dist

    def test_closestUtil_empty_list(self, cpp): # Handle an empty list of points
        points = []
        expected_dist = float('inf')
        result = cpp.closestUtil(points)
        assert result == expected_dist

    def test_closestUtil_single_point(self, cpp): # Handle 1 point
        points = [Point(1, 1)]
        expected_dist = float('inf')
        result = cpp.closestUtil(points)
        assert result == expected_dist

    def test_closestUtil_negative_coordinates(self, cpp): # this test handle negative points
        points = [Point(-1, -1), Point(-2, -2)]
        expected_dist = 2 ** 0.5
        result = cpp.closestUtil(points)
        assert result == expected_dist

    def test_closestUtil_crossing_midpoint(self, cpp): # This test when the closest pair near mid from right and left
        points = [Point(-2, 0), Point(-1, 0), Point(1, 0), Point(2, 0)]
        expected_dist = 1.0
        result = cpp.closestUtil(points)
        assert result == expected_dist

