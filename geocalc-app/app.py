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


# Main Index Page
@app.route('/', methods=['POST', "GET"])
def index():
    point_data = {}
    line_data = {}
    circle_data = {}

    if request.method == 'POST':
        option = request.form['options']
        point_num = request.form['point_num']

        # If user didn't given a number of points, re-render index page
        if point_num == '':
            return render_template('index.html', point_data=point_data,
                                   line_data=line_data,
                                   circle_data=circle_data,)

        # Create number of points given by user
        points = random_points(int(point_num))

        # Based on user entered option, call appropriate function
        if option == 'op1':
            point_data, line_data, circle_data = line_seg(points)
        elif option == 'op2':
            point_data, line_data, circle_data = closest_pair(points)
        elif option == 'op3':
            point_data, line_data, circle_data = convex_hull(points)
        elif option == 'op4':
            point_data, line_data, circle_data = largest_circle(points)
        else:
            print('invalid option')

        return render_template('index.html', point_data=point_data,
                               line_data=line_data,
                               circle_data=circle_data,)
    else:
        return render_template('index.html', point_data=point_data,
                               line_data=line_data,
                               circle_data=circle_data,)


def closest_pair(points):
    np_points = np.array(points)
    closest_pair_finder = ClosestPairOfPoints(np_points)
    min_distance, best_pair = closest_pair_finder.closest_util(
        np_points)
    
    # Generate best_pair as circles to display as red
    circles = [Circle(Point(best_pair[0].coords[0], best_pair[0].coords[1]), 3), 
               Circle(Point(best_pair[1].coords[0], best_pair[1].coords[1]), 3)]

    lines = []

    # Put point, line, and circle data into json format
    point_data, line_data, circle_data = data_into_json(points, lines, circles)

    return point_data, line_data, circle_data


def convex_hull(points):
    # Turn points into array of tuples
    tuple_points = [(point.coords[0], point.coords[1])
              for point in points]

    # Initialize Convex_Hull and do a graham scan on all points
    ch = ConvexHull(tuple_points)
    hull = ch.graham_scan(tuple_points)

    # Create Lines based on graham scan's hull values
    lines = []
    for i in range(len(hull)-1):
        line = Line(Point(hull[i][0], hull[i][1]),
                    Point(hull[i+1][0], hull[i+1][1]))
        lines.append(line)

    circles = []

    # Put point, line, and circle data into json format
    point_data, line_data, circle_data = data_into_json(points, lines, circles)

    return point_data, line_data, circle_data


def largest_circle(points):
    Largest_Circle.test()

    # Generate random point, line, and circle data
    lines, circles = random_data()

    # Put point, line, and circle data into json format
    point_data, line_data, circle_data = data_into_json(points, lines, circles)

    return point_data, line_data, circle_data


def line_seg(points):
    Line_Seg.test()

    # Generate random line, and circle data
    lines, circles = random_data()

    # Put point, line, and circle data into json format
    point_data, line_data, circle_data = data_into_json(points, lines, circles)

    return point_data, line_data, circle_data



# Function returns x random points
def random_points(x):
    # Create x random points
    points = []
    for _ in range(x):
        point = Point(random.randint(10, 490), random.randint(10, 490))
        points.append(point)

    return points


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
def data_into_json(points, lines, circles):
    point_data = {
        "x": [int(point.coords[0]) for point in points],
        "y": [int(point.coords[1]) for point in points],
    }

    line_data = {
        "start_x": [int(line.start.coords[0]) for line in lines],
        "start_y": [int(line.start.coords[1]) for line in lines],
        "end_x": [int(line.end.coords[0]) for line in lines],
        "end_y": [int(line.end.coords[1]) for line in lines],
    }

    circle_data = {
        "x": [int(circle.center.coords[0]) for circle in circles],
        "y": [int(circle.center.coords[1]) for circle in circles],
        "radius": [int(circle.radius) for circle in circles],
    }

    return point_data, line_data, circle_data


if __name__ == "__main__":
    app.run(debug=True)
