#!/usr/bin/python3
""" Module that refers to a function that lists attributes
    of classes and instances"""


def lookup(obj):
    """ Function that returns the list of available attributes"""

    return(dir(obj))
