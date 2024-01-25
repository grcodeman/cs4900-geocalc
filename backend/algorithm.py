from backend.point import Point


class Algorithm:
    def __init__(self) -> None:
        # Create a list of points.
        self.points = []

    def add_point(self, point) -> None:
        # Create and add a new point object to the list of points.
        self.points.append(Point(point[0], point[1]))

    def remove_point(self, point) -> None:
        # Remove a point object from the list of points.
        point_to_remove = Point(point[0], point[1])
        if point_to_remove in self.points:
            self.points.remove(point_to_remove)

    def clear_points(self) -> None:
        # Clear the list of points.
        self.points.clear()
