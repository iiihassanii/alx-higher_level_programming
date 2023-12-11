#!/usr/bin/python3
"""square Class"""
from .rectangle import Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """_summary_

        Args:
            size (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.height)

    def update(self, *args, **kwargs):
        """_summary_
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    @property
    def size(self):
        """size
        """
        return self.width

    @size.setter
    def size(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        self.width = value
        self.height = value
