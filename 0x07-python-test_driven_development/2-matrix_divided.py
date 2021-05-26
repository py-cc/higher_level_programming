#!/usr/bin/python3
""" Module that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ Function that divides all elements of a matrix with number (div)

        Returns:  a new_matrix with result division

        Raises:
            TypeError: if elements in matrix are nor int an float
            TypeError: If rows of the matrix have diferente size
            TypeError: if div variable is not an int or a float
            ZeroDivisionError: if div is equal to 0
    """

# Error data type and elements (int/float and list)
    if isinstance(matrix, list) is not True or len(matrix) == 0:
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')

    for item in matrix:
        if isinstance(item, list) is not True or len(item) == 0:
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
    for element in item:
        if type(element) not in (int, float):
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')

# Error len matrix, len column and row
    for i in range(len(matrix)):
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError('Each row of the matrix must have the same size')
        else:
            continue

# data type int or float is not zero of div number
    if type(div) not in (int, float):
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')

# logic matrix in new list and divides with number (div)
    new_matrix = []
    for i in matrix:
        new_list = []
        for j in i:
            resultado = j / div
            new_list.append(round(resultado, 2))
        new_matrix.append(new_list)
    return new_matrix
