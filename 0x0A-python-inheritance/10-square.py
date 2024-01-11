#!/usr/bin/python3
""" Module that defines a class BaseGeometry """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class that defines a Square from Rectangle """

    def __init__(self, size):
        """ Method that initializes the class

        Args:
            size: size of the square

        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ Method that returns the string representation of the object """
        return "[Square] {}/{}".format(self.__size, self.__size)
