#!/usr/bin/python3
"""Defining Square Class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the class."""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Returns [Square] (<id>) <x>/<y> - <width>/<height>."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ Get the size."""
        return self.width

    @size.setter
    def size(self, value):
        """ Set size. """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the class Square by adding a public method."""
        atts = ["id", "size", "x", "y"]
        if len(args) > 0:
            [setattr(self, a, b) for a, b in zip(atts, args)]
        else:
            [setattr(self, a, b) for a, b in kwargs.items()]

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
