# Standard library imports.
import os
import random
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
is_highlighted = []  # Keeps track of if lines should be highlighted


# Main Index Page
@app.route('/', methods=['POST', "GET"])
def index():
    point_data = {}
    line_data = {}
    circle_data = {}
    msg = ""

    # Remove any previously made circles
    for i in range(len(circles)-1, -1, -1):
        del circles[i]

    if request.method == 'POST':
        command = request.form['command']

        # Call appropriate function based on command input
        if command.startswith('add_point'):
            msg = add_point(command)
        elif command.startswith('remove_point'):
            msg = remove_point(command)
        elif command.startswith("clear_points"):
            msg = clear_points()
        elif command.startswith("add_line"):
            msg = add_line(command)
        elif command.startswith("remove_line"):
            msg = remove_line(command)
        elif command.startswith("clear_lines"):
            msg = clear_lines()
        elif command.startswith("closest_pair_of_points"):
            msg = closest_pair()
        elif command.startswith('convex_hull'):
            msg = convex_hull()
        else:
            msg = "Invalid Command."

        point_data, line_data, circle_data = data_into_json() 

        return render_template('index.html', point_data=point_data,
                               line_data=line_data,
                               circle_data=circle_data,
                               msg=msg)
    else:
        return render_template('index.html', point_data=point_data,
                               line_data=line_data,
                               circle_data=circle_data,
                               msg=msg)

def add_point(command):
    try:
        # Parse command
        _, x, y = command.split()
        # Turn x and y into integers and create a Point class variable
        point = Point(int(x), int(y))
        # Add point to points
        points.append(point)
    except Exception as e:
        return f"Error adding point: {e}"
    
    return f"{point} added."

def remove_point(command):
    try:
        # Parse command
        _, x, y = command.split()
        # Turn x and y into integers and create a Point class variable
        point = Point(int(x), int(y))
        # Find the index of the point in points array.
        index = points.index(point)
        # Remove the point from the points array.
        del points[index]
    except Exception as e:
        return f"Error removing point: {e}"
    
    return f"{point} removed"

def clear_points():
    try:
        # Remove each point in points.
        for i in range(len(points)-1, -1, -1):
            del points[i]
    except Exception as e:
        return f"Error clearing point: {e}"
    
    return f"Cleared points."

def add_line(command):
    try:
        # Parse command
        _, x1, y1, x2, y2 = command.split()
        # Turn parsed command into integers and create a Line.
        line = Line(Point(int(x1), int(y1)), Point(int(x2), int(y2)))
        # Add line to lines and False to is_highlighted.
        lines.append(line)
        is_highlighted.append(False)
    except Exception as e:
        return f"Error adding line: {e}"
    
    return f"{line} added"

def remove_line(command):
    try:
        # Parse command
        _, x1, y1, x2, y2 = command.split()
        # Turn parsed command into integers and create a Line.
        line = Line(Point(int(x1), int(y1)), Point(int(x2), int(y2)))
        # Find the index of the line in lines array.
        index = lines.index(line)
        # Remove the line from the lines and is_highlighted array.
        del lines[index]
        del is_highlighted[index]
    except Exception as e:
        return f"Error removing line: {e}"
    
    return f"{line} removed."

def clear_lines():
    try:
        # Remove each line in lines.
        for i in range(len(lines)-1, -1, -1):
            del lines[i]
            del is_highlighted[i]
    except Exception as e:
        return f"Error clearing lines: {e}"
    
    return f"Cleared lines."

def closest_pair():
    try:
        # Turn points in np array
        np_points = np.array(points)

        # Initalize closest pair of points algorithms
        # and find closest pair of points
        closest_pair_finder = ClosestPairOfPoints(np_points)
        min_distance, best_pair = closest_pair_finder.closest_util(
            np_points)
        
        # Generate best_pair as circles to display as red
        circles.append(Circle(Point(best_pair[0].coords[0], best_pair[0].coords[1]), 3))
        circles.append(Circle(Point(best_pair[1].coords[0], best_pair[1].coords[1]), 3))
    except Exception as e:
        return f"Error finding closest pair of points: {e}"
    
    msg = f"({best_pair[0].coords[0]}, " \
          + f"{best_pair[0].coords[1]}) " \
          + f"and ({best_pair[1].coords[0]}, "\
          + f"{best_pair[1].coords[1]}) "\
          + f"are the closest pair of points with"\
          + f" a distance of {min_distance:.3f}."

    return msg


