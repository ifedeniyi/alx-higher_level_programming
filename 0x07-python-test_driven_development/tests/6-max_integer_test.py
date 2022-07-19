#!usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_regular(self):
        """Test with a regular list of ints: should return the max result"""
        arr = [1, 2, 3, 4, 5]
        result = max_integer(arr)
        self.assertEqual(result, 5)

    def test_not_int(self):
        """Test with a list of non-ints and ints:
        should raise a TypeError exception"""
        arr = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, arr)

    def test_empty(self):
        """Test with an empty list: should return None"""
        arr = []
        result = max_integer(arr)
        self.assertEqual(result, None)

    def test_negative(self):
        """Test with a list of negative values: should return the max"""
        arr = [-2, -6, -1]
        result = max_integer(arr)
        self.assertEqual(result, -1)

    def test_float(self):
        """Test with a list of mixed ints and floats: should return the max"""
        arr = [3, 4.5, 2]
        result = max_integer(arr)
        self.assertEqual(result, 4.5)

    def test_not_list(self):
        """Test with a parameter that's not a list: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, 7)

    def test_unique(self):
        """Test with a list of one int: should return the value of this int"""
        arr = [45]
        result = max_integer(arr)
        self.assertEqual(result, 45)

    def test_identical(self):
        """Test with a list of identical values: should return the value"""
        arr = [8, 8, 8, 8, 8]
        result = max_integer(arr)
        self.assertEqual(result, 8)

    def test_strings(self):
        """Test with a list of strings: should return the first string"""
        arr = ["hi", "hello"]
        result = max_integer(arr)
        self.assertEqual(result, "hi")

    def test_none(self):
        """Test with a None as parameter: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, None)
