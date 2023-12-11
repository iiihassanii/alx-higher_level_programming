#!/usr/bin/python3
"""_summary_
        """

import unittest
from models.base import Base
import json
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    """__init__ test"""
    # Base object is created successfully with default id value

    # Base object is created successfully with custom id value
    def test_custom_id_value(self):
        """_summary_
        """
        obj = Base(10)
        assert obj.id == 10

        # Multiple Base objects are created successfully with unique id values
    def test_unique_id_values(self):
        """_summary_
        """
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        assert obj1.id != obj2.id != obj3.id

        # Base object is created successfully with negative id value
    def test_negative_id_value(self):
        """_summary_
        """
        obj = Base(-5)
        assert obj.id == -5

    # Initializes an instance of the Base class with no arguments
    def test_init_with_no_arguments(self):
        """_summary_
        """
        base = Base(0)
        assert base.id == 0

    # Initializes an instance of the Base class with an ID argument
    def test_init_with_id_argument(self):
        """_summary_
        """
        base = Base(5)
        assert base.id == 5

    # Initializes multiple instances of
    def test_init_with_different_id_arguments(self):
        """_summary_
        """
        base1 = Base(1)
        base2 = Base(2)
        base3 = Base(3)
        assert base1.id == 1
        assert base2.id == 2
        assert base3.id == 3

    # Initializes an instance of the Base class with ID argument as 0
    def test_init_with_zero_id_argument(self):
        """_summary_
        """
        base = Base(0)
        assert base.id == 0

    # Initializes an instance
    def test_init_with_negative_id_argument(self):
        """_summary_
        """
        base = Base(-5)
        assert base.id == -5

    # Initializes an instance of the Base class with ID argument as a float
    def test_init_with_float_id_argument(self):
        """_summary_
        """
        base = Base(3.14)
        assert base.id == 3.14

    """from_json_string Test"""
    # Returns an empty list when given a None input

    def test_returns_empty_list_with_none_input(self):
        """_summary_
        """
        # Arrange
        json_string = None

        # Act
        result = Base.from_json_string(json_string)

        # Assert
        assert result == []

    # Returns a Python object when given a valid JSON string input
    def test_valid_json_string_input(self):
        """_summary_
        """
        # Arrange
        json_string = '{"name": "John", "age": 30}'

        # Act
        result = Base.from_json_string(json_string)

        # Assert
        assert isinstance(result, dict)

    # Returns the correct Python object when
    # given a JSON string representing a list
    def test_returns__list(self):
        """_summary_
        """
        # Arrange
        json_string = '[1, 2, 3, 4, 5]'

        # Act
        result = Base.from_json_string(json_string)

        # Assert
        assert isinstance(result, list)
        assert result == [1, 2, 3, 4, 5]

    # Returns an empty list when given an empty string input
    def test_returns_empty_list(self):
        """_summary_
        """
        # Arrange
        json_string = ""

        # Act
        result = Base.from_json_string(json_string)

        # Assert
        assert result == []

    # Raises a JSONDecodeError when given an invalid JSON string input
    def test_invalid_json_string_input(self):
        """_summary_
        """
        # Arrange
        json_string = '{"name": "John", "age": 30,}'

        # Act and Assert
        with self.assertRaises(json.JSONDecodeError):
            Base.from_json_string(json_string)

    # Raises a TypeError when given a non-string input
    def test_raises_type_error_with_non_string_input(self):
        """_summary_
        """
        # Arrange
        json_string = 123

        # Act and Assert
        with self.assertRaises(TypeError):
            Base.from_json_string(json_string)

    # Returns the correct Python object
    # when given a JSON string representing a dictionary
    def test_returns_correct_object_with_dictionary_input(self):
        """_summary_
        """
        # Arrange
        json_string = '{"name": "John", "age": 30}'

        # Act
        result = Base.from_json_string(json_string)

        # Assert
        assert result == {"name": "John", "age": 30}

    # Returns the correct Python object when
    # given a JSON string representing a nested dictionary
    def test_returns_correct_object_with_nested_dictionary_input(self):
        """_summary_
        """
        # Arrange
        json_string = '{"person": {"name": "John", "age": 30}}'

        # Act
        result = Base.from_json_string(json_string)

        # Assert
        assert result == {"person": {"name": "John", "age": 30}}

    # Returns the correct Python object when
    #  given a JSON string representing a list of dictionaries
    def test_returns_correct_object_with_list_of_dictionaries_input(self):
        """_summary_
        """
        # Arrange
        json_string = '[{"name": "John", "age": 30}\
            , {"name": "Jane", "age": 25}]'

        # Act
        result = Base.from_json_string(json_string)

        # Assert
        assert result == [{"name": "John", "age": 30},
                          {"name": "Jane", "age": 25}]

    """to_json_string tests"""

    # Returns an empty list as a JSON string when given an empty list.
    def test_empty_list(self):
        """_summary_
        """
        # Arrange
        my_obj = []

        # Act
        result = Base.to_json_string(my_obj)

        # Assert
        assert result == "[]"

    # Returns a JSON string representation of the given Python object.
    def test_python_object(self):
        """_summary_
        """
        # Arrange
        my_obj = {"name": "John", "age": 30}

        # Act
        result = Base.to_json_string(my_obj)

        # Assert
        assert result == '{"name": "John", "age": 30}'

    # Returns an empty list as a JSON string when given None.
    def test_none(self):
        """_summary_
        """
        # Arrange
        my_obj = None

        # Act
        result = Base.to_json_string(my_obj)

        # Assert
        assert result == "[]"

    # Returns an empty list as a JSON string
    # when given an empty string.
    def test_empty_string(self):
        """_summary_
        """
        # Arrange
        my_obj = ""

        # Act
        result = Base.to_json_string(my_obj)

        # Assert
        assert result == "[]"

    # Returns a JSON string representation
    # of a list of dictionaries.

    # Returns a JSON string representation of a list of integers.

    def test_list_of_integers(self):
        """_summary_
        """
        # Arrange
        my_obj = [1, 2, 3, 4, 5]

        # Act
        result = Base.to_json_string(my_obj)

        # Assert
        assert result == '[1, 2, 3, 4, 5]'

    """save_to_file tests"""
    # If list_objs is an empty list, writes an empty list to the file.

    def test_save_to_file_write_empty_list_if_list_objs_is_empty(self):
        """_summary_
        """
        # Arrange
        list_objs = []

        # Act
        Base.save_to_file(list_objs)

        # Assert
        with open("Base.json", "r") as file:
            data = file.read()
            assert data == '[]'

    # If an object in list_objs does not
    # have a to_dictionary method, raises an AttributeError.

    def test_save_to_file_dictionary_method(self):
        """_summary_
        """
        # Arrange
        class CustomObject:
            def __init__(self, id):
                self.id = id

        obj1 = Base(1)
        obj2 = CustomObject(2)
        list_objs = [obj1, obj2]

        # Act and Assert
        with self.assertRaises(AttributeError):
            Base.save_to_file(list_objs)

    """load_from_file test"""
    # Loads a list of objects from a JSON file and returns it
    # Returns an empty list if the file does not exist

    def test_load_from_file_empty_list_if_file_not_exist(self):
        """_summary_
        """
        # Initialize the class object
        obj = Base()

        # Load objects from a non-existent JSON file
        loaded_list = obj.load_from_file()

        # Check if the loaded list is an empty list
        assert loaded_list == []

    # Returns an empty list if the file is empty
    def test_load_from_file_empty_list_if_file_empty(self):
        """_summary_
        """
        # Initialize the class object
        obj = Base()

        # Create an empty JSON file
        with open("Base.json", "w") as file:
            file.write("")

        # Load objects from the empty JSON file
        loaded_list = obj.load_from_file()

        # Check if the loaded list is an empty list
        assert loaded_list == []

    # Raises an exception if the file is not in JSON format
    def test_load_from_file_raises_exception_if_file_not_json(self):
        """_summary_
        """
        # Initialize the class object
        obj = Base()

        # Create a non-JSON file
        with open("Base.txt", "w") as file:
            file.write("This is not a JSON file")

        # Check if loading objects from the non-JSON file raises an exception
        with self.assertRaises(json.JSONDecodeError):
            obj.load_from_file()

    # Raises an exception if the file contains invalid JSON
    def test_load_from_file_raises_exception_if_file_invalid_json(self):
        """_summary_
        """
        # Initialize the class object
        obj = Base()

        # Create a JSON file with invalid JSON
        with open("Base.json", "w") as file:
            file.write("{invalid_json}")

        # Check if loading objects from the JSON
        #  file with invalid JSON raises an exception
        with self.assertRaises(json.JSONDecodeError):
            obj.load_from_file()

    # Raises an exception if the list of objects in the file is not a list
    def test_load_from_file_raises_exception_if_list_not_list(self):
        """_summary_
        """
        # Initialize the class object
        obj = Base()

        # Create a JSON file with a non-list object
        with open("Base.json", "w") as file:
            file.write('{"id": 1}')

        # Check if loading objects from the JSON
        #  file with a non-list object raises an exception
        with self.assertRaises(TypeError):
            obj.load_from_file()

    def test_id(self):
        """
            Initialise an instance with id > 0
        """
        b = Base(12)
        self.assertEqual(12, b.id)

    def test_id_zero(self):
        """
            Initialise instance with id == 0
        """
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        """
            Initialise instance with id < 0
        """
        b = Base(-2)
        self.assertEqual(-2, b.id)

    def test_id_string(self):
        """
            Intialise instance with id is string
        """
        b = Base("Base")
        self.assertEqual("Base", b.id)

    def test_id_list(self):
        """
            Initialise instance with id is list
        """
        b = Base([1, 3, 6])
        self.assertEqual([1, 3, 6], b.id)

    def test_id_tuple(self):
        """
            Initialise instance with id is tuple
        """
        b = Base((1, 3))
        self.assertEqual((1, 3), b.id)

    def test_id_dict(self):
        """
            Initialise instance with id is dict
        """
        b = Base({'id': 12})
        self.assertEqual({'id': 12}, b.id)

    def test_to_json_type(self):
        """
           test to_json type
        """
        sq = Square(9)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_to_json_value(self):
        """
             Test to json value (string)
        """
        sq = Square(1, 0, 0, 9)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string), [{"id": 9, "y": 0,
                                                    "size": 1, "x": 0}])

    def test_to_json_None(self):
        """
            test to json None
        """
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_empty(self):
        """
            test to_json Empty
        """
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_from_json_string(self):
        """
            test from json_string
        """
        sq = Square(1, 0, 0, 234)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        json_list = Base.from_json_string(json_string)
        self.assertEqual(json_list, [{'size': 1, 'x': 0, 'y': 0, 'id': 234}])

    def test_from_json_none(self):
        """
            Test from json none
        """
        json_list = Base.from_json_string(None)
        self.assertEqual(json_list, [])

    def test_from_json_empty(self):
        """
            test from json none
        """
        json_list = Base.from_json_string([])
        self.assertEqual(json_list, [])


class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def test_save_to_file_csv_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def test_save_to_file_csv_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def test_save_to_file__csv_cls_name(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file_csv([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("", f.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
