#!/usr/bin/python3
"""Module for Rectangle class
"""


class Rectangle:
    """This class describes a rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Rectangle's width (int) """
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Rectangle's height (int) """
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ Rectangle area """
    def area(self):
        return (self.width * self.height)

    """ Rectangle perimeter """
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return (0)
        return ((2 * self.width) + (2 * self.height))

    """__str__ method to print the Rectangle"""
    def __str__(self):
        row = ""
        if self.height == 0 or self.width == 0:
            return (row)
        for i in range(self.height):
            for j in range(self.width):
                row += "#"
            row += "\n"
        row = row[0:-1]
        return (row)

    """rep method"""
    def __repr__(self):
        return ("Rectangle(" + str(self.width) + ", " + str(self.height) + ")")

    """__del__ method when an instance is deleted"""
    def __del__(self):
        print("Bye rectangle...")
