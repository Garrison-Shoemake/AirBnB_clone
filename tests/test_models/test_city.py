#!/usr/bin/python3
"""tests for city instance"""
from models.city import City
import unittest

c = City()


class TestCity(unittest.TestCase):

    """test for Test City"""

    def test_state_id(self):
        self.assertTrue(isinstance(c.state_id, str))

    def test_city_name(self):
        self.assertTrue(isinstance(c.name, str))

if __name__ == '__main__':
    unittest.main()
