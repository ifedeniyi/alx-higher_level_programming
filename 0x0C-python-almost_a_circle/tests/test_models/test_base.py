#!/usr/bin/env python3
"""Unittest for `base` module functionality
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.a1 = Base(12)
        self.a2 = Base(7)

    def test_no_param(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        with self.assertRaises(AttributeError):
            type(self.b2).__nb_objects
            type(self.b2).nb_objects

    def test_param(self):
        self.assertEqual(self.a1.id, 12)
        self.assertEqual(self.b1.id, 4)
        self.assertEqual(self.a2.id, 7)
