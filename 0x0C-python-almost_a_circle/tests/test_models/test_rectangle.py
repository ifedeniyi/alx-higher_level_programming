#!/usr/bin/python3
"""Unit tests for the `rectangle` module.
"""
import io
import json
import os
import unittest
import contextlib
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the `Rectangle` class."""

    def tearDown(self):
        Rectangle.reset_obj_count()

    def test_complete_args(self):
        """Tests with complete args"""

        r1 = Rectangle(10, 5, 16, 4, "A")
        r2 = Rectangle(20, 10)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 16)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, "A")
        self.assertEqual(r2.width, 20)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 1)

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
                'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})
        self.assertDictEqual(
            r2.to_dictionary(), {
                'x': 0, 'y': 0, 'id': 2, 'height': 20, 'width': 10})

        r1 = Rectangle(10, 20, 1, 2)
        r1_dict = r1.to_dictionary()
        self.assertIsInstance(r1_dict, dict)

        r2 = Rectangle(5, 25)
        r2.update(**r1_dict)
        self.assertDictEqual(r1_dict, r2.to_dictionary())

    def test_to_json(self):
        """Tests serializing an object to JSON using `to_json_string()`."""

        r1 = Rectangle(10, 7, 2, 8)
        dict1 = r1.to_dictionary()
        json_dict = Rectangle.to_json_string([dict1])
        self.assertIsInstance(dict1, dict)
        self.assertIsInstance(json_dict, str)

    def test_from_json(self):
        """Tests deserializing an obj from JSON using `from_json_string()`."""

        r1 = Rectangle(10, 5, 7, 2, 8)
        dict1 = r1.to_dictionary()
        json_dict = Rectangle.to_json_string([dict1])
        self.assertIsInstance(dict1, dict)
        self.assertIsInstance(json_dict, str)
        self.assertEqual([dict1], Rectangle.from_json_string(json_dict))

    def test_save_to_file(self):
        """Tests saving a list of `Rectangle` instances to a JSON file."""

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as f:
            json_dict = json.load(f)

            self.assertEqual(
                json_dict, [r1.to_dictionary(), r2.to_dictionary()])
            self.assertNotEqual(json_dict, [r1.to_dictionary()])

        os.remove("Rectangle.json")

    def test_create_instance(self):
        """Tests dynamically creating new instance from a dictionary."""

        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        r2_dictionary = r2.to_dictionary()

        self.assertIsInstance(r2, Rectangle)
        self.assertEqual(r2.width, r1.width)
        self.assertEqual(r2.height, r1.height)
        self.assertEqual(r2.x, r1.x)
        self.assertEqual(r2.y, r1.y)
        self.assertEqual(r2.id, r1.id)
        self.assertDictEqual(r1_dictionary, r2_dictionary)

    def test_load_from_file(self):
        """Tests loading list of instances from JSON file and
        dynamically creating new instance from loaded list."""

        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle(20, 10, 2, 3)
        input_dicts = [r1, r2]

        Rectangle.save_to_file(input_dicts)
        output_dicts = Rectangle.load_from_file()

        self.assertIsInstance(output_dicts[0], Rectangle)
        self.assertIsInstance(output_dicts[1], Rectangle)
        self.assertEqual(output_dicts[0].width, 3)
        self.assertEqual(output_dicts[0].height, 5)
        self.assertEqual(output_dicts[0].x, 1)
        self.assertEqual(output_dicts[0].y, 0)

        self.assertEqual(output_dicts[1].width, 20)
        self.assertEqual(output_dicts[1].height, 10)
        self.assertEqual(output_dicts[1].x, 2)
        self.assertEqual(output_dicts[1].y, 3)
        self.assertEqual(output_dicts[1].id, 2)

    def test_load_from_csv(self):
        """Tests loading list of instances from CSV file and
        dynamically creating new instance from loaded list."""

        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle(20, 10, 2, 3)
        input_dicts = [r1, r2]

        Rectangle.save_to_file_csv(input_dicts)
        output_dicts = Rectangle.load_from_file_csv()

        self.assertIsInstance(output_dicts[0], Rectangle)
        self.assertIsInstance(output_dicts[1], Rectangle)
        self.assertEqual(output_dicts[0].width, 3)
        self.assertEqual(output_dicts[0].height, 5)
        self.assertEqual(output_dicts[0].x, 1)
        self.assertEqual(output_dicts[0].y, 0)

        self.assertEqual(output_dicts[1].width, 20)
        self.assertEqual(output_dicts[1].height, 10)
        self.assertEqual(output_dicts[1].x, 2)
        self.assertEqual(output_dicts[1].y, 3)
        self.assertEqual(output_dicts[1].id, 2)

    def test_save_to_csv(self):
        """Tests saving a list of `Rectangle` instances to a CSV file."""

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])

        loaded_instance = Rectangle.load_from_file_csv()
        to_dict = [d.to_dictionary() for d in loaded_instance]

        self.assertEqual(to_dict,
                         [r1.to_dictionary(), r2.to_dictionary()])
        self.assertEqual(r1.id, to_dict[0]['id'])
        self.assertEqual(r1.x, to_dict[0]['x'])
        self.assertEqual(r1.y, to_dict[0]['y'])
        self.assertEqual(r1.width, to_dict[0]['width'])
        self.assertEqual(r1.height, to_dict[0]['height'])

        self.assertEqual(r2.id, to_dict[1]['id'])
        self.assertEqual(r2.x, to_dict[1]['x'])
        self.assertEqual(r2.y, to_dict[1]['y'])
        self.assertEqual(r2.width, to_dict[1]['width'])
        self.assertEqual(r2.height, to_dict[1]['height'])

        os.remove("Rectangle.csv")
