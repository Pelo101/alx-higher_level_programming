#!/usr/bin/python3
""" A module checks if object is an inherited  of class """


def inherits_from(obj, a_class):
    """ A function checks if an objet inherited from a class"""

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
