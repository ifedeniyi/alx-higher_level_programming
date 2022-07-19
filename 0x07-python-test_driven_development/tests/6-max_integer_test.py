#!usr/bin/python3
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestingPassingCases(unittest.TestCase):
    def testStuff(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([2, 4, 20]), 20)
        self.assertEqual(max_integer([1000, 10000, 500000]), 500000)
