#!/usr/bin/python3
"""This module defines a Rectangle"""


class Rectangle:

    """ This class defines objects of a rectangle """


def __init__(self, width=0, height=0):

    """This function defines a Rectangle
    Args:
        width: width of rectangle
        heigth: height of rectangle
    Returns: None
    Raises:
            ValueError: If height and width are not >= 0
            TypeError:  If height and width are not integers.
    """

    self.width = width
    self.height = height


@property
def width(self):

    """defines the width of a rectangle"""
    return self.__width


@width.setter
def width(self, value):

    """sets the value of the width
       Args:
           width: width of the rectangle
           value: value of width

       Raises:
              TypeError : If width is not an integer.
              ValueError: if width >= 0.
    """


if not isinstance(width, int):
    raise TypeError("width must be an integer")
if width > 0:

    raise ValueError("width must be >= 0")
    self.__width = value


@property
def height(self):

    """Function defines height of a rectangle"""
    return self.__height


@height.setter
def height(self, value):

    """Function sets the value of height.
          Args:
              height: height of the rectangle
              value : value of height
           Raises:
                 TypeError: if height is not an integer.
                 ValueError: if height is >= 0.
    """


if not isinstance(height, int):
    raise TypeError("height must be an integer")
if height > 0:
    raise ValueError("height must be >= 0")
    self.__height = value
