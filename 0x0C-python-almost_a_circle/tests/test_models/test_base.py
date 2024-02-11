#!/usr/bin/python3
""" Unittest for Base Module """
import unittest
from models.base import Base


class test_Baseclass(unittest.TestCase):
    """ Test base class"""

    def test_base_id(self):

             obj1 = Base()
             self.assertEqual(obj1.id, 1)

             obj2 = Base()
             self.assertEqual(obj2.id, 2)

             obj3 = Base()
             self.assertEqual(obj3.id, 3)

             obj4 = Base(12)
             self.assertEqual(obj4.id, 12)

             obj5 = Base(4)
             self.assertEqual(obj5.id, 4)

             obj6 = Base(5.5)
             self.assertEqual(obj6.id, 5.5)

             obj7 = Base(-4)
             self.assertEqual(obj7.id, -4)

             obj8 = Base(None)
             self.assertEqual(obj8.id, 4)


    if __name__ == '__main__':
        unittest.main()

