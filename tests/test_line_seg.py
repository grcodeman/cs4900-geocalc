import pytest
from point import Point
from line_seg import LineSegmentIntersection

class TestLineSegmentIntersection:
    @pytest.fixture
    def lsi(self):
        return LineSegmentIntersection()
    def test_on_segment_true(self, lsi):
        p = Point(0, 0)
        q = Point(1, 1)
        r = Point(2, 2)
        assert lsi.on_segment(p, q, r) == True

    def test_on_segment_false(self, lsi):
        p = Point(0, 0)
        q = Point(8, 8)
        r = Point(5, 5)
        assert lsi.on_segment(p, q, r) == False
    
    def test_on_segment_horizontal(self, lsi):
        p = Point(3,3)
        q = Point(7,5)
        r = Point(6,6)
        assert lsi.on_segment(p,q,r) == False

    def test_on_segment_vertical(self, lsi):
        p = Point(3,3)
        q = Point(5,7)
        r = Point(6,6)
        assert lsi.on_segment(p,q,r) == False

    def test_on_segment_negative(self, lsi):
        p = Point(3,-5)
        q = Point(5,-3)
        r = Point(6,6)
        assert lsi.on_segment(p,q,r) == True

    def test_orientation_collinear(self, lsi):
        p = Point(0, 0)
        q = Point(1, 1)
        r = Point(2, 2)
        assert lsi.orientation(p, q, r) == 0

    def test_orientation_clockwise(self, lsi):
        p = Point(0, 0)
        q = Point(2, 0)
        r = Point(1, 1)
        assert lsi.orientation(p, q, r) == 1

    def test_orientation_counterclockwise(self, lsi):
        p = Point(0, 0)
        q = Point(1, 1)
        r = Point(2, 0)
        assert lsi.orientation(p, q, r) == 2

    def test_orientation_clockwise_negative(self, lsi):
        p = Point(-1, -1)
        q = Point(-2, -1)
        r = Point(-2, -2)
        assert lsi.orientation(p, q, r) == 1

    def test_orientation_counterclockwise_negative(self, lsi):
        p = Point(-1, -1)
        q = Point(-2, -2)
        r = Point(-2, -1)
        assert lsi.orientation(p, q, r) == 2

    def test_orientation_horizontal(self, lsi):
        p = Point(1, 1)
        q = Point(3, 1)
        r = Point(5, 1)
        assert lsi.orientation(p, q, r) == 0

    def test_orientation_vertical(self, lsi):
        p = Point(1, 1)
        q = Point(1, 2)
        r = Point(1, 3)
        assert lsi.orientation(p, q, r) == 0

    def test_orientation_diagonal(self, lsi):
        p = Point(1, 1)
        q = Point(2, 2)
        r = Point(3, 3)
        assert lsi.orientation(p, q, r) == 0

    def test_orientation_negative_diagonal(self, lsi):
        p = Point(-1, -1)
        q = Point(-2, -2)
        r = Point(-3, -3)
        assert lsi.orientation(p, q, r) == 0

    def test_do_intersect_true(self, lsi):
        p1 = Point(1, 1)
        q1 = Point(10, 10)
        p2 = Point(1, 10)
        q2 = Point(10, 1)
        assert lsi.do_intersect(p1, q1, p2, q2) is True

    def test_do_intersect_false(self, lsi):
        p1 = Point(1, 1)
        q1 = Point(4, 1)
        p2 = Point(2, 2)
        q2 = Point(4, 2)
        assert lsi.do_intersect(p1, q1, p2, q2) == False

    def test_do_intersect_non_intersecting_segments(self, lsi):
        p1 = Point(0, 0)
        q1 = Point(1, 0)
        p2 = Point(2, 1)
        q2 = Point(3, 1)
        assert lsi.do_intersect(p1, q1, p2, q2) is False

    def test_do_intersect_intersecting_segments(self, lsi):
        p1 = Point(0, 0)
        q1 = Point(2, 2)
        p2 = Point(1, 1)
        q2 = Point(3, 1)
        assert lsi.do_intersect(p1, q1, p2, q2) is True

    def test_do_intersect_collinear_segments(self, lsi):
        p1 = Point(0, 0)
        q1 = Point(2, 2)
        p2 = Point(3, 3)
        q2 = Point(4, 4)
        assert lsi.do_intersect(p1, q1, p2, q2) is False

    def test_do_intersect_one_inside_another(self, lsi):
        p1 = Point(0, 0)
        q1 = Point(4, 4)
        p2 = Point(1, 1)
        q2 = Point(3, 3)
        assert lsi.do_intersect(p1, q1, p2, q2) is True

    def test_do_intersect_one_overlapping_another(self, lsi):
        p1 = Point(0, 0)
        q1 = Point(3, 3)
        p2 = Point(2, 2)
        q2 = Point(4, 4)
        assert lsi.do_intersect(p1, q1, p2, q2) is True

    def test_do_intersect_vertical_horizontal_segments(self, lsi):
        p1 = Point(0, 0)
        q1 = Point(0, 2)
        p2 = Point(0, 1)
        q2 = Point(0, 3)
        assert lsi.do_intersect(p1, q1, p2, q2) is True

    def test_do_intersect_parallel_non_intersecting(self, lsi):
        p1 = Point(0, 0)
        q1 = Point(2, 0)
        p2 = Point(0, 1)
        q2 = Point(2, 1)
        assert lsi.do_intersect(p1, q1, p2, q2) is False

    def test_do_intersect_parallel_overlapping(self, lsi):
        p1 = Point(0, 0)
        q1 = Point(3, 0)
        p2 = Point(1, 0)
        q2 = Point(4, 0)
        assert lsi.do_intersect(p1, q1, p2, q2) is True

    def test_do_intersect_parallel_collinear(self, lsi):
        p1 = Point(0, 0)
        q1 = Point(4, 0)
        p2 = Point(5, 0)
        q2 = Point(8, 0)
        assert lsi.do_intersect(p1, q1, p2, q2) is False
