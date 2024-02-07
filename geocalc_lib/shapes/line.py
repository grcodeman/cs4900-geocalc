# Personal imports.
from point import Point


class Line:
    """
    A class to represent a line in 2D space.

    Attributes
    ----------
    start : Point
        The start point of the line.
    end : Point
        The end point of the line.
    """

    def __init__(self, start: Point, end: Point) -> None:
        if start == end:
            raise ValueError("Start and end points cannot be the same")
        self._start = start
        self._end = end

    @property
    def start(self) -> Point:
        return self._start

    @property
    def end(self) -> Point:
        return self._end

    def length(self) -> float:
        """Returns the length of the line."""

        return self.start.distance_to(self.end)

    def midpoint(self) -> Point:
        """Returns the midpoint of the line."""

        return Point((self.start.x + self.end.x) / 2, (self.start.y + self.end.y) / 2)

    def slope(self) -> float:
        """Returns the slope of the line."""
        try:
            return (self.end.y - self.start.y) / (self.end.x - self.start.x)
        except ZeroDivisionError:
            return float('inf')  # Infinite slope for vertical lines

    def is_parallel_to(self, other: 'Line') -> bool:
        """Checks if this line is parallel to another line."""

        return self.slope() == other.slope()

    def __str__(self) -> str:
        return f"Line(start={self.start}, end={self.end})"

    def __eq__(self, other: 'Line') -> bool:
        return self.start == other.start and self.end == other.end

    def __repr__(self) -> str:
        return f"Line(start={self.start!r}, end={self.end!r})"
