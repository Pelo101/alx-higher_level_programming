#!/usr/bin/python3
""" A module that returns an object as string representation"""
import json


def from_json_string(my_str):
    """ Function that returns a object as string rep"""

    return json.loads(my_str)