def convex_hull():
    try:
        # Turn points into array of tuples
        tuple_points = [(point.coords[0], point.coords[1])
                        for point in points]

        # Initialize Convex_Hull and do a graham scan on all points
        ch = ConvexHull(tuple_points)
        hull = ch.graham_scan(tuple_points)

        # Create Lines based on graham scan's hull values
        for i in range(len(hull)-1):
            line = Line(Point(hull[i][0], hull[i][1]),
                        Point(hull[i+1][0], hull[i+1][1]))
            lines.append(line)
            is_highlighted.append(False)
    except Exception as e:
        return f"Error finding convex hull: {e}"

    return f"Successfully created convex hull out of {len(hull)-1} points."


def largest_circle(points):
    # Turn points into np.array of array point values
    np_points = np.array([[point.coords[0], point.coords[1]]
                            for point in points])
    
    # Run LargestEmptyCircle algorithm
    lec = LargestEmptyCircle(np_points)
    center, radius = lec.find_largest_empty_circle()

    circles = [Circle(Point(center[0], center[1]), radius)]

    lines = []

    # Put point, line, and circle data into json format
    point_data, line_data, circle_data = data_into_json(points, lines, circles, [])

    return point_data, line_data, circle_data


def line_seg(lines):
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

    # Keep track of lines that intersect so they can be highlighted
    is_highlighted = [False for line in lines]
    for i in range(len(line_pairs)):
        if results[i]:
            for j in range(len(lines)):
                if lines[j] == line_pairs[i][0]:
                    is_highlighted[j] = True
                if lines[j] == line_pairs[i][1]:
                    is_highlighted[j] = True

    points = []
    circles = []

    # Put point, line, and circle data into json format
    point_data, line_data, circle_data = data_into_json(points, lines, circles, is_highlighted)

    return point_data, line_data, circle_data



# Function returns x random points
def random_points(x):
    # Create x random points
    points = []
    for _ in range(x):
        point = Point(random.randint(10, 490), random.randint(10, 490))
        points.append(point)

    return points

# Function returns x random lines
def random_lines(x):
    # Create x random lines
    lines = []
    for _ in range(x):
        line = Line(Point(random.randint(10, 490), random.randint(10, 490)),
                    Point(random.randint(10, 490), random.randint(10, 490)))
        lines.append(line)
        
    return lines


# Function creates random points, lines, and circles
def random_data():
    # Generate 2 random lines, and 2 random circles
    lines = [Line(Point(random.randint(10, 490), random.randint(10, 490)),
                  Point(random.randint(10, 490), random.randint(10, 490))),
             Line(Point(random.randint(10, 490), random.randint(10, 490)),
                  Point(random.randint(10, 490), random.randint(10, 490))),]

    circles = [Circle(Point(random.randint(10, 490), random.randint(10, 490)),
                      random.randint(50, 100)),
               Circle(Point(random.randint(10, 490), random.randint(10, 490)),
                      random.randint(50, 100)),]

    return lines, circles


# Function turns given point, line, and circle data into json format
def data_into_json():
    point_data = {
        "x": [int(point.coords[0]) for point in points],
        "y": [int(point.coords[1]) for point in points],
    }

    line_data = {
        "start_x": [int(line.start.coords[0]) for line in lines],
        "start_y": [int(line.start.coords[1]) for line in lines],
        "end_x": [int(line.end.coords[0]) for line in lines],
        "end_y": [int(line.end.coords[1]) for line in lines],
        "is_highlighted": is_highlighted,
    }

    circle_data = {
        "x": [int(circle.center.coords[0]) for circle in circles],
        "y": [int(circle.center.coords[1]) for circle in circles],
        "radius": [int(circle.radius) for circle in circles],
    }

    return point_data, line_data, circle_data


if __name__ == "__main__":
    app.run(debug=True)
