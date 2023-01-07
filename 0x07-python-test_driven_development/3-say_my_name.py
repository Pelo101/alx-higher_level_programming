#!/usr/bin/python3
"""

This module prints a first name and surnanme


"""


def say_my_name(first_name, last_name=""):
    """
  This function prints My name is <first name> <last name>

    Args:
        first_name: first name

        last_name: last name

    Returns:

         none

    Raises:

        TypeError: if first_name and last_name are not strings.

    """


if type(first_name) is not str:
    raise TypeError("first_name must be string")
if type(last_name) is not str:
    raise TypeError("last_name must be string")

print("My name is {} {}".format(first_name, last_name))
