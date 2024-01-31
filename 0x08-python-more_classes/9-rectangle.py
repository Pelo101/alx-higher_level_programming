#!/usr/bin/python3
""" A module that defines a Rectangle """


class Rectangle:
    """ A class that defines a Rectangle """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Instantiation of the class """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """ Prints the rectangle with character #"""
        empty_string = ""

        if self.__width == 0 or self.__height == 0:
            return (empty_string)
        return (
            ((str(self.print_symbol) * self.__width) + "\n") * self.__height
            )[:-1]

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """ A method  returns the biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area1 = rect_1.area()
        area2 = rect_2.area()

        if area2 <= area1:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ A method to create a square """
        return cls(size, size)
