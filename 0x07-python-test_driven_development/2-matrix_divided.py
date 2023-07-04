#!/usr/bin/python3
''' this is 2-matrix_divided module
This module supplies one function, matrix_divided().  For example
>>> matrix_divided([[3, 6, 10],[20, 70, 98]], 2)
[[1.5, 3.0, 5.0], [10.0, 35.0, 49.0]]
'''


def matrix_divided(matrix, div):
    ''' Divid matrix by div
        Return new matrix with all elements rounded to 2 decimal places
    '''
    if matrix is None or type(matrix) not in [list] or len(matrix) == 0 or\
            type(matrix[0]) not in [list] or len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    length = len(matrix[0])
    for raw in matrix:
        if len(raw) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for i in raw:
            if type(i) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    ls = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return ls
