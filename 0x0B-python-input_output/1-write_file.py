#!/usr/bin/python3
""" A module that writes to a file"""


def write_file(filename="", text=""):
    """ Function that writes string to a file"""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
