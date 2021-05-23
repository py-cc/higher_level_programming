#!/usr/bin/python3
""" Module that define a class rectangle """


class Rectangle:

    """ Class that defines a rectangle """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Init method to initialized a instance"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            line = str(self.print_symbol) * self.width
            rectangle = (line + '\n') * (self.height - 1) + line
        return rectangle

    def __repr__(self):
        """ Method that returns a rectangle by # character """
        repr_t = "Rectangle({}, {})".format(
            self.width, self.height)
        return repr_t

    def __del__(self):
        """ Method that deletes a object """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Method compare areas between rectangles."""
        if isinstance(rect_1, Rectangle) is not True:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if isinstance(rect_2, Rectangle) is not True:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ Method to manage a square """
        return cls(size, size)
