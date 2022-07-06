#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import calculator_1 as calc

    av = sys.argv
    ac = len(av) - 1
    ops = ["+", "-", "*", "/"]

    if ac != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if av[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(av[1])
    b = int(av[3])

    if av[2] == "+":
        print("{} + {} = {}".format(av[1], av[3], calc.add(a, b)))
    if av[2] == "-":
        print("{} - {} = {}".format(av[1], av[3], calc.sub(a, b)))
    if av[2] == "*":
        print("{} * {} = {}".format(av[1], av[3], calc.mul(a, b)))
    if av[2] == "/" or av[2] == "//":
        print("{} / {} = {}".format(av[1], av[3], calc.div(a, b)))
