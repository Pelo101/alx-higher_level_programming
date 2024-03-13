#!/usr/bin/python3
"""A module that tests rectangle"""

import unittest
from models.rectangle import Rectangle
from models.base import Base

class Test_Rectangle(unittest.TestCase):

    def test_instances(self):
        test_rectangle_instance = Rectangle(width=5, height=10)
        self.assertIsInstance(test_rectangle_instance, Rectangle)


    def test_inheritance(self):
        rectangle_instance = Rectangle(width=5, height=10)
        self.assertIsInstance(rectangle_instance, Rectangle)
        self.assertIsInstance(rectangle_instance, Base)

    def test_getter(self):
        rectangle_instance = Rectangle(width=2, height=10, x=4, y=3)

        self.assertEqual(rectangle_instance.width, 2)
        self.assertEqual(rectangle_instance.height, 10)
        self.assertEqual(rectangle_instance.x, 4)
        self.assertEqual(rectangle_instance.y, 3)



