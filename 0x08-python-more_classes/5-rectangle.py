#!/usr/bin/python3
"""defines a new rectangle"""


class Rectangle:
    """Represents a class rectangle"""

    def __init__(self, width=0, height=0):
        """
        init a rectangle

        parameters:
            width (int): width of rectangle
            height (int): height of rectangle

        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """get width"""
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
        """get height"""
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
        """get perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
    def __str__(self):
        """Return the printable rep of the rect

        Represents the rectangle with # character
        """

        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
            return ("".join(rect))

        def __repr__(self):
            """Return the string rep of the Rectangle"""
            rect = "Rectangle(" + str(self.__width)
            rect += ", " + str(self.__height) + ")"

            return (rect)

        def __del__(self):
            """Print a message for every deletion of a Rectangle."""
            print("Bye rectangle...")
