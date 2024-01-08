#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    if matrix is None:
        matrix = [[]]

    for row in matrix:
        for i, element in enumerate(row):
            if i != 0:
                print(" ", end="")
            print("{:d}".format(element), end="")
        print()
