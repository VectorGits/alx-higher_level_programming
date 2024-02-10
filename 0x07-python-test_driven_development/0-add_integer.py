#!/usr/bin/python3
"""
This is the "add_integer" module.
"""


def add_integer(a, b=98):
    """Return the sum of two integers."""

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
