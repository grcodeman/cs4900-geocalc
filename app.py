from flask import Flask, render_template, request, redirect
from backend.point import Point

import random

app = Flask(__name__)

# Main Index Page
@app.route('/', methods=['POST', "GET"])
def index():
    if request.method == 'POST':
        option = request.form['options']

        # Based on user entered option, call appropriate function
        if option == 'op1':
            point_data = line_seg()
        elif option == 'op2':
            point_data = closest_pair()
        elif option == 'op3':
            point_data = convex_hull()
        elif option == 'op4':
            point_data = largest_circle()
        else:
            print('invalid option')
            point_data = {}

        return render_template('index.html', point_data=point_data)
    else:
        point_data = {}

        return render_template('index.html', point_data=point_data)


def line_seg():
    print('line seg')

    points = random_points(50)

    # Put points into json format
    point_data = {
        "x": [point.x for point in points],
        "y": [point.y for point in points],
    }

    return point_data


def closest_pair():
    print('closest pair')

    points = random_points(50)

    # Put points into json format
    point_data = {
        "x": [point.x for point in points],
        "y": [point.y for point in points],
    }

    return point_data


def convex_hull():
    print('convex hull')

    points = random_points(50)

    # Put points into json format
    point_data = {
        "x": [point.x for point in points],
        "y": [point.y for point in points],
    }

    return point_data


def largest_circle():
    print('largest circle')

    points = random_points(50)

    # Put points into json format
    point_data = {
        "x": [point.x for point in points],
        "y": [point.y for point in points],
    }

    return point_data
 
    
# Function returns x random points
def random_points(x):
    # Create x random points
    points = []
    for _ in range(x):
        point = Point(random.randint(10, 490), random.randint(10, 490))
        points.append(point)

    return points


if __name__ == "__main__":
    app.run(debug=True)