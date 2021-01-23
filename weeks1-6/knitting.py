# Author: Ryan Doherty, rdoherty2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Knitting
from sys import stdin

n, m, k = map(int, stdin.readline().split())

pattern = list(map(int, stdin.readline().split()))

total_stitches = n
prev_row_stitches = n
for i in range(m - 1):
    this_row_stitches = prev_row_stitches + pattern[i % (len(pattern))]
    total_stitches += this_row_stitches
    prev_row_stitches = this_row_stitches

print(total_stitches)
