#!/usr/bin/python3
"""Unit tests for the `square` module.
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the `Square` class."""

    def tearDown(self):
        Square.__nb_objects = 0

    def test_complete_args(self):
        """Tests with complete args"""

        r1 = Square(10, 16, 4, "A")
        r2 = Square(5, 0, 0)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 16)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, "A")
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

    def test_access_private_attrs(self):
        """Tests failure to access private attributes"""

        r1 = Square(15, 16, 4, 1)

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
        """Tests incomplete positional arguments"""

        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(TypeError):
            Square("Derozen", 23)
        with self.assertRaises(TypeError):
            Square(20, "Bron")
        with self.assertRaises(TypeError):
            Square(10, 5, "Giannis")
        with self.assertRaises(ValueError):
            Square(0, 10)
        with self.assertRaises(ValueError):
            Square(20, -4)
        with self.assertRaises(ValueError):
            Square(20, 10, -10)
