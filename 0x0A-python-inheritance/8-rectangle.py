#!/usr/bin/python3
""" Module that defines a class BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ Class that defines a Rectangle from BaseGeometry """

    def __init__(self, width, height):
        """ Method that initializes the class

        Args:
            width: width of the rectangle
            height: height of the rectangle

        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    # def __str__(self):
    #     """ Method that returns the string representation of the object """
    #     return "[Rectangle] {}/{}".format(self.__width, self.__height)

    # def area(self):
    #     """ Method that returns the area of the object """
    #     return self.__width * self.__height
