#!/usr/bin/python3
"""square """


class Square:
    """Represents a square with a given size."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): The length of the square's sides.
            Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = 0  # Initialize with default value
        self.size = size  # Use the setter method to validate and set the size
        self.__position = (0, 0)
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The length of the square's sides.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new length of the square's sides.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If value contains non-positive integers.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple")
        elif len(value) != 2 or not all(isinstance(i, int) and
                                        i >= 0 for i in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Prints a square of '#' characters.

        Each side of the square has a length equal to the size of the square.

        Returns:
            None
        """
        for _ in range(self.__size):
            if self.__position[1] <= 0:
                print(" " * self.__position[0], end="")
            print("#" * self.__size)
        if self.__size == 0:
            print()
