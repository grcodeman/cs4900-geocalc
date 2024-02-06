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

    def __init__(self, start: 'Point', end: 'Point') -> None:
        self.start = start
        self.end = end
