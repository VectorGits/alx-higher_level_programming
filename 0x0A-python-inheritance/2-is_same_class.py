#!/usr/bin/python3
"""Module contains a function that returns True if the object is exactly an
"""


def is_same_class(obj, a_class):
    """Function returns True if the object is exactly an instance of the
    specified class; otherwise False.

    Args:
        obj: object to check
        a_class: class to check against

    Returns:
        True if the object is exactly an instance of the specified class;
        otherwise False.

    """
    return type(obj) == a_class
