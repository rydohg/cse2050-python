# Author: Ryan Doherty, rdoherty2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Newton's Basin
"""
Newton's Basin.

Run Newton's method to find whether a given guess converges
to a root of the given polynomial.
"""
from sys import stdin, stdout

roots = [complex(num) for num in stdin.readline().split()]


def equation(x):
    """Return the result of the given polynomial at point x."""
    result = x - roots[0]
    for root in roots[1:]:
        result *= x - root
    return result


def derivative(x):
    """Return derivative of the polynomial made from the roots at point x."""
    delta_x = 0.0000001
    return (equation(x + delta_x) - equation(x)) / delta_x


def newtons_method(guess, iteration=0):
    """Run Newton's method until it converges or hits 20 iterations."""
    if iteration >= 20:
        return "diverges"
    new_guess = guess - (equation(guess) / derivative(guess))
    epsilon = 0.00001
    for i in range(len(roots)):
        if new_guess.real - epsilon < roots[i].real < new_guess.real + epsilon:
            return i
    return newtons_method(new_guess, iteration + 1)


while initial_guess := stdin.readline():
    stdout.write(f"{newtons_method(complex(initial_guess))}\n")
