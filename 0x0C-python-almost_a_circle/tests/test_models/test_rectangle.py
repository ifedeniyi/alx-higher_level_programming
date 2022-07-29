#!/usr/bin/python3
"""Unit tests for the `rectangle` module.
"""
import io
import unittest
import contextlib
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the `Rectangle` class."""

    def test_complete_args(self):
        """Tests with complete args"""

        r1 = Rectangle(10, 5, 16, 4, "A")
        r2 = Rectangle(10, 5, 0, 0)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 16)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, "A")
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

    def test_access_private_attrs(self):
        """Tests failure to access private attributes"""

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
        """Tests incomplete positional arguments"""

        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(20)
        with self.assertRaises(TypeError):
            Rectangle("Derozen", 23)
        with self.assertRaises(TypeError):
            Rectangle(20, "Bron")
        with self.assertRaises(TypeError):
            Rectangle(20, 10, "Kawhi")
        with self.assertRaises(TypeError):
            Rectangle(20, 10, 5, "Giannis")
        with self.assertRaises(ValueError):
            Rectangle(0, 10)
        with self.assertRaises(ValueError):
            Rectangle(20, -4)
        with self.assertRaises(ValueError):
            Rectangle(20, 10, -10)
        with self.assertRaises(ValueError):
            Rectangle(20, 10, 10, -20)

    def test_rectangle_area(self):
        """Tests computing the area of a `Rectangle` instance,
        using the `area()` public method."""

        rect1 = Rectangle(20, 10)
        rect2 = Rectangle(20, 1)
        rect3 = Rectangle(ord('a'), ord('b'))
        self.assertEqual(rect1.area(), 200)
        self.assertEqual(rect2.area(), 20)
        self.assertEqual(rect3.area(), (ord('a') * ord('b')))

    def test_rectangle_display(self):
        """Tests printing to stdout the `Rectangle` instance
        with the character `#`."""

        rect1 = Rectangle(2, 4)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            rect1.display()

        self.assertEqual(f.getvalue(), "##\n##\n##\n##\n")
