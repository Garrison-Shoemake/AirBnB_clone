#!/usr/bin/python3
""" This is the unit test for amenity.py  """

from models.amenity import Amenity
import unittest

a = Amenity()


class TestAmenity(unittest.TestCase):
    """ only one test for amenity's single attribute """

    def test_amenity_id(self):
        self.assertTrue(isinstance(a.name, str))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
