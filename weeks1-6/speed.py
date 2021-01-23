# Author: Ryan Doherty, rdoherty2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Speed Limit
from sys import stdin

while True:
    num_of_speeds = int(stdin.readline())
    if num_of_speeds == -1:
        break

    distance = 0
    prev_time = 0
    for i in range(0, num_of_speeds):
        speed, time = map(int, stdin.readline().split())
        distance += speed * (time - prev_time)
        prev_time = time
    print(f'{distance} miles')
