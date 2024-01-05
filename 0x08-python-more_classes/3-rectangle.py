#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Rep a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Init a new Rectangle.

        Parameters:
            width (int): The width
            height (int): The height.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """get area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """get the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable rep of the rectangle.

        Represents the rectangle as # character.
        """

        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
