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

    def to_json(self, attrs=None):
        """_summary_

            Args:
                attrs (_type_, optional): _description_. Defaults to None.

            Returns:
                _type_: _description_
            """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json_data):
        """_summary_

        Args:
            json_data (_type_): _description_
        """
        for attr, value in json_data.items():
            setattr(self, attr, value)
