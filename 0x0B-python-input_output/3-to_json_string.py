#!/usr/bin/python3
"""Module contains a function that returns the JSON representation of an object (string)"""
import json



def to_json_string(my_obj):
    """Function that returns the JSON representation of an object (string)
    
    Arguments:
        my_obj (str): object to be converted to JSON
    
    Returns:
        str: JSON representation of the object
    """

    return json.dumps(my_obj)
