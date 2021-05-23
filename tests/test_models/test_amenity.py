#!/usr/bin/python3
from models.amenity import Amenity
import unittest

a = Amenity()

class TestAmenity(unittest.TestCase):


    def test_amenity_id(self):
        self.assertTrue(type(a.name) is str)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
