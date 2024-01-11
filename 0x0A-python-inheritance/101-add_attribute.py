#!/usr/bin/python3
""" Module that defines a function add_attribute """


def add_attribute(obj, name, value):
    """ Function that adds a new attribute to an object if it’s possible

    Args:
        obj: object to add the attribute to
        name: name of the attribute
        value: value of the attribute

    Raises:
        TypeError: if the attribute cannot be added

    """

    if isinstance(obj, (int, str, float, list, dict, set, tuple, bool, type(None))):
        raise TypeError("can't add new attribute")
    if hasattr(obj, '__slots__') and name not in obj.__slots__:
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
