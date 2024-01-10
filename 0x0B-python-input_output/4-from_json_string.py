#!.usr/bin/python3
"""Module contains a function that returns an object
(Python data structure) represented by a JSON string"""
import json


def from_json_string(my_str):
    """Function that returns an object (Python
    data structure) represented by a JSON string

    Arguments:
        my_str (str): JSON string to be converted to object

    Returns:
        obj: object represented by JSON string
    """

    return json.loads(my_str)
