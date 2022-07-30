#!/usr/bin/python3
"""Unit tests for the `square` module.
"""
import json
import os
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the `Square` class."""

    def tearDown(self):
        Square.reset_obj_count()

    def test_complete_args(self):
        """Tests with complete args"""

        s1 = Square(10, 16, 4, "A")
        s2 = Square(5, 0, 0)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 16)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.id, "A")
        self.assertEqual(s2.x, 0)
        self.assertEqual(s2.y, 0)

    def test_access_private_attrs(self):
        """Tests failure to access private attributes"""

        s1 = Square(15, 16, 4, 1)

        with self.assertRaises(AttributeError):
            s1.__width
        with self.assertRaises(AttributeError):
            s1.__height
        with self.assertRaises(AttributeError):
            s1.__x
        with self.assertRaises(AttributeError):
            s1.__y
        with self.assertRaises(AttributeError):
            s1.__nb_objects

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
            s2.to_dictionary(), {'id': 1, 'x': 0, 'size': 10, 'y': 0})

        s1 = Square(10, 2, 1)
        s1_dict = s1.to_dictionary()
        self.assertIsInstance(s1_dict, dict)

        s2 = Square(1, 1)
        s2.update(**s1_dict)
        self.assertDictEqual(s1_dict, s2.to_dictionary())

    def test_to_json(self):
        """Tests serializing an object to JSON using `to_json_string()`."""

        s1 = Square(10, 7, 2, 8)
        dict1 = s1.to_dictionary()
        json_dict = Square.to_json_string([dict1])
        self.assertIsInstance(dict1, dict)
        self.assertIsInstance(json_dict, str)

    def test_from_json(self):
        """Tests deserializing an obj from JSON using `from_json_string()`."""

        s1 = Square(10, 7, 2, 8)
        dict1 = s1.to_dictionary()
        json_dict = Square.to_json_string([dict1])
        self.assertIsInstance(dict1, dict)
        self.assertIsInstance(json_dict, str)
        self.assertEqual([dict1], Square.from_json_string(json_dict))

    def test_save_to_file(self):
        """Tests saving a list of `Square` instances to a JSON file."""

        s1 = Square(10, 2, 3)
        s2 = Square(4)
        Square.save_to_file([s1, s2])

        with open("Square.json", "r") as f:
            json_dict = json.load(f)

            self.assertEqual(
                json_dict, [s1.to_dictionary(), s2.to_dictionary()])
            self.assertNotEqual(json_dict, [s1.to_dictionary()])

        os.remove("Square.json")

    def test_create_instance(self):
        """Tests dynamically creating new instance from a dictionary."""

        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        s2_dictionary = s2.to_dictionary()

        self.assertIsInstance(s2, Square)
        self.assertEqual(s2.size, s1.size)
        self.assertEqual(s2.x, s1.x)
        self.assertEqual(s2.y, s1.y)
        self.assertEqual(s2.id, s1.id)
        self.assertDictEqual(s1_dictionary, s2_dictionary)

    def test_load_from_file(self):
        """Tests loading list of instances from JSON file and
        dynamically creating new instance from loaded list."""

        s1 = Square(3, 5, 1)
        s2 = Square(20, 1, 2, 3)
        input_dicts = [s1, s2]

        Square.save_to_file(input_dicts)
        output_dicts = Square.load_from_file()

        self.assertIsInstance(output_dicts[0], Square)
        self.assertIsInstance(output_dicts[1], Square)

        self.assertEqual(output_dicts[0].width, 3)
        self.assertEqual(output_dicts[0].height, 3)
        self.assertEqual(output_dicts[0].size, 3)
        self.assertEqual(output_dicts[0].x, 5)
        self.assertEqual(output_dicts[0].y, 1)

        self.assertEqual(output_dicts[1].width, 20)
        self.assertEqual(output_dicts[1].height, 20)
        self.assertEqual(output_dicts[1].size, 20)
        self.assertEqual(output_dicts[1].x, 1)
        self.assertEqual(output_dicts[1].y, 2)
        self.assertEqual(output_dicts[1].id, 3)

    def test_load_from_csv(self):
        """Tests loading list of instances from CSV file and
        dynamically creating new instance from loaded list."""

        s1 = Square(3, 5, 1)
        s2 = Square(20, 10, 2, 3)
        input_dicts = [s1, s2]

        Square.save_to_file_csv(input_dicts)
        output_dicts = Square.load_from_file_csv()

        self.assertIsInstance(output_dicts[0], Square)
        self.assertIsInstance(output_dicts[1], Square)

        self.assertEqual(output_dicts[0].size, 3)
        self.assertEqual(output_dicts[0].x, 5)
        self.assertEqual(output_dicts[0].y, 1)
        self.assertEqual(output_dicts[0].id, 1)

        self.assertEqual(output_dicts[1].size, 20)
        self.assertEqual(output_dicts[1].x, 10)
        self.assertEqual(output_dicts[1].y, 2)
        self.assertEqual(output_dicts[1].id, 3)

    def test_save_to_csv(self):
        """Tests saving a list of `Square` instances to a CSV file."""

        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        Square.save_to_file_csv([s1, s2])

        loaded_instance = Square.load_from_file_csv()
        to_dict = [d.to_dictionary() for d in loaded_instance]

        self.assertEqual(to_dict,
                         [s1.to_dictionary(), s2.to_dictionary()])
        self.assertEqual(s1.id, to_dict[0]['id'])
        self.assertEqual(s1.x, to_dict[0]['x'])
        self.assertEqual(s1.y, to_dict[0]['y'])
        self.assertEqual(s1.size, to_dict[0]['size'])

        self.assertEqual(s2.id, to_dict[1]['id'])
        self.assertEqual(s2.x, to_dict[1]['x'])
        self.assertEqual(s2.y, to_dict[1]['y'])
        self.assertEqual(s2.size, to_dict[1]['size'])

        os.remove("Square.csv")
