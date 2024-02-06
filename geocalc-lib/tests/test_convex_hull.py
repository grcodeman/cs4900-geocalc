
import pytest
from convex_hull import Convex_Hull


class TestConvexHull(pytest.TestCase):
    @pytest.fixture
    def ch(self):
        return Convex_Hull()

    def test_points_forming_a_square(self, ch):
        points = [(0, 0), (1, 0), (1, 1), (0, 1)]
        expected_result = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]
        assert ch.graham_scan(points) == expected_result

    def test_points_forming_a_rectangle(self, ch):
        points = [(0, 0), (2, 0), (2, 1), (0, 1)]
        expected_result = [(0, 0), (2, 0), (2, 1), (0, 1), (0, 0)]
        assert ch.graham_scan(points) == expected_result

    def test_points_forming_a_triangle(self, ch):
        points = [(0, 0), (1, 0), (0.5, 1)]
        expected_result = [(0, 0), (1, 0), (0.5, 1), (0, 0)]
        assert ch.graham_scan(points) == expected_result

    def test_points_forming_a_line(self, ch):
        points = [(0, 0), (1, 1), (2, 2), (3, 3)]
        expected_result = [(0, 0), (3, 3), (0, 0)]
        assert ch.graham_scan(points) == expected_result

    def test_points_forming_a_circle(self, ch):
        points = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        expected_result = [(0, -1), (1, 0), (0, 1), (-1, 0), (0, -1)]
        assert ch.graham_scan(points) == expected_result

    def test_points_in_random_order(self, ch):
        points = [(0, 2), (1, 3), (3, 1), (2, 0), (4, 4), (0, 0)]
        expected_result = [(0, 0), (4, 4), (0, 2), (1, 3), (3, 1), (0, 0)]
        assert ch.graham_scan(points) == expected_result

    def test_points_in_descending_order(self, ch):
        points = [(4, 4), (3, 3), (2, 2), (1, 1), (0, 0)]
        expected_result = [(0, 0), (4, 4), (0, 0)]
        assert ch.graham_scan(points) == expected_result

    def test_basic_points(self, ch):
        points = [(0, 0), (1, 1), (1, 0), (0, 1)]
        expected_result = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]
        assert ch.graham_scan(points) == expected_result

    def test_points_with_collinear(self, ch):
        points = [(0, 0), (1, 1), (2, 2), (3, 3)]
        expected_result = [(0, 0), (1, 1), (3, 3), (0, 0)]
        assert ch.graham_scan(points) == expected_result

    def test_point_forming_concave_shape(self, ch):
        points = [(0, 0), (1, 1), (2, 0), (1, 2), (0, 1)]
        expected_result = [(0, 0), (2, 0), (1, 2), (0, 1), (0, 0)]
        assert ch.graham_scan(points) == expected_result

    def test_points_with_duplicates(self, ch):
        points = [(0, 0), (1, 1), (1, 1), (2, 2), (3, 3)]
        expected_result = [(0, 0), (1, 1), (3, 3), (0, 0)]
        assert ch.graham_scan(points) == expected_result

    def test_points_less_than_3_points(self, ch):
        points = [(0, 0), (1, 1)]
        expected_result = "Not possible for Convex Hull with less than 3 points."
        assert ch.graham_scan(points) == expected_result
