#!/usr/bin/python3
"""_summary_"""


def print_square(size):
    """_summary_

    Args:
        size (_type_): _description_

    Raises:
        TypeError: _description_
        ValueError: _description_
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        print("#" * size)
    print()
