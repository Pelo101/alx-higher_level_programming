#!/usr/bin/python3
""" A module that defines a square """


class Square:
    """ A class that defines a square """
    def __init__(self, size=0):

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ A method that returns the current square area """
        return self.__size ** 2
