#!/usr/bin/python3
""" A module that inherits from another class"""


class MyList(list):
    """ A class that inherits from the list class"""

    def print_sorted(self):

        print(sorted(self))
