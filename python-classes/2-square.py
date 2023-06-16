#!/usr/bin/python3
""" Class Square that defines a square """


class Square():
    """class initialization"""
    def __init__(self, size=0):
        """ Definition with private instance attribute size
        which is assigned with the double underscore before given name"""

        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
