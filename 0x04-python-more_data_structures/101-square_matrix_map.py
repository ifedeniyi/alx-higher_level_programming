#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    def anon(arr):
        return list(map(lambda x: x**2, arr))
    return list(map(anon, matrix))
