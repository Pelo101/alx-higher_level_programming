#!/usr/bin/python3
"""A module that defines a sqaure"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that creates a square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns the string representation of square"""

        return '[{}] ({}) {}/{} - {}' .\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Returns the size of the sqaure"""
        return self.width

    @size.setter
    def size(self, value):
        """Function that sets the attributes of square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns argument to each attribute"""
        attributes = ['id', 'size', 'x', 'y']

        for attr, value in zip(attributes, args):
            if value is not None:
                setattr(self, attr, value)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a rectangle"""

        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y

        }
