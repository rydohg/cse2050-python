# First Problem Google Kickstart Round H
from sys import stdin

num_test_cases = int(stdin.readline())


def find_least_amount_of_time(n, k, s):
    # if it is longer to go back then complete
    time_to_go_back_and_return = (k - s) + (n - s)
    if time_to_go_back_and_return > n:
        return k + n
    else:
        return k + time_to_go_back_and_return


for i in range(num_test_cases):
    test_case = [int(num) for num in stdin.readline().rstrip().split()]
    print(f"Case #{i}: {find_least_amount_of_time(test_case[0], test_case[1], test_case[2])}")
