"""
Program launches a flask webserver running at 'http://127.0.0.1:5000'
or 'http://localhost:5000/' where the user can enter commands to 
add/remove/clear points and lines, run algorithms,
and resize the displayed grid.
"""

# Standard library imports.
import os
import sys
import numpy as np

# Third-party imports.
from flask import Flask, render_template, request

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
from geocalc_lib.shapes.circle import Circle
from geocalc_lib.algorithms.closest_pair_of_points import ClosestPairOfPoints
from geocalc_lib.algorithms.convex_hull import ConvexHull
from geocalc_lib.algorithms.largest_empty_circle import LargestEmptyCircle
from geocalc_lib.algorithms.line_segment import LineSegmentIntersection

app = Flask(__name__)

# Initialize points, lines, and circles as empty arrays
points = []
lines = []
circles = []
# Keeps track of if points and lines should be highlighted
is_highlighted = [[], []]
# Also keep track of grid size
grid_size = [10]


@app.route('/', methods=['POST', "GET"])
def index():
    """
    Main index page, calls functions based on user input.
    """
    point_data = {}
    line_data = {}
    circle_data = {}
    msg = ["Enter 'help' to view commands."]

    # Remove any previously made circles
    # and highlighted points and lines
    for i in range(len(circles)-1, -1, -1):
        del circles[i]

    for i in range(len(is_highlighted[0])):
        is_highlighted[0][i] = False
    for i in range(len(is_highlighted[1])):
        is_highlighted[1][i] = False

    if request.method == 'POST':
        # Get user inputted command
        command = request.form['command']

        # Call appropriate function based on command input
        if command.startswith('add_point'):
            msg = [add_point(command)]
        elif command.startswith('remove_point'):
            msg = [remove_point(command)]
        elif command.startswith("clear_points"):
            msg = [clear_points()]
        elif command.startswith("add_line"):
            msg = [add_line(command)]
        elif command.startswith("remove_line"):
            msg = [remove_line(command)]
        elif command.startswith("clear_lines"):
            msg = [clear_lines()]
        elif command.startswith("closest_pair_of_points"):
            msg = [closest_pair()]
        elif command.startswith('convex_hull'):
            msg = [convex_hull()]
        elif command.startswith('largest_empty_circle'):
            msg = [largest_circle()]
        elif command.startswith('line_segment'):
            msg = [line_segment()]
        elif command.startswith('set_grid'):
            msg = [set_grid(command)]
        elif command.startswith('help'):
            # Display help message with commands
            msg = ["Add a point or line: add_point x y |"
                   + " add_line x1 y1 x2 y2",
                   "Remove a point or line: remove_point x y |"
                   + " remove_line x1 y1 x2 y2",
                   "Clear all points or lines: clear_points | clear_lines",
                   "Algorithms: closest_pair_of_points | convex_hull | "
                   + "largest_empty_circle | "
                   + "line_segment",
                   "Change grid size: set_grid d"]
        else:
            msg = ["Invalid Command."]

        # Turn points, lines, and circles into json data
        point_data, line_data, circle_data = data_into_json()

        # Render index.html with supplied data
        return render_template('index.html', point_data=point_data,
                               line_data=line_data,
                               circle_data=circle_data,
                               msg=msg, grid_size=grid_size[0])
    else:
        # Render index.html with supplied data
        return render_template('index.html', point_data=point_data,
                               line_data=line_data,
                               circle_data=circle_data,
                               msg=msg, grid_size=grid_size[0])


def add_point(command):
    """
    Adds a point to points array.
    """
    try:
        # Parse command
        _, x, y = command.split()
        # Turn x and y into integers and create a Point class variable
        point = Point(int(x), int(y))
        # Add point to points is is_highlighted as False
        points.append(point)
        is_highlighted[0].append(False)
    except Exception as e:
        return f"Error adding point: {e}"

    return f"{point} added."


def remove_point(command):
    """
    Removes a given point from points array.
    """
    try:
        # Parse command
        _, x, y = command.split()
        # Turn x and y into integers and create a Point class variable
        point = Point(int(x), int(y))
        # Find the index of the point in points array.
        index = points.index(point)
        # Remove the point from the points array and highlighted value.
        del points[index]
        del is_highlighted[0][index]
    except Exception as e:
        return f"Error removing point: {e}"

    return f"{point} removed"


def clear_points():
    """
    Removes all points from points array.
    """
    try:
        # Remove each point in points array and is_highlighted value.
        for i in range(len(points)-1, -1, -1):
            del points[i]
            del is_highlighted[0][i]
    except Exception as e:
        return f"Error clearing point: {e}"

    return f"Cleared points."


def add_line(command):
    """
    Adds a line to lines array.
    """
    try:
        # Parse command
        _, x1, y1, x2, y2 = command.split()
        # Turn parsed command into integers and create a Line.
        line = Line(Point(int(x1), int(y1)), Point(int(x2), int(y2)))
        # Add line to lines and False to is_highlighted.
        lines.append(line)
        is_highlighted[1].append(False)
    except Exception as e:
        return f"Error adding line: {e}"

    return f"{line} added"


def remove_line(command):
    """
    Removes a given line from lines array.
    """
    try:
        # Parse command
        _, x1, y1, x2, y2 = command.split()
        # Turn parsed command into integers and create a Line.
        line = Line(Point(int(x1), int(y1)), Point(int(x2), int(y2)))
        # Find the index of the line in lines array.
        index = lines.index(line)
        # Remove the line from the lines and is_highlighted array.
        del lines[index]
        del is_highlighted[1][index]
    except Exception as e:
        return f"Error removing line: {e}"

    return f"{line} removed."


