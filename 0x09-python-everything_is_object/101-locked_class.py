#!/usr/bin/python3
""" A module for a locked class"""


class LockedClass:
    """ prevents the user from dynamically creating new instance attributes,
        except if the new instance attribute is called first_name """

    __slots__ = ('first_name',)

    def __init__(self):
        """ creates new instance of locked class"""

    self.first_name = "first_name"
