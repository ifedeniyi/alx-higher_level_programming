#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0 or my_list is None:
        return 0

    lhs = sum([x*y for x, y in my_list])
    rhs = sum([y for _, y in my_list])

    return lhs/rhs
