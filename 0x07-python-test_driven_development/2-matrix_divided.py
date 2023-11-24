#!/usr/bin/python3
"""_summary_"""


def matrix_divided(matrix, div):
    """Divides all elements in the matrix by div"""
    # check if all int or float
    size = -1
    for row in matrix:
        if size == -1:
            size = len(row)
        elif size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix must be a matrix"
                                " (list of lists) of integers/floats")

    # ! check if div is 0 or not number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    # ! Create the new matrix
    matrix2 = [[round(element/div, 2) for element in row] for row in matrix]

    return (matrix2)
