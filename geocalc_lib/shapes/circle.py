# Standard library imports.
from __future__ import annotations
from math import pi

# Personal imports.
from point import Point


class Circle:
    """
    A class to represent a circle in 2D space.

    Attributes
    ----------
    center : Point
        The center of the circle.
    radius : float
        The radius of the circle, must be non-negative.
    """

    def __init__(self, center: Point, radius: float) -> None:
        if radius < 0:
            raise ValueError("Radius must be non-negative!")
        self._center = center
        self._radius = radius

    @property
    def center(self) -> Point:
        return self._center

    @property
    def radius(self) -> float:
        return self._radius

    def area(self) -> float:
        """Returns the area of the circle."""
        
        return pi * self.radius ** 2

    def circumference(self) -> float:
        """Returns the circumference of the circle."""
        
        return 2 * pi * self.radius

    def contains_point(self, point: Point) -> bool:
        """Checks if a given point lies inside or on the circle."""

        return self.center.distance_to(point) <= self.radius

    def __str__(self) -> str:
        return f"Circle(center={self.center}, radius={self.radius})"

    def __eq__(self, other: Circle) -> bool:
        return self.center == other.center and self.radius == other.radius
