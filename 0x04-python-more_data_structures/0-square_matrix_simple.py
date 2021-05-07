def square_matrix_simple(matrix=[]):
    new_matrix = []
    for item in matrix:
        list_square = list(map(lambda x: x ** 2, item))
        new_matrix.append(list_square)
    return new_matrix
