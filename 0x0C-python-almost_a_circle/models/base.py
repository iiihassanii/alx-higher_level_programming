#!/usr/bin/python3
"""This module provides a base class with file I/O functionality."""

import json
import csv


class Base:
    """Base class for file I/O operations."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance.

        Args:
            id (int, optional): The ID of the instance. Defaults to None.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def from_json_string(json_string):
        """Deserialize a JSON string into a Python object.

        Args:
            json_string (str): The JSON string.

        Returns:
            The deserialized Python object.
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @staticmethod
    def to_json_string(my_obj):
        """Serialize a Python object into a JSON string.

        Args:
            my_obj: The Python object to be serialized.

        Returns:
            str: The JSON string representation of the object.
        """
        if my_obj is None or not my_obj:
            return "[]"
        return json.dumps(my_obj)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a JSON file.

        Args:
            list_objs (list): The list of objects to be saved.
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as file:
            if list_objs is None or not list_objs:
                file.write('[]')
            else:
                list_dicts = [item.to_dictionary() for item in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @classmethod
    def load_from_file(cls):
        """Load objects from a JSON file.

        Returns:
            list: The list of loaded objects.
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as file:
                list_dicts = Base.from_json_string(file.read())
                return [cls.create(**dict) for dict in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Create a new instance of the class.

        Args:
            dictionary: The attributes of the instance.

        Returns:
            The new instance.
        """
        dummy = None
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of objects to a CSV file.

        Args:
            list_objs (list): The list of objects to be saved.
        """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write('[]')
            else:
                list_dict = [item.to_dictionary() for item in list_objs]
                # Write the list_dict to the file using the csv module

    @classmethod
    def load_from_file_csv(cls):
        """Load objects from a CSV file.

        Returns:
            list: The list of loaded objects.
        """
        try:
            filename = "{}.csv".format(cls.__name__)
            with open(filename, 'r') as file:
                csv_reader = csv.DictReader(file)
                data = [row for row in csv_reader]
            return data
        except FileNotFoundError:
            return []
