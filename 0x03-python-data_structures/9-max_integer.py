#!/usr/bin/python3

def max_integer(my_list=[]):
    maxnum = 0

    if not my_list or len(my_list) < 1:
        return None

    for i in my_list:
        maxnum = i if i > maxnum else maxnum

    return maxnum
