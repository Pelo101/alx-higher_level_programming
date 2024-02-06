#!/usr/bin/python3
""" A module that writes object to text file using json rep"""
import json


def save_to_json_file(my_obj, filename):
    """ A function that wries an object a json rep"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
