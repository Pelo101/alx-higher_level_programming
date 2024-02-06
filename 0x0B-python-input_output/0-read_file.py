#!/usr/bin/python3
""" Module that reads a file"""


def read_file(filename=""):
    """ A function that reads a file"""

    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
