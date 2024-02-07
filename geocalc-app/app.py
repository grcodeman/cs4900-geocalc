# Standard library imports.
import os
import random
import sys

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
from geocalc_lib.algorithms import *
from geocalc_lib.shapes.circle import *


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


def line_seg(points):
    Line_Seg.test()

    # Generate random line, and circle data
    lines, circles = random_data()

    # Put point, line, and circle data into json format
    point_data, line_data, circle_data = data_into_json(points, lines, circles)

    return point_data, line_data, circle_data


def closest_pair(points):
    Closest_Pair.test()

    # Generate random point, line, and circle data
    lines, circles = random_data()

    # Put point, line, and circle data into json format
    point_data, line_data, circle_data = data_into_json(points, lines, circles)

    return point_data, line_data, circle_data


def convex_hull(points):
    # Convert Class point values into array values
    point_arr = []
    for point in points:
        point_arr.append([point.x, point.y])

    # Initialize Convex_Hull and do a graham scan on all points
    ch = Convex_Hull()
    hull = ch.graham_scan(point_arr)

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
        "x": [point.x for point in points],
        "y": [point.y for point in points],
    }

    line_data = {
        "start_x": [line.start.x for line in lines],
        "start_y": [line.start.y for line in lines],
        "end_x": [line.end.x for line in lines],
        "end_y": [line.end.y for line in lines],
    }

    circle_data = {
        "x": [circle.center.x for circle in circles],
        "y": [circle.center.y for circle in circles],
        "radius": [circle.radius for circle in circles],
    }

    return point_data, line_data, circle_data


if __name__ == "__main__":
    app.run(debug=True)
