#!/usr/bin/python3

def max_integer(my_list=[]):
    max = 0

    if not my_list or len(my_list) < 1:
        return None
    
    for i in my_list:
        max = i if i > max else max

    return max
