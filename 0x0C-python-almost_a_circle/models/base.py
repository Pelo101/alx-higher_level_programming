#!/usr/bin/python3
""" A module that manages the id attributes for all classes"""
import json


class Base:
    """ A class that manages the id attributes for classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """instatination of a class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns json string representation of list_dictionaries"""

        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
