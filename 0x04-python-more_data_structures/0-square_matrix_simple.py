#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for i, v in enumerate(matrix):
        new_matrix.append(list(map(lambda x: x**2, v)))

    return new_matrix
