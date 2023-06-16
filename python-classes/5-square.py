#!/usr/bin/python3
""" Class Square that defines a square """


class Square:
    """ class initialization """
    def __init__(self, size=0):
        """ Definition with private instance attribute size
        which is assigned with the double underscore before given name """

        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """ size definition to retrieve (getter)
        A method used for getting a value is decorated with @property """
        return self.__size

    @size.setter
    def size(self, value):
        """ size definition to setter the data, now size will be equal to value
        A method that function as the setter is decorated with @ .setter """
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        """ Public instance method that prints in stdout
        the square with the character #
        """
        for i in range(self.size):
            for s in range(self.size):
                print("#", end="")
            print("")

        if self.size is 0:
            print("")
