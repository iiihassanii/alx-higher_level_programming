#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    # Base object is created successfully with default id value
    def test_default_id_value(self):
        obj = Base()
        assert obj.id == 1

        # Base object is created successfully with custom id value
    def test_custom_id_value(self):
        obj = Base(10)
        assert obj.id == 10

        # Multiple Base objects are created successfully with unique id values
    def test_unique_id_values(self):
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        assert obj1.id != obj2.id != obj3.id

        # Base object is created successfully with negative id value
    def test_negative_id_value(self):
        obj = Base(-5)
        assert obj.id == -5
