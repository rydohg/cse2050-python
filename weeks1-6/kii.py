# Author: Ryan Doherty, rdoherty2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Manatee Vocalizations
"""
Manatee Vocalizations.

Recurse and find the character representing
the manatee vocalization at a certain point
in the sequence given as input.
"""
from sys import stdin, stdout

char = int(stdin.readline())
char_count = 0


def calc_vocalizations(i, prev_max=0):
    """Recurse until we find the character."""
    global char_count
    if char_count + 1 == char:
        stdout.write("k\n")
        exit()
    elif char_count + 1 + i > char:
        stdout.write("i\n")
        exit()
    char_count += 1 + i
    if i != 2:
        calc_vocalizations(i - 1, prev_max)
    if i > prev_max:
        prev_max = i
        calc_vocalizations(i + 1, prev_max)


calc_vocalizations(2)
