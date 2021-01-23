# Author: Ryan Doherty, rdoherty2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Master Mind
from sys import stdin

code, guess = stdin.readline().split()
r = 0
s = 0
for i in range(len(code)):
    if code[i] == guess[i]:
        r += 1
    elif guess[i] in code and not guess[i] in guess[:i]:
        s += 1

print(f"{r} {s}")
