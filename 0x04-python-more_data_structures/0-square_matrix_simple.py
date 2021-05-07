#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for item in matrix:
        new_list = list(map(lambda x: x ** 2, item))
        new_matrix.append(new_list)
    return new_matrix
