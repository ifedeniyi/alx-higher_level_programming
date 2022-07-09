#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    for i, v in enumerate(set(my_list)):
        sum += v
    return sum
