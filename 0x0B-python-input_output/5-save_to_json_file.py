#!/usr/bin/python3
"""Module contains a function that writes an
Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file,
    using a JSON representation

    Arguments:
        my_obj (obj): object to be converted to JSON
        filename (str): filename to write to
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
