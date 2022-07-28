#!/usr/bin/python3
"""Unit tests for the `rectangle` module.
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the `Rectangle` class."""

    def test_complete_args(self):
        """Test with complete args"""

        r1 = Rectangle(10, 5, 16, 4, "A")
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 16)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, "A")

    def test_access_private_attrs(self):
        """Test failure to access private attributes"""

        r1 = Rectangle(10, 5, 16, 4, 1)

        with self.assertRaises(AttributeError):
            r1.__width
        with self.assertRaises(AttributeError):
            r1.__height
        with self.assertRaises(AttributeError):
            r1.__x
        with self.assertRaises(AttributeError):
            r1.__y
        with self.assertRaises(AttributeError):
            r1.__nb_objects

    def test_invalid_args(self):
        """Test incimplete positional arguments"""

        with self.assertRaises(TypeError):
            Rectangle()

        with self.assertRaises(TypeError):
            Rectangle(20)
