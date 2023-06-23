#!/usr/bin/python3
"""
This module have a empty class named Geometry
"""


class BaseGeometry:
    """Class description for Base Geometry"""

    def area(self):
        """Public instance method that raise an Exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Public instance method that validates value"""
        if not type(value) is int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
