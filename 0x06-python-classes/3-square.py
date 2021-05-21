#!/usr/bin/python3

""" File with class Square """


class Square:
    """Class Square"""

    def __init__(self, size=0):
        """ __init__ constructor method"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ area returns the current square area """
        return self.__size ** 2
