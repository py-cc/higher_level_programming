#!/usr/bin/python3
"""Module that adds 2 integers"""


def add_integer(a, b=98):
    """ Function to add to integers or float variable

    Parameters:
    __________
        a : int or float value to add
        b : int or float value to add

    Return:
    _______
        Result to add of two values

    Raises:
    _______
        TypeError, if a and b are not int or float data types

    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
