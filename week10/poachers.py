# Author: Ryan Doherty, rdoherty2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Poachers
"""
Poachers.

Calculate which manatees are safe from poachers and which
manatees are in danger or vulnerable to them using scipy's
convex_hull
"""
import numpy
from scipy.spatial import ConvexHull
from sys import stdin, stdout


def within_polygon(points, test_point):
    """
    Calculate if test_point is within the polygon.

    A point is within the hull if it doesn't change
    the hull if we add it and recalculate the hull.
    """
    convex_hull = ConvexHull(numpy.asarray(points))
    test_points = points
    test_points.append(test_point)
    test_hull = ConvexHull(numpy.asarray(test_points))
    if set(convex_hull.vertices) == set(test_hull.vertices):
        return True
    else:
        return False


num_people_and_manatees = \
    [int(number) for number in stdin.readline().rstrip().split(" ")]

warden_positions = []
poacher_positions = []
manatee_positions = []

for i in range(num_people_and_manatees[0]):
    warden_positions.append(
        [int(number) for number in stdin.readline().rstrip().split()])

for i in range(num_people_and_manatees[1]):
    poacher_positions.append(
        [int(number) for number in stdin.readline().rstrip().split()])

for i in range(num_people_and_manatees[2]):
    manatee_positions.append(
        [int(number) for number in stdin.readline().rstrip().split()])

for manatee in manatee_positions:
    stdout.write(f"Manatee at ({manatee[0]},{manatee[1]}) is ")
    if within_polygon(warden_positions, manatee):
        stdout.write("safe")
    elif within_polygon(poacher_positions, manatee):
        stdout.write("endangered")
    else:
        stdout.write("vulnerable")
    stdout.write(".\n")
