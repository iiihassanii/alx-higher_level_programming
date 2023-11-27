#!/usr/bin/python3
"""_summary_
        """


class Rectangle:
    """_summary_
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """_summary_

        Args:
            width (int, optional): _description_. Defaults to 0.
            height (int, optional): _description_. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.width == 0 or self.height == 0:
            return ''

        rectangle = ''
        for _ in range(self.height):
            for i in range(self.width):
                rectangle += str(self.print_symbol)
            rectangle += '\n'
        rectangle = rectangle[:-1]
        return rectangle

    def __repr__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """delete
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """_summary_

        Args:
            rect_1 (_type_): _description_
            rect_2 (_type_): _description_

        Raises:
            TypeError: _description_
            TypeError: _description_

        Returns:
            _type_: _description_
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.area()
        area2 = rect_2.area()
        if area1 >= area2:
            return rect_1
        if area1 < area2:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """_summary_

        Args:
            size (int, optional): _description_. Defaults to 0.

        Returns:
            _type_: _description_
        """
        return cls(size, size)
