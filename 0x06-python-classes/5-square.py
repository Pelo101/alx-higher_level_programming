#!/usr/bin/python3
""" A module that defines a square"""


class Square:
    """ A class that defines a square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ A method to define size and retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ A method that returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """ A method that  prints in stdout the square with #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print('#' * self.__size)
