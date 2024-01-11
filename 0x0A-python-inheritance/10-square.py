#!/usr/bin/python3
""" Module that defines a class BaseGeometry """


class BaseGeometry:
    """ Class that defines the attributes of Geometric Shapes """

    def area(self):
        """ Method that defines the area of a geomtric shape """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method that recieves the value property

        Árgs:
            name: name of the object
            value: value of the property

        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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

    def __str__(self):
        """ Method that returns the string representation of the object """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """ Method that returns the area of the object """
        return self.__width * self.__height


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
