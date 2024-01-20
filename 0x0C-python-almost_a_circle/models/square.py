#!/usr/bin/python3
""" Module that contains class Square,
inheritance of class Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor method """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ String representation of the object """
        return "[Square] ({}) {}/{} - {}".\
         format(self.id, self.x, self.y, self.width)
