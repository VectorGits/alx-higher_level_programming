#!/usr/bin/python3
"""Module contains a function that returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """Function returns the list of available attributes and methods of an
    object
    Args:
        obj (object): object to look up
    Returns:
        list: list of available attributes and methods
    """
    return dir(obj)
