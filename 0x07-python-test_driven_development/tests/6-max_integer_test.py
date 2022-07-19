#!usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([2, 4, 20]), 20)
        self.assertEqual(max_integer([1000, 10000, 500000]), 500000)
