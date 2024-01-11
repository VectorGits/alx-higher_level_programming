#!/usr/bin/python3
""" Module that defines a class MyInt """


class MyInt(int):
    """ Class that defines a MyInt object """

    def __eq__(self, other):
        """ Method that overrides the equality operator """
        return super().__ne__(other)

    def __ne__(self, other):
        """ Method that overrides the inequality operator """
        return super().__eq__(other)
