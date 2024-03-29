#!/usr/bin/python3
"""Module for Student class"""


class Student:
    """Class for jsonification"""

    def __init__(self, first_name, last_name, age):
        """Initialization of Student object

        Args:
            first_name (str): first name of student
            last_name (str): last name of student
            age (int): age of student

        Returns: None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dictionary representation of Student instance"""
        return self.__dict__
