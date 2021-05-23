#!/usr/bin/python3
""" Module that define a class rectangle """


class Rectangle:

    """ Class that defines a rectangle """

    def __init__(self, width=0, height=0):
        """ Init method to initialized a instance"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """ Method getter for height atributte"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Method setter for height atributte """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """ Method getter for width atributte"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Method setter for width atributte """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """ Method that calculates area of a rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Method that calculates perimeter of a rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        """ Method that returns a rectangle by # character """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            line = '#' * self.width
            rectangle = (line + '\n') * (self.height - 1) + line
        return rectangle

    def __repr__(self):
        """ Method that returns a rectangle by # character """
        repr_t = "Rectangle({}, {})".format(
            self.width, self.height)
        return repr_t

    def __del__(self):
        """ Method that deletes a object """
        print("Bye rectangle...")
