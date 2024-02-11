# geocalc - Geometric Computations Package

## Overview
This repository serves as a workspace for geocalc.

**geocalc-lib** is a Python package designed to complete geometric computations.  
It can also be imported into other projects.  
**geocalc-app** is the frontend designed to (optionally) interact with geocalc-lib. 

## Features
The initial release, Version 1.0, includes the following capabilities:

- **Points**: Represent a single point in 2D space.
- **Line Segments**: Define a straight line between two distinct points.
- **Circles**: Represented by a center point and a radius.

As well as the following computational capabilities:
- **Closest Pair of Points**: Find the closest pair of points.
- **Convex hull**: Find a convex hull among a list of supplied points.
- **Largest Empty Circle**: Find the largest empty circle possible.
- **Line Segment Intersections**: Find the line intersections among a given set of lines.

## Usage
Intall requirements.txt (pip install -r requirements.txt)

**app.py** is a frontend program that launches a flask web application where the user can
enter commands which will display on a graph. The user can add/remove points and lines,
perform algorithms, and change the displayed graph grid size.

    Command to run app.py in terminal: python app.py | python3 app.py

    Development server on 'http://localhost:5000/' or 'http://127.0.0.1:5000'.

**console.py** launches a command line user interface where the user
can add/remove points and lines and perform algorithms.

    Command to run console.py in terminal: python console.py | python3 console.py

    Enter 'help' while running program to display commands.

## Authors (alphabetically)
[Ahmed Alabkri](https://github.com/AhmedAlabkri)  
[Ali Azimi](https://github.com/aliazim1)  
[Matthew Schaney](https://github.com/matthewschaney)  
[Sam Selesky](https://github.com/samselesky)  
[Cody Thornell](https://github.com/grcodeman)  
