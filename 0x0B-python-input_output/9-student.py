#!/usr/bin/python3
""" A module that defines a student class"""


class Student:
    """ A class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """ instantiation of a class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of student"""

        return self.__dict__
