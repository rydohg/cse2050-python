# Wow i thought this was clever but it didn't get full points
from sys import stdin
import math


def num_boring_numbers(l, r):
    count = 0
    for num in range(l, r + 1):
        boring = True
        num_digits = int(math.log(num, 10)) + 1
        position = 1
        for decimal_place in reversed(range(int(num_digits))):
            digit = int(num % pow(10, decimal_place + 1) / pow(10, decimal_place))
            # if not in an even position and the digit is even it's not boring
            if digit % 2 == 0 and position % 2 != 0:
                boring = False
            elif digit % 2 != 0 and position % 2 == 0:
                boring = False
            position += 1
        if boring:
            count += 1
    return count


num_test_cases = int(stdin.readline())
for case in range(num_test_cases):
    test_case = [int(num) for num in stdin.readline().rstrip().split()]
    print(f"Case #{case + 1}: {num_boring_numbers(test_case[0], test_case[1])}")
