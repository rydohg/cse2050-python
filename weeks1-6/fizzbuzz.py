# Author: Ryan Doherty, rdoherty2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Fizz Buzz

while line := input():
    x, y, n = map(int, line.split())
    for i in range(1, n + 1):
        if i % x == 0 and i % y == 0:
            print("FizzBUzz")
        elif i % x == 0:
            print("Fizz")
        elif i % y == 0:
            print("Buzz")
        else:
            print(i)
