#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    av = sys.argv
    ac = len(av) - 1
    sum = 0

    for i in range(1, ac+1):
        sum += int(av[i])

    print("{}".format(sum))
