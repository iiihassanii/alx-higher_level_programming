#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    # The function returns the maximum integer in a list of integers.

    def test_returns_max_integer(self):
        """_summary_
        """
        # Arrange
        lst = [1, 2, 3, 4, 5]

        # Act
        result = max_integer(lst)

        # Assert
        self.assertAlmostEqual(max_integer(lst), 5)

    # The function returns None if the list is empty.
    def test_returns_none_for_empty_list(self):
        """_summary_
        """
        # Arrange
        lst = []

        # Act
        result = max_integer(lst)

        # Assert
        self.assertAlmostEqual(max_integer(lst), None)

    # The function works correctly with a list of one integer.
    def test_returns_single_integer(self):
        """_summary_
        """
        # Arrange
        lst = [5]

        # Act
        result = max_integer(lst)

        # Assert
        self.assertAlmostEqual(max_integer(lst), 5)

    # The function works correctly with a list
    #  containing only the integer 0.
    def test_returns_zero_for_list_with_zero(self):
        """_summary_
        """
        # Arrange
        lst = [0]

        # Act
        result = max_integer(lst)

        # Assert
        self.assertAlmostEqual(max_integer(lst), 0)
    # The function works correctly with a list
    #  containing the maximum integer value.

    def test_returns_max_integer_value(self):
        """_summary_
        """
        # Arrange
        lst = [100, 200, 300, 400, 500]

        # Act
        result = max_integer(lst)

        # Assert
        self.assertAlmostEqual(max_integer(lst), 500)

    # The function works correctly with a list
    # containing the minimum integer value.
    def test_returns_min_integer_value(self):
        """_summary_
        """
        # Arrange
        lst = [-500, -400, -300, -200, -100]

        # Act
        result = max_integer(lst)

        # Assert
        self.assertAlmostEqual(max_integer(lst), -100)

        # The function works correctly with a
        #  list of multiple integers.
    def test_multiple_integers(self):
        """_summary_
        """
        # Arrange
        lst = [1, 2, 3, 4, 5]

        # Act
        result = max_integer(lst)

        # Assert
        self.assertAlmostEqual(max_integer(lst), 5)

    # The function works correctly with a list of negative integers.
    def test_negative_integers(self):
        """_summary_
        """
        # Arrange
        lst = [-5, -3, -1, -2, -4]

        # Act
        result = max_integer(lst)

        # Assert
        self.assertAlmostEqual(max_integer(lst), -1)

    # The function works correctly with a list of positive integers.
    def test_positive_integers(self):
        """_summary_
        """
        # Arrange
        lst = [10, 20, 30, 40, 50]

        # Act
        result = max_integer(lst)

        # Assert
        self.assertAlmostEqual(max_integer(lst), 50)

    # The function test non int input
    def test_non_int(self):
        """_summary_
        """
        self.assertRaises(TypeError, max_integer, True)

    # The function Test a list of strings.
    def test_list_of_strings(self):
        """_summary_
        """
        strings = ["say", "Hassan"]
        self.assertEqual(max_integer(strings), "say")


if __name__ == '__main__':
    unittest.main()
