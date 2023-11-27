#!/usr/bin/python3
"""_summary_
        """


class Rectangle:
    """_summary_
    """

    def __init__(self, width=0, height=0):
        """_summary_

        Args:
            width (int, optional): _description_. Defaults to 0.
            height (int, optional): _description_. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__width

    @width.setter
    def width(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__height

    @height.setter
    def height(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__height * self.__width

    def perimeter(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        rectangle_str = ''

        for _ in range(self.__height):
            rectangle_str += '#' * self.__width + '\n'
        return rectangle_str
