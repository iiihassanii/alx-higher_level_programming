#!/usr/bin/python3
"""class Student"""


class Student:
    """class Student"""
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """_summary_

        Args:
            first_name (_type_): _description_
            last_name (_type_): _description_
            age (_type_): _description_
        """
        Student.first_name = first_name
        Student.last_name = last_name
        Student.age = age

    def to_json(self):
        return Student.__dict__
