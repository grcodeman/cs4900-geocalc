from flask import Flask, render_template, request

from backend.point import Point
from backend.line import Line
from backend.circle import Circle

from backend.line_seg import Line_Seg
from backend.closest_pair import Closest_Pair
from backend.convex_hull import Convex_Hull
from backend.largest_circle import Largest_Circle

import random

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
    Convex_Hull.test()

    # Generate random point, line, and circle data
    lines, circles = random_data()

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
