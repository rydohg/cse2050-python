# Author: Ryan Doherty, rdoherty2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Annual Percentage Rate
from decimal import *
from sys import stdin, stdout


def right_align(col_size, str_size):
    for i in range(0, col_size - str_size):
        stdout.write(" ")


balance, apr, payment = map(Decimal, stdin.readline().split())
print("payment       balance      interest")

stdout.write("      0")
right_align(14, len("{:2f}".format(balance)))

stdout.write('{:2f}'.format(balance))
right_align(14, 4)
stdout.write("0.00")
print(" ")
total_interest: Decimal = Decimal(0)
interest: Decimal = balance * apr / 100 / 12
for i in range(1, 100):
    interest = round(balance * apr / 100 / 12, 2)
    balance = balance + interest - payment
    total_interest += interest
    if balance <= 0:
        right_align(7, len(str(i)))
        stdout.write("{:d}".format(i))
        right_align(14, 4)

        stdout.write('0.00')
        right_align(14, len("{:.2f}".format(total_interest)))
        stdout.write("{:.2f}".format(total_interest))
        print(" ")
        break
    right_align(7, len(str(i)))
    stdout.write('{:d}'.format(i))
    right_align(14, len("{:2f}".format(balance)))
    stdout.write('{:2f}'.format(balance))
    right_align(14, len("{:2f}".format(total_interest)))
    stdout.write("{:2f}".format(total_interest))
    print("")
