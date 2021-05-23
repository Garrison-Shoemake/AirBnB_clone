#!/usr/bin/python3
"""tests for city instance"""
from models.city import City
import unittest

c = City()


class TestCity(unittest.TestCase):
    """test for Test City"""

    def test_state_id(self):
        """ test for state id"""
        self.assertTrue(isinstance(c.state_id, str))

    def test_city_name(self):
        """test for city name"""
        self.assertTrue(isinstance(c.name, str))

if __name__ == '__main__':
    unittest.main()
