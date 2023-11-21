#!/usr/bin/python3
"""square """


class Square:
    """Represents a square with a given size."""
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): The length of the square's sides.
            Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
