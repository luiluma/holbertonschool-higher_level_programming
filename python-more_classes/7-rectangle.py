#!/usr/bin/python3
""" Class Rectangle with private instances width and height
and public instances area and perimeter """


class Rectangle:
    """ class initialization """

    number_of_instances = 0
    """ public class attribute initialized in 0 """

    print_symbol = "#"
    """ Public class attribute used as any symbol for str representation """

    def __init__(self, width=0, height=0):
        """
        Definition with private instance attribute width and height """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width method to retrieve (getter)
        A method used for getting a value is decorated with @property """
        return self.__width

    @property
    def height(self):
        """ height method to retrieve (getter) """
        return self.__height

    @width.setter
    def width(self, value):

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ height method to set a new value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ public instance method area """
        return self.__width * self.__height

    def perimeter(self):
        """ public instance perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ definition of str representation """
        empty = ""
        if self.__width == 0 or self.__height == 0:
            return empty
        for h in range(self.__height):
            for w in range(self.__width):
                empty = empty + str(self.print_symbol)
            empty = empty + '\n'
        return empty[:-1]

    def __repr__(self):
        """ printable representation of Rectangle """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ destruction """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
