#!/usr/bin/python3
"""class Student"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """_summary_

        Args:
            first_name (_type_): _description_
            last_name (_type_): _description_
            age (_type_): _description_
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return Student.__dict__
