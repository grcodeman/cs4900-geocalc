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
            # Convert strings to integers and create a Point class variable.
            point = Point(int(x), int(y))
            # Add the point to the points array.
            self.points.append(point)
            # Print a success message in green.
            print("\033[92m" + f"Point {point} added." + "\033[0m")
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
            # Convert strings to integers and create a Point class variable
            point = Point(int(x), int(y))
            try:
                # Find the index of the point in points array.
                index = self.points.index(point)
                # Remove the point from the points array.
                del self.points[index]
                # Print a success message in green.
                print("\033[92m" + f"Point {point} removed." + "\033[0m")
            except ValueError:
                # Print an error in red.
                print("\033[91m" + f"Point entered does not exist." + "\033[0m")
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
            # Add the line to lines array
            self.lines.append(line)
            # Print a success message in green.
            print("\033[92m" + f"Point {line} added." + "\033[0m")
        except ValueError:
            # Print a user error in yellow.
            print("\033[93m" + "Invalid point format. Usage: add_line x1 y1 x2 y2"
                  + "\033[0m")
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
                print("\033[92m" + f"Line {line} removed." + "\033[0m")
            except ValueError:
                # Print an error in red.
                print("\033[91m" + f"Line entered does not exist." + "\033[0m")
        except ValueError:
            # Print an error in yellow.
            print("\033[93m" + "Invalid line format. Usage: remove_line x1 y1 x2 y2"
                  + "\033[0m")
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
        try:
            # Assuming command format is "closest_pair_of_points"
            _, = command.split()
            # Turn points into an np.array and call ClosestPairOfPoints Algorithm 
            np_points = np.array(self.points)
            closest_pair_finder = ClosestPairOfPoints(np_points)
            min_distance, best_pair = closest_pair_finder.closest_util(np_points)
            # Print a success message in green displaying algorithm information
            print("\033[92m" + f"({best_pair[0].coords[0]}, {best_pair[0].coords[1]}) " 
                  + f"({best_pair[1].coords[0]}, {best_pair[1].coords[1]}) "
                  + f"are the closest pair of points with a distance of {min_distance:.3f}."
                  + "\033[0m")
        except Exception as e:
            # Print an error in red.
            print("\033[91m" + f"Error finding closest pair: {e}" + "\033[0m")


console = Console()
console.run()