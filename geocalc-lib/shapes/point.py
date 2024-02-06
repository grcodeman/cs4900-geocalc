# Third party imports.
import numpy as np


class Point:
    """
    A class to represent a point in 2D space.
    
    Attributes
    ----------
    coords : np.ndarray
        The coordinates of the point in 2D space.
    
    Methods
    -------
    __eq__(other)
        Check if two points are equal.
        
    __lt__(other)
        Check if the current point is less than another point.

    __str__
        Convert Point object to string

    __repr__
        Show the string instead of address memory
    """

    def __init__(self, x: int, y: int) -> None:
        self.coords = np.array([x, y])

    def __eq__(self, other: 'Point') -> bool:
        return np.array_equal(self.coords, other.coords)

    def __lt__(self, other) -> bool:
        return (self.coords[0], self.coords[1]) < (other.coords[0],
                                                   other.coords[1])

    def __str__(self) -> str:
        return f"Point({self.coords[0]}, {self.coords[1]})"

    def __repr__(self) -> str:
        return self.__str__()
