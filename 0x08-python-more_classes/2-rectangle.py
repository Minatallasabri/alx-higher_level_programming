#!/usr/bin/python3
"""implement a new class"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """init method

        Args:
            width (int): the width
            height (int): the height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width
        """
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
        """ Get/set the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area method"""
        return (self.__height * self.__width)

    def perimeter(self):
        """ perimeter method
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))
