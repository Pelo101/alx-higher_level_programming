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

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []

        file_name = cls.__name__ + ".json"
        json_string = cls.to_json_string(
                [obj.to_dictionary()for obj in list_objs]
                )

        with open(file_name, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance"""
        dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance
