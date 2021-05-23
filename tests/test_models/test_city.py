#!/usr/bin/python3
from models.city import City
import unittest

c = City()

class TestCity(unittest.TestCase):

    def test_state_id(self):
        self.assertTrue(type(c.state_id) is str)

    def test_city_name(self):
        self.assertTrue(type(c.name) is str)

if __name__ == '__main__':
    unittest.main()
