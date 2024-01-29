#!/usr/bin/python3
""" A module that defines a Rectangle """


class Rectangle:
    """ A class that defines a Rectangle """
    def __init__(self, width=0, height=0):
        """ Instantiation of the class """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property to return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter to set the width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ Property to retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter to set the height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must >= 0')
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return(self.__width * self.__height)

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """ Prints the rectangle with character #"""
        if self.__width == 0 or self.__height == 0:
            print("")
        return("#" * self.__width + "\n") * self.__height
