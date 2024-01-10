#!/usr/bin/python3
"""Module contains a function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """Function that creates an Object from a JSON file

    Arguments:
        filename (str): filename to read from

    Returns:
        obj: object represented by JSON string
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
