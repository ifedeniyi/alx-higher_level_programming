#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    av = sys.argv
    ac = len(av) - 1
    ops = ["+", "-", "*", "/"]

    if ac != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if av[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if av[2] == "+":
        print("{} + {} = {}".format(av[1], av[3], int(av[1]) + int(av[3])))
    if av[2] == "-":
        print("{} - {} = {}".format(av[1], av[3], int(av[1]) - int(av[3])))
    if av[2] == "*":
        print("{} * {} = {}".format(av[1], av[3], int(av[1]) * int(av[3])))
    if av[2] == "/":
        print("{} / {} = {}".format(av[1], av[3], int(av[1]) / int(av[3])))
