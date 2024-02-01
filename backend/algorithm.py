import numpy as np
from point import Point

class Algorithms:
    def __init__(self):
        # Initialize an empty array for storing points
        self.points = np.array([], dtype=Point)

    def add_point(self, point):
        # Append a new point
        self.points = np.append(self.points, point)

    def remove_point(self, point):
        # Remove a point 
        self.points = self.points[self.points != point]

    def clear_points(self):
        # Clear all points
        self.points = np.array([], dtype=Point)
