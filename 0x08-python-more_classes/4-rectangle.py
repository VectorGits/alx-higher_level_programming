#!/usr/bin/python3
"""
Rectangle
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """Initializes a new rectangle

        Args:
            width (int): the width of the new rectangle
            height (int): the height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set/Get the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Set/Get the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return (("#" * self.__width + '\n') * self.__height)[:-1]

    def __repr__(self):
        """Returns a str that can be used to create the object"""
        return "Rectangle({}, {})". format(self.__width, self.__height)
