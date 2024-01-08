#!/usr/bin/python3

"""
Module contains class that avoids dynamically created attributes
"""


class LockedClass:
    slots = ['first_name']

    def __init__(self):
        """Init method"""
        pass
