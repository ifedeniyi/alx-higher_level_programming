#!/usr/bin/python3
"""Unit tests for the `base` module.
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the `Base` class."""

    def test_no_param(self):
        """Testing `Base` class with no arguments."""

        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        with self.assertRaises(AttributeError):
            type(self.b2).nb_objects
        with self.assertRaises(AttributeError):
            type(self.b2).__nb_objects

    def test_param(self):
        """Testing `Base` class with numeric arguments."""

        a1 = Base(12)
        a2 = Base(7)
        self.assertEqual(a1.id, 12)
        self.assertEqual(a2.id, 7)

    def test_string_param(self):
        """Testing `Base` class with alphanum arguments."""

        c1 = Base("wendigo")
        c2 = Base("djinn")
        self.assertEqual(c1.id, "wendigo")
        self.assertEqual(c2.id, "djinn")

    def test_object_param(self):
        """Testing `Base` class with object arguments."""

        d1 = Base(["wendigo", 34, (3, 4)])
        d2 = Base(("x", "y"))
        self.assertEqual(d1.id, ["wendigo", 34, (3, 4)])
        self.assertEqual(d2.id, ("x", "y"))

    def test_invalid_param(self):
        """Testing `Base` class with excess arguments."""

        with self.assertRaises(TypeError):
            e1 = Base(4, 16)
        with self.assertRaises(TypeError):
            e2 = Base(5, 25)
