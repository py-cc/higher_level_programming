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
