#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for filas in matrix:
        new_fila = []
        for columnas in filas:
            new_fila.append(columnas ** 2)
        new_matrix.append(new_fila)
    return new_matrix
