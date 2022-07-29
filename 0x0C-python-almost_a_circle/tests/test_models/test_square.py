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

    def test_update_square(self):
        """Tests updating a `Square` instance dynamically."""

        sqr = Square(20)
        sqr.update(15, 10, 3, 2)
        self.assertEqual(sqr.id, 15)
        self.assertEqual(sqr.width, 10)
        self.assertEqual(sqr.height, 10)
        self.assertEqual(sqr.x, 3)
        self.assertEqual(sqr.y, 2)

        sqr.update(2, 10, 4, 1)
        self.assertEqual(sqr.id, 2)
        self.assertEqual(sqr.width, 10)
        self.assertEqual(sqr.height, 10)
        self.assertEqual(sqr.x, 4)
        self.assertEqual(sqr.y, 1)

        sqr.update(size=30)
        self.assertEqual(sqr.width, 30)
        self.assertEqual(sqr.height, 30)

        sqr.update(x=3, y=1)
        self.assertEqual(sqr.x, 3)
        self.assertEqual(sqr.y, 1)

        sqr.update(5, 15, x=4, y=2)
        self.assertEqual(sqr.id, 5)
        self.assertEqual(sqr.width, 15)
        self.assertEqual(sqr.height, 15)
        self.assertEqual(sqr.x, 3)
        self.assertEqual(sqr.y, 1)

    def test_failing_update_square(self):
        """Tests failing cases for updating a `Square`
        instance dynamically."""

        sqr = Square(1, 4)

        with self.assertRaises(ValueError):
            sqr.update(2, 0)
        with self.assertRaises(ValueError):
            sqr.update(2, 20, -5)
        with self.assertRaises(ValueError):
            sqr.update(2, 20, 10, -2)
        with self.assertRaises(TypeError):
            sqr.update(2, "wardell")
        with self.assertRaises(TypeError):
            sqr.update(2, 25, "wardell")
        with self.assertRaises(TypeError):
            sqr.update(2, 25, 10, "wardell")
        sqr.update(25, 15, x=4, y=2)
        with self.assertRaises(AssertionError):
            self.assertEqual(sqr.x, 4)
            self.assertEqual(sqr.y, 2)

    def test_rect_to_dict(self):
        """Tests building the dictionary representation of a `Square.`"""

        s1 = Square(10, 2, 1, 9)
        s2 = Square(10)
        self.assertDictEqual(
            s1.to_dictionary(), {'id': 9, 'x': 2, 'size': 10, 'y': 1})
        self.assertDictEqual(
            s2.to_dictionary(), {'id': 33, 'x': 0, 'size': 10, 'y': 0})

        s1 = Square(10, 2, 1)
        s1_dict = s1.to_dictionary()
        self.assertIsInstance(s1_dict, dict)

        s2 = Square(1, 1)
        s2.update(**s1_dict)
        self.assertDictEqual(s1_dict, s2.to_dictionary())

    def test_to_json(self):
        """Tests serializing a dictionary to JSON using `to_dictionary()`."""

        s1 = Square(10, 7, 2, 8)
        dict1 = s1.to_dictionary()
        json_dict = Square.to_json_string([dict1])
        self.assertIsInstance(dict1, dict)
        self.assertIsInstance(json_dict, str)
