#!/usr/bin/python3

def weight_average(my_list=[]):
    lhs = sum([x*y for x, y in my_list])
    rhs = sum([y for _, y in my_list])

    return lhs/rhs
