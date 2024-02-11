# Standard library imports.
import os
import random
import sys
import numpy as np

# Personal imports.
# If this were to be published, this would simply reference the package
# on PyPI. However, because this is a local package, we need to add the
# path to the system path.

# Get the absolute path of the geocalc-app directory
app_directory = os.path.dirname(os.path.abspath(__file__))

# Get the path of the parent directory of geocalc-app and geocalc-lib
parent_directory = os.path.dirname(app_directory)

# Add the parent directory to sys.path to access geocalc-lib
sys.path.append(parent_directory)

# Now you should be able to import modules from geocalc-lib
from geocalc_lib.shapes.point import Point
from geocalc_lib.shapes.line import Line
from geocalc_lib.algorithms.closest_pair_of_points import ClosestPairOfPoints
from geocalc_lib.algorithms.convex_hull import ConvexHull
from geocalc_lib.algorithms.largest_empty_circle import LargestEmptyCircle
from geocalc_lib.algorithms.line_segment import LineSegmentIntersection


class Console:
    """
    A class to represent a command line ui for geocalc_lib package

    Attributes
    ----------
    prompt : 'geocalc1.0> '
        A string at the beginning of each input.
    points : array
        An array of points.
    lines : array
        An array of lines.

    Methods
    -------
    run()
        This method will run the command line ui,
        asking the user for input commands until
        they enter 'exit' or 'quit'.
    handle_add_point(command)
        This method will add the given point to the points array.
    handle_remove_point(command)
        Removes a given point from the points array.
    handle_clear_points(command)
        Removes all points from the points array.
    handle_add_line(command)
        Adds a given line to the lines array.
    handle_remove_line(command)
        Removes a given line from the lines array.
    handle_remove_lines
        Removes all lines from the lines array.
    handle_closest_pair(command)
        Performs the closest pair of points algorithm
        on the points in the points array.
    handle_convex_hull(command)
        Performs the convex hull algorithm
        on the points in the points array.
    handle_largest_circle(command)
        Performs the largest empty circle algorithm
        on the points in the points array.
    handle_line_segment(command)
        Performs the line segment intersection algorithm
        on each line pair to determine if the intersect.

    Usage
    -----
        import numpy as np

        from geocalc_lib.shapes.point import Point
        from geocalc_lib.shapes.line import Line
        from geocalc_lib.algorithms.closest_pair_of_points import (
            ClosestPairOfPoints)
        from geocalc_lib.algorithms.convex_hull import ConvexHull
        from geocalc_lib.algorithms.largest_empty_circle import (
            LargestEmptyCircle)
        from geocalc_lib.algorithms.line_segment import (
            LineSegmentIntersection)

        # Initialize the class
        console = Console()

        # Run the ui
        console.run()

    Commands
    --------
    add_point x y
        Adds the given point to the points array.
    remove_point x y
        Removes the given point from the points array.
    clear_points
        Removes all points from the points array.
    add_line x1 y1 x2 y2
        Adds the given line to the lines array.
    remove_line x1 y1 x2 y2
        Removes the given line from the lines array.
    clear_lines
        Removes all lines from the lines array.
    closest_pair_of_points
        Performs the closest pair of points algorithm
        on the points in the points array.
    convex_hull
        Performs the convex hull alforithm
        on the points in the points array.
    largest_empty_circle
        Performs the largest empty circle algorithm
        on the points in the points array.
    line_segment
        Performs the line segment intersection algorithm
        for each pair of lines from the lines array.
    """

    def __init__(self) -> None:
        self.prompt = 'geocalc1.0> '
        # Initialize an empty array for storing points and lines.
        self.points = []
        self.lines = []

    def run(self) -> None:
        while True:
            try:
                command = input(self.prompt)
                # Exit commands.
                if command.lower() in ['exit', 'quit']:
                    print("Exiting the console.")
                    break
                elif command.startswith('add_point'):
                    self.handle_add_point(command)
                elif command.startswith('remove_point'):
                    self.handle_remove_point(command)
                elif command.startswith('clear_points'):
                    self.handle_clear_points(command)
                elif command.startswith('add_line'):
                    self.handle_add_line(command)
                elif command.startswith('remove_line'):
                    self.handle_remove_line(command)
                elif command.startswith('clear_lines'):
                    self.handle_clear_lines(command)
                elif command.startswith('closest_pair_of_points'):
                    self.handle_closest_pair(command)
                elif command.startswith('convex_hull'):
                    self.handle_convex_hull(command)
                elif command.startswith("largest_empty_circle"):
                    self.handle_largest_circle(command)
                elif command.startswith("line_segment"):
                    self.handle_line_segment(command)
                elif command.startswith("help"):
                    print("Add a point or line:\n\tadd_point x y |"
                          + " add_line x1 y1 x2 y2\n"
                          + "Remove a point or line:\n\tremove_point x y |"
                          + " remove_line x1 y1 x2 y2\n"
                          + "Clear all points or lines:\n\tclear_points | "
                          + "clear_lines\n"
                          + "Algorithms:\n\tclosest_pair_of_points | convex_hull"
                          + " | largest_empty_circle | line_segment")
                else:
                    # Print user error in yellow.
                    print("\033[93m" + "Unknown command." + "\033[0m")
            except KeyboardInterrupt:
                print("\nExiting the console (interrupted).")
                break
            except EOFError:
                print("\nExiting the console (EOF).")
                break

    def handle_add_point(self, command) -> None:
        try:
            # Assuming the command format is "add_point x y"
            _, x, y = command.split()
            # Convert strings to integers
            # and create a Point class variable.
            point = Point(int(x), int(y))
            # If point is already in points, don't add point
            if point in self.points:
                # Print message in yellow and return
                print("\033[93m" + f"{point} already entered."
                      + "\033[0m")
                return
            # Add the point to the points array.
            self.points.append(point)
            # Print a success message in green.
            print("\033[92m" + f"{point} added." + "\033[0m")
        except ValueError:
            # Print a user error in yellow.
            print("\033[93m" + "Invalid point format. Usage: add_point x y"
                  + "\033[0m")
        except Exception as e:
            # Print an error in red.
            print("\033[91m" + f"Error adding point: {e}" + "\033[0m")

    def handle_remove_point(self, command) -> None:
        try:
            # Assuming the command format is "remove_point x y"
            _, x, y = command.split()
            # Convert strings to integers
            # and create a Point class variable
            point = Point(int(x), int(y))
            try:
                # Find the index of the point in points array.
                index = self.points.index(point)
                # Remove the point from the points array.
                del self.points[index]
                # Print a success message in green.
                print("\033[92m" + f"{point} removed." + "\033[0m")
            except ValueError:
                # Print an error in red.
                print("\033[91m" + f"{point} does not exist."
                      + "\033[0m")
        except ValueError:
            # Print an error in yellow.
            print("\033[93m" + "Invalid point format. Usage: remove_point x y"
                  + "\033[0m")
        except Exception as e:
            # Print an error in red.
            print("\033[91m" + f"Error removing point: {e}" + "\033[0m")

    def handle_clear_points(self, command) -> None:
        try:
            # Assuming the command format is "clear_points"
            _, = command.split()
            # Clear the list of points.
            self.points = []
            # Print a success message in green.
            print("\033[92m" + "Points cleared." + "\033[0m")
        except Exception as e:
            # Print an error in red.
            print("\033[91m" + f"Error clearing points: {e}" + "\033[0m")

    def handle_add_line(self, command) -> None:
        try:
            # Assuming the command format is "add_line x1 y1 x2 y2"
            _, x1, y1, x2, y2 = command.split()
            # Convert string to integers and create a Line class variable
            line = Line(Point(int(x1), int(y1)), Point(int(x2), int(y2)))
            # If line is already in lines, don't add line
            if line in self.lines:
                # Print message in yellow and return
                print("\033[93m" + f"{line} already entered."
                      + "\033[0m")
                return
            # Add the line to lines array
            self.lines.append(line)
            # Print a success message in green.
            print("\033[92m" + f"{line} added." + "\033[0m")
        except ValueError:
            # Print a user error in yellow.
            print("\033[93m" + "Invalid point format. Usage: "
                  + "add_line x1 y1 x2 y2" + "\033[0m")
        except Exception as e:
            # Print an error in red.
            print("\033[91m" + f"Error adding line: {e}" + "\033[0m")

    def handle_remove_line(self, command) -> None:
        try:
            # Assuming the command format is "remove_line x1 y1 x2 y2"
            _, x1, y1, x2, y2 = command.split()
            # Convert string to integers and create a Line class variable
            line = Line(Point(int(x1), int(y1)), Point(int(x2), int(y2)))
            try:
                # Find the index of the line in lines array.
                index = self.lines.index(line)
                # Remove the line from the lines array.
                del self.lines[index]
                # Print a success message in green.
                print("\033[92m" + f"{line} removed." + "\033[0m")
            except ValueError:
                # Print an error in red.
                print("\033[91m" + f"{line} does not exist." + "\033[0m")
        except ValueError:
            # Print an error in yellow.
            print("\033[93m" + "Invalid line format. Usage: "
                  + "remove_line x1 y1 x2 y2" + "\033[0m")
        except Exception as e:
            # Print an error in red.
            print("\033[91m" + f"Error removing line: {e}" + "\033[0m")

    def handle_clear_lines(self, command) -> None:
        try:
            # Assuming the command format is "clear_lines"
            _, = command.split()
            # Clear the list of lines.
            self.lines = []
            # Print a success message in green.
            print("\033[92m" + "Lines cleared." + "\033[0m")
        except Exception as e:
            # Print an error in red.
            print("\033[91m" + f"Error clearing Lines: {e}" + "\033[0m")

    def handle_closest_pair(self, command) -> None:
        # Check if there aren't enough points to run the algorithm.
        if len(self.points) < 2:
            # Display a warning message in red and return
            print("\033[91m" + f"Not enough points."
                  + f" Add points with command 'add_point x y'" + "\033[0m")
            return

        try:
            # Assuming command format is "closest_pair_of_points"
            _, = command.split()
            # Turn points into an np.array
            # and call ClosestPairOfPoints algorithm
            np_points = np.array(self.points)
            closest_pair_finder = ClosestPairOfPoints(np_points)
            min_distance, best_pair = closest_pair_finder.closest_util(
                np_points)
            # Print a success message in green displaying algorithm info
            print("\033[92m" + f"({best_pair[0].coords[0]}, "
                  + f"{best_pair[0].coords[1]}) "
                  + f"and ({best_pair[1].coords[0]}, "
                  + f"{best_pair[1].coords[1]}) "
                  + f"are the closest pair of points with"
                  + f" a distance of {min_distance:.3f}."
                  + "\033[0m")
        except Exception as e:
            # Print an error in red.
            print("\033[91m" + f"Error finding closest pair: {e}" + "\033[0m")

    def handle_convex_hull(self, command) -> None:
        # Check if there aren't enough points to run the algorithm.
        if len(self.points) < 3:
            # Display a warning message in red and return
            print("\033[91m" + f"Not enough points."
                  + f" Add points with command 'add_point x y'" + "\033[0m")
            return

        try:
            # Assuming command format is "convex_hull"
            _, = command.split()
            # Turn points into array of tuples
            points = [(point.coords[0], point.coords[1])
                      for point in self.points]
            # Call ConvexHull algorithm and perform a graham scan
            convex_hull_finder = ConvexHull(points)
            convex_hull = convex_hull_finder.graham_scan(points)
            # Print a success message in green displaying convex hull info
            print("\033[92m" + "Convex Hull Shape:" + "\033[0m")
            for point in convex_hull:
                print("\033[92m" + f"({point[0]}, {point[1]})" + "\033[0m")
        except Exception as e:
            # Print an error in red.
            print("\033[91m" + f"Error finding convex hull: {e}" + "\033[0m")

    def handle_largest_circle(self, command) -> None:
        # Check if there aren't enough points to run the algorithm.
        if len(self.points) < 4:
            # Display a warning message in red and return
            print("\033[91m" + f"Not enough points."
                  + f" Add points with command 'add_point x y'" + "\033[0m")
            return

        try:
            # Assuming command format is "largest_empty_circle"
            _, = command.split()
            # Turn points into np.array of array point values
            np_points = np.array([[point.coords[0], point.coords[1]]
                                 for point in self.points])
            # Call LargestEmptyCircle algorithm
            lec = LargestEmptyCircle(np_points)
            center, radius = lec.find_largest_empty_circle()
            # Print a success message in green
            # displaying algorithm information
            print("\033[92m" + f"Largest empty circle has a"
                  + f" center of {center} and radius of {radius:.3f}."
                  + "\033[0m")
        except Exception as e:
            # Print an error in red.
            print("\033[91m" + f"Error finding largest empty circle: "
                  + f"{e}" + "\033[0m")

    def handle_line_segment(self, command) -> None:
        # Check if there aren't enough lines to run the algorithm.
        if len(self.lines) < 2:
            # Display a warning message in red and return
            print("\033[91m" + f"Not enough lines."
                  + f" Add lines with command 'add_line x1 y1 x2 y2'"
                  + "\033[0m")
            return

        try:
            # Assuming command format is "line_segment"
            _, = command.split()
            # Get each pair of lines
            line_pairs = []
            for i, line1 in enumerate(self.lines):
                for line2 in self.lines[i + 1:]:
                    line_pairs.append([line1, line2])
            # For each pair of lines, call LineSegmentIntersection algorithm
            lsi = LineSegmentIntersection(np.array(self.points))
            results = []
            for pair in line_pairs:
                result = lsi.do_intersect(pair[0].start, pair[0].end,
                                          pair[1].start, pair[1].end)
                results.append(result)
            # Print a success message in green displaying line segment info
            print("\033[92m" + f"Line Segment Intersections:" + "\033[0m")
            # For each line_pair, display whether they intersected or not
            for i in range(len(line_pairs)):
                result = "intersect" if results[i] else "do not intersect"
                print("\033[92m" + f"[({line_pairs[i][0].start.coords[0]}, "
                      + f"{line_pairs[i][0].start.coords[1]}),"
                      + f" ({line_pairs[i][0].end.coords[0]},"
                      + f" {line_pairs[i][0].end.coords[1]})]"
                      + f" and [({line_pairs[i][1].start.coords[0]},"
                      + f" {line_pairs[i][1].start.coords[1]}),"
                      + f" ({line_pairs[i][1].end.coords[0]},"
                      + f" {line_pairs[i][1].end.coords[1]})] {result}."
                      + "\033[0m")
        except Exception as e:
            # Print an error in red.
            print("\033[91m" + f"Error finding line segment intersection: {e}"
                  + "\033[0m")


console = Console()
console.run()
