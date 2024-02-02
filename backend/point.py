import numpy as np

class Point:
    def __init__(self, x, y):
        self.coords = np.array([x, y])

    def __eq__(self, other):
        return np.array_equal(self.coords, other.coords)

    def __lt__(self, other): #Less than method, for sorting
        return (self.coords[0], self.coords[1]) < (other.coords[0], other.coords[1])