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
        The radius of the circle.
    """
    
    def __init__(self, center: 'Point', radius: float) -> None:
        self.center = center
        self.radius = radius
