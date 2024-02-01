class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __lt__(self, other): #Less than method, for sorting
        return (self.coords[0], self.coords[1]) < (other.coords[0], other.coords[1])