def clear_lines():
    """
    Removes every line from lines array.
    """
    try:
        # Remove each line in lines and its is_highlighted value.
        for i in range(len(lines)-1, -1, -1):
            del lines[i]
            del is_highlighted[1][i]
    except Exception as e:
        return f"Error clearing lines: {e}"

    return f"Cleared lines."


def closest_pair():
    """
    Function performs the closest pair of points algorithm on all
    points and displays the closest pair of points as highlighted.
    """
    try:
        # Turn points in np array
        np_points = np.array(points)

        # Initalize closest pair of points algorithms
        # and find closest pair of points
        closest_pair_finder = ClosestPairOfPoints(np_points)
        min_distance, best_pair = closest_pair_finder.closest_util(
            np_points)

        # Highlight the closest pair of points
        for i in range(len(points)):
            if points[i] in best_pair:
                is_highlighted[0][i] = True
    except Exception as e:
        return f"Error finding closest pair of points: {e}"

    # Generate output message
    msg = f"({best_pair[0].coords[0]}, " \
          + f"{best_pair[0].coords[1]}) " \
          + f"and ({best_pair[1].coords[0]}, "\
          + f"{best_pair[1].coords[1]}) "\
          + f"are the closest pair of points with"\
          + f" a distance of {min_distance:.3f}."

    return msg


def convex_hull():
    """
    Function performs the convex hull algorithm on all points
    and creates the convex hull with lines connecting each hull point.
    """
    try:
        # Turn points into array of tuples
        tuple_points = [(point.coords[0], point.coords[1])
                        for point in points]

        # Initialize ConvexHull and do a graham scan on all points
        ch = ConvexHull(tuple_points)
        hull = ch.graham_scan(tuple_points)

        # Create Lines based on graham scan's hull values
        for i in range(len(hull)-1):
            line = Line(Point(hull[i][0], hull[i][1]),
                        Point(hull[i+1][0], hull[i+1][1]))
            lines.append(line)
            is_highlighted[1].append(False)
    except Exception as e:
        return f"Error finding convex hull: {e}"

    return f"Successfully created convex hull out of {len(hull)-1} points."


def largest_circle():
    """
    Function performs the largest empty circle algorithm on all points
    and creates the largest empty circle to be displayed.
    """
    try:
        # Turn points into np.array of array point values
        np_points = np.array([[point.coords[0], point.coords[1]]
                              for point in points])

        # Run LargestEmptyCircle algorithm
        lec = LargestEmptyCircle(np_points)
        center, radius = lec.find_largest_empty_circle()

        # Create largest empty circle
        circles.append(Circle(Point(float(center[0]),
                                    float(center[1])), float(radius)))
    except Exception as e:
        return f"Error finding largest empty circle: {e}"

    return f"Largest empty circle has a center of"\
           + f" {center} and radius of {radius:.3f}."


def line_segment():
    """
    Function performs the line segment intersection algorithm on all
    lines and highlights all intersecting lines.
    """
    try:
        # Get each pair of lines
        line_pairs = []
        for i, line1 in enumerate(lines):
            for line2 in lines[i + 1:]:
                line_pairs.append([line1, line2])

        # For each pair of lines, call LineSegmentIntersection algorithm
        lsi = LineSegmentIntersection(np.array([]))
        results = []
        for pair in line_pairs:
            result = lsi.do_intersect(pair[0].start, pair[0].end,
                                      pair[1].start, pair[1].end)
            results.append(result)

        # Highlight each line that intersects with another line.
        for i in range(len(line_pairs)):
            if results[i]:
                for j in range(len(lines)):
                    if lines[j] in line_pairs[i]:
                        is_highlighted[1][j] = True

        # Get number of intersections
        intersect_count = 0
        for highlight in is_highlighted[1]:
            if highlight:
                intersect_count += 1
    except Exception as e:
        return f"Error finding line segment intersections: {e}"

    return f"{intersect_count} lines intersect."


def set_grid(command):
    """
    Function changes the grid size to the given user input.
    """
    try:
        # Parse command
        _, new_size = command.split()
        # Set new_size as an integer
        new_size = int(new_size)
        # Set grid_size to new_size
        del grid_size[0]
        grid_size.append(new_size)
    except Exception as e:
        return f"Error setting new grid size: {e}"

    return f"Successfully set new grid size to {grid_size}"


def data_into_json():
    """
    Function turns given point, line, and circle data into json format.
    """
    point_data = {
        "x": [int(point.coords[0]) for point in points],
        "y": [int(point.coords[1]) for point in points],
        "is_highlighted": is_highlighted[0],
    }

    line_data = {
        "start_x": [int(line.start.coords[0]) for line in lines],
        "start_y": [int(line.start.coords[1]) for line in lines],
        "end_x": [int(line.end.coords[0]) for line in lines],
        "end_y": [int(line.end.coords[1]) for line in lines],
        "is_highlighted": is_highlighted[1],
    }

    circle_data = {
        "x": [float(circle.center.coords[0]) for circle in circles],
        "y": [float(circle.center.coords[1]) for circle in circles],
        "radius": [float(circle.radius) for circle in circles],
    }

    return point_data, line_data, circle_data


if __name__ == "__main__":
    app.run(debug=True)
