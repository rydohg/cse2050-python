# Author: Ryan Doherty, rdoherty2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Tri-Color Sort
from sys import stdin

us = []
ca = []
aus = []

while id_number := stdin.readline():
    if id_number.rstrip().endswith("036"):  # aus
        aus.append(id_number.rstrip())
    elif id_number.rstrip().endswith("124"):  # can
        ca.append(id_number.rstrip())
    elif id_number.rstrip().endswith("840"):  # US
        us.append(id_number.rstrip())

for id_number in aus + ca + us:
    print(id_number)
