#!/usr/bin/python3
""" A module that creates an object from JSON file"""
import json


def load_from_json_file(filename):
    """ A function that creates an object from JSON file"""
    with open(filename) as file:
        return json.load(file)
