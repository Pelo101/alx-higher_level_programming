#!/usr/bin/python3
""" A module that defines a square """


class Square:
    """ A class that defines a square (based on 1-square.py) """
    def __init__(self, size=0):

        self.__size = size

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
