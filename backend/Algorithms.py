from point import Point

class Algorithms:
    def __init__(self):
        self.points = []  # List to store points

    def add_point(self, point):
        self.points.append(point)

    def remove_point(self, point):
        self.points.remove(point)

    def clear_points(self):
        self.points.clear()

#Instance:
cg = Algorithms()
cg.add_point(Point(1, 2))
cg.add_point(Point(3, 4))
cg.remove_point(Point(1, 2))
cg.clear_points()
