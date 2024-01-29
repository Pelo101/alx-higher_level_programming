#!/usr/bin/python3
""" A module that defines a Rectangle """


class Rectangle:
    """ A class that defines a Rectangle """
    def __init__(self, width=0, height=0):
        """ Instantiation of the class """
        self._width = width
        self. height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):

        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('with must be >= 0')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must >= 0')
        self._height = value
