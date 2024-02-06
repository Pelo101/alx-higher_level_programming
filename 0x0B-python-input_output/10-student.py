#!/usr/bin/python3
""" A module that defines a student class"""


class Student:
    """ A class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """ instantiation of a class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of student"""
        if attrs is None:

            return self.__dict__

        else:
            return {attr: getattr(self, attr, None) for attr in attrs}
