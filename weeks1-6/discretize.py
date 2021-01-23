# Author: Ryan Doherty, rdoherty2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Discretizing the Sphere
from sys import stdin
from decimal import *
from math import *

# half of each dimension of the grid
n, m = map(int, stdin.readline().split())

while True:
    # phi (latitude) and lambda (longitude) (lambda is reserved in python)
    latitude, longitude = map(Decimal, stdin.readline().split())
    x_coord = 0
    y_coord = 0
    if latitude > 0:
        dist_from_x_axis = min(floor(latitude % 360 / 45), n * 2)
        x_coord = n + dist_from_x_axis
    else:
        dist_from_x_axis = min(ceil(latitude % 360 / 45), n * 2)
        x_coord = n - dist_from_x_axis

    if longitude > 0:
        dist_from_y_axis = 0
        if longitude > m * 45:
            dist_from_y_axis = min(-(m * 45) + floor(longitude % (m * 45) / 45), m * 2)
        else:
            dist_from_y_axis = min(floor(longitude % (m * 45) / 45), m * 2)
        y_coord = m + dist_from_y_axis
    else:
        dist_from_y_axis = min(ceil(longitude % 360 / 45), m * 2)
        y_coord = m - dist_from_y_axis

    print(f"x coord: {x_coord}")
    print(f"y coord: {y_coord}")