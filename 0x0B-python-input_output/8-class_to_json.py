#!/usr/bin/python3
""" A module that converts object attribute to dictionary"""


def class_to_json(obj):
    """ function that converts object to attribute dictionary"""

    return obj.__dict__
