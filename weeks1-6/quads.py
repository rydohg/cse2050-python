# Author: Ryan Doherty, rdoherty2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Quads Workout
from sys import stdin, stdout

x = int(stdin.readline())
y = int(stdin.readline())

if x > 0 and y > 0:
    stdout.write("I")
elif (x < 0) and y > 0:
    stdout.write("II")
elif x < 0 and y < 0:
    stdout.write("III")
else:
    stdout.write("IV")
