#!/usr/bin/python3
""" A module that inherits from the Base class"""

from models.base import Base


class Rectangle(Base):
    """ A class that manages the id attribute inherited from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ A instantiation of a class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def x(self):
        """attribute of a rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """attribute of a rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """returns the area of the Rectangle"""
        return self.__height * self.__width

    def display(self):
        """ displays the rectangle with # """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        return f"[Rectangle]({id(self)}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args):
        """assigns argument to each attribute"""

        attributes = ['id', 'width', 'height', 'x', 'y']
        for i, args in enumerate(args):
            setattr(self, attributes[i], args)



