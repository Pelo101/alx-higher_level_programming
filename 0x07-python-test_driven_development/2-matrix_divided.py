#!/usr/bin/python3
"""

This module divides all the elements of the matrix



"""


def matrix_divided(matrix, div):
    """
   This function divides all the elements of a matrix

    Args:
       Matrix : list of lists that contains integers and/or floats.
       div: number that is used to divide

    Return:
       new matrix after division.

    Raises:

          TypeError:
                   If matrix elements are not integers and/or floats.
                   If row of matrix are not the same size
                   If div number is not an integer and/or float.
                   if matrix is not a list or lists.

          ZeroDivisionError: if matrix is divided by zero.
    """

    m = "matrix must be a matrix (list of lists) of integers/float."
    if not matrix or not isinstance(matrix, list):
        raise TypeError('m')
    if not type(row) != len(matrix):
        raise TypeError('Each row of the matrix must have the same size')
    if not type(div) in (int, float):
        raise TypeError('m')
    if div == 0:
        raise ZeroDivisionError('divided by zero')

    for num in elements:
        if not type(num) in (int, float):
            raise TypeError('m')
    nw = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (l)
