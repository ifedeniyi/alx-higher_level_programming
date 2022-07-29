#!/usr/bin/python3
"""Unit tests for the `rectangle` module.
"""
import io
import unittest
import contextlib
from models.rectangle import Rectangle
from models.base import Base


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

        rect = Rectangle(2, 4, 0, 0, 5)
        rect1 = Rectangle(5, 2)
        f = io.StringIO()
        f1 = io.StringIO()
        with contextlib.redirect_stdout(f):
            rect.display()
        self.assertEqual(f.getvalue(), "##\n##\n##\n##\n")
        with contextlib.redirect_stdout(f1):
            rect1.display()
        self.assertEqual(f1.getvalue(), "#####\n#####\n")
        f.close()
        f1.close()

    def test_rectangle_display_xy(self):
        """Tests printing to stdout the `Rectangle` instance
        with the character `#`."""

        rect = Rectangle(2, 4, 2, 2, 5)
        rect1 = Rectangle(5, 2, 1, 1)
        f = io.StringIO()
        f1 = io.StringIO()
        with contextlib.redirect_stdout(f):
            rect.display()
        self.assertEqual(f.getvalue(), "\n\n  ##\n  ##\n  ##\n  ##\n")
        with contextlib.redirect_stdout(f1):
            rect1.display()
        self.assertEqual(f1.getvalue(), "\n #####\n #####\n")
        f.close()
        f1.close()

    def test_rectangle_str(self):
        """Tests printing to stdout the `Rectangle` instance
        with `print()` and `str()`."""

        rect = Rectangle(2, 4, 0, 0, 5)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            print(rect)
        self.assertEqual(f.getvalue(), "[Rectangle] (5) 0/0 - 2/4\n")
        with contextlib.redirect_stdout(f):
            str(rect)
        self.assertEqual(f.getvalue(), "[Rectangle] (5) 0/0 - 2/4\n")
        f.close()

    def test_update_rectangle(self):
        """Tests updating a `Rectangle` instance dynamically."""

        rect = Rectangle(20, 4)
        rect.update(15, 10, 15, 8, 9)
        self.assertEqual(rect.id, 15)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 15)
        self.assertEqual(rect.x, 8)
        self.assertEqual(rect.y, 9)

        rect.update(2, 20, 10, 2, 2)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 20)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 2)

        rect.update(width=30, height=5)
        self.assertEqual(rect.width, 30)
        self.assertEqual(rect.height, 5)

        rect.update(x=3, y=1)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 1)

        rect.update(5, 15, 4, x=4, y=2)
        self.assertEqual(rect.id, 5)
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 1)

    def test_failing_update_rectangle(self):
        """Tests failing cases for updating a `Rectangle`
        instance dynamically."""

        rect = Rectangle(1, 4)

        with self.assertRaises(ValueError):
            rect.update(2, 0)
        with self.assertRaises(ValueError):
            rect.update(2, 20, -5)
        with self.assertRaises(ValueError):
            rect.update(2, 20, 10, -2)
        with self.assertRaises(ValueError):
            rect.update(2, 20, 10, 2, -1)
        with self.assertRaises(TypeError):
            rect.update(2, "wardell")
        with self.assertRaises(TypeError):
            rect.update(2, 25, "wardell")
        with self.assertRaises(TypeError):
            rect.update(2, 25, 10, "wardell")
        with self.assertRaises(TypeError):
            rect.update(2, 25, 10, 2, "wardell")
        rect.update(25, 15, x=4, y=2)
        with self.assertRaises(AssertionError):
            self.assertEqual(rect.x, 4)
            self.assertEqual(rect.y, 2)

    def test_rect_to_dict(self):
        """Test building the dictionary representation of a `Rectangle."""

        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(10, 20)
        self.assertDictEqual(
            r1.to_dictionary(), {
                'x': 1, 'y': 9, 'id': 14, 'height': 2, 'width': 10})
        self.assertDictEqual(
            r2.to_dictionary(), {
                'x': 0, 'y': 0, 'id': 15, 'height': 20, 'width': 10})
