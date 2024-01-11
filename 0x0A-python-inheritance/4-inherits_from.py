#!/usr/bin/python3
"""Module contains a function that returns True if the object is an instance
of, or if the object is an instance of a class that inherited from, the
specified class; otherwise False.
"""


def inherits_from(obj, a_class):
    """Function returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class;
    otherwise False.

    Args:
        obj: object to check
        a_class: class to check against

    Returns:
        True if the object is an instance of, or if the object is an instance
        of a class that inherited from, the specified class; otherwise False.

    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